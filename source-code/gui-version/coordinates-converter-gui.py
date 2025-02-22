import tkinter as tk
import ttkbootstrap as ttk
import os
import sys
import csv
from os.path import dirname, abspath
from tkinter import filedialog
from pyproj import Transformer

# cwd to .exe directory
os.chdir(dirname(abspath(sys.argv[0])))

# app functionality
def change_input_menu():
    var_mb_input_format.set("")
    var_input_menu_options = ttk.Menu(mb_input_format)
    selected = var_input_system.get()
    if selected == "wgs84":
        options = ["WGS84 Degrees", "WGS84 50N", "WGS84 51N"]
    elif selected == "prs92":
        options = ["PRS92 Degrees", "PRS92 Zone 1", "PRS92 Zone 2", "PRS92 Zone 3", "PRS92 Zone 4", "PRS92 Zone 5"]
    for option in options:
        var_input_menu_options.add_radiobutton(label=option, command=lambda x=option: var_mb_input_format.set(x))
    mb_input_format["menu"] = var_input_menu_options

def change_output_menu():
    var_mb_output_format.set("")
    var_output_menu_options = ttk.Menu(mb_output_format)
    selected = var_output_system.get()
    if selected == "wgs84":
        options = ["WGS84 Degrees", "WGS84 50N", "WGS84 51N"]
    elif selected == "prs92":
        options = ["PRS92 Degrees", "PRS92 Zone 1", "PRS92 Zone 2", "PRS92 Zone 3", "PRS92 Zone 4", "PRS92 Zone 5"]
    for option in options:
        var_output_menu_options.add_radiobutton(label=option, command=lambda x=option: var_mb_output_format.set(x))
    mb_output_format["menu"] = var_output_menu_options

def open_file():
    target = filedialog.askopenfilename()
    var_filename.set(target)
    if not target:
        var_status.set("")
    elif not target.endswith(".csv"):
        ent_status.configure(foreground="#FF3600")
        var_status.set("Invalid file type. Please select a CSV file.")
        btn_convert.configure(state="disabled")
        target = None
    else:
        ent_status.configure(foreground="#22DD22")
        var_status.set("CSV file selected. Press the button to start the conversion.")
        btn_convert.configure(state="enabled")
        return target
    
def convert():
    input_coordinates = []
    with open(var_filename.get(), "r") as file:
        reader = csv.reader(file)
        for row in reader:
            input_coordinates.append(row)
    EPSG_codes = {
        "prs92,deg":"EPSG:4683",
        "prs92,z1":"EPSG:3121",
        "prs92,z2":"EPSG:3122",
        "prs92,z3":"EPSG:3123",
        "prs92,z4":"EPSG:3124",
        "prs92,z5":"EPSG:3125",
        "wgs84,deg":"EPSG:4326",
        "wgs84,50n":"EPSG:32650",
        "wgs84,51n":"EPSG:32651"
    }
    dict_input_output_settings = {
        "WGS84 Degrees":"wgs84,deg",
        "WGS84 50N":"wgs84,50n",
        "WGS84 51N":"wgs84,51n",
        "PRS92 Degrees":"prs92,deg",
        "PRS92 Zone 1":"prs92,z1",
        "PRS92 Zone 2":"prs92,z2",
        "PRS92 Zone 3":"prs92,z3",
        "PRS92 Zone 4":"prs92,z4",
        "PRS92 Zone 5":"prs92,z5"
    }
    input_settings = dict_input_output_settings.get(var_mb_input_format.get())
    output_settings = dict_input_output_settings.get(var_mb_output_format.get())
    pyproj_transformer = Transformer.from_crs(EPSG_codes.get(input_settings), EPSG_codes.get(output_settings), always_xy=True)
    input_x = []
    input_y = []
    for i, xy in enumerate(input_coordinates):
        try:
            input_x.append(input_coordinates[i][0])
            input_y.append(input_coordinates[i][1])
        except IndexError:
            ent_status.configure(foreground="#FF3600")
            var_status.set("Invalid input coordinates. Please try again...")
            return
    output_coords = []
    for n in range(len(input_coordinates)):
        try:
            output_coord = pyproj_transformer.transform(input_x[n], input_y[n])
            output_coords.append(output_coord)
        except TypeError:
            ent_status.configure(foreground="#FF3600")
            var_status.set("Invalid input coordinates. Please recheck the input CSV file and try again.")
            return
    with open(f"{var_filename.get()} -to- {var_mb_output_format.get()}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for xy in output_coords:
            writer.writerow(xy)
    ent_status.configure(foreground="#22DD22")
    var_status.set(f"Conversion from {var_mb_input_format.get()} to {var_mb_output_format.get()} completed.")
    
# app geometry
root = ttk.Window(title="CBA's Coordinates Converter", themename="darkly")
root.iconbitmap("converter-icon.ico")
root_width = 570
root_height = 320
root.geometry(f"{root_width}x{root_height}")
root.minsize(root_width, root_height)
root.maxsize(root_width, root_height)

# app layout ###

# title ##
frm_title_label = ttk.Frame(master=root)
frm_title_label.pack(pady=(5, 0), side="top")
lbl_title_label = ttk.Label(master=frm_title_label, text="CBA's Coordinates Converter - PRS92 ⇌ WGS84", font="Calibri 10 bold")
lbl_title_label.pack()

# input - output settings ##
frm_io_settings = ttk.Frame(master=root)
frm_io_settings.pack()

# input settings
frm_input_settings = ttk.Frame(master=frm_io_settings)
frm_input_settings.pack(side="left", padx=5)
lblfrm_input_system = ttk.LabelFrame(master=frm_input_settings, text="Converting from:")
lblfrm_input_system.pack(pady=5)
var_input_system = ttk.StringVar()
var_mb_input_format = ttk.StringVar()
mb_input_format = ttk.Menubutton(frm_input_settings, width=14, bootstyle="secondary", textvariable=var_mb_input_format)
rdbtn_input_system_wgs84 = ttk.Radiobutton(master=lblfrm_input_system,
                                           text="WGS84",
                                           variable=var_input_system,
                                           value="wgs84",
                                           command=change_input_menu)
rdbtn_input_system_wgs84.pack(padx=5, pady=(2, 0), anchor="w")
rdbtn_input_system_prs92 = ttk.Radiobutton(master=lblfrm_input_system,
                                           text="PRS92",
                                           variable=var_input_system,
                                           value="prs92",
                                           command=change_input_menu)
rdbtn_input_system_prs92.pack(padx=5, pady=2, anchor="w")
lbl_menu_input_format_desc = ttk.Label(master=frm_input_settings, text="Input coordinates format:")
lbl_menu_input_format_desc.pack()
mb_input_format.pack(pady=5)

# output settings
frm_output_settings = ttk.Frame(master=frm_io_settings)
frm_output_settings.pack(side="left", padx=5)
lblfrm_output_system = ttk.LabelFrame(master=frm_output_settings, text="Converting to:")
lblfrm_output_system.pack(pady=5)
var_output_system = ttk.StringVar()
var_mb_output_format = ttk.StringVar()
mb_output_format = ttk.Menubutton(frm_output_settings, width=14, bootstyle="secondary", textvariable=var_mb_output_format)
rdbtn_output_system_wgs84 = ttk.Radiobutton(master=lblfrm_output_system,
                                           text="WGS84",
                                           variable=var_output_system,
                                           value="wgs84",
                                           command=change_output_menu)
rdbtn_output_system_wgs84.pack(padx=5, pady=(2, 0), anchor="w")
rdbtn_output_system_prs92 = ttk.Radiobutton(master=lblfrm_output_system,
                                           text="PRS92",
                                           variable=var_output_system,
                                           value="prs92",
                                           command=change_output_menu)
rdbtn_output_system_prs92.pack(padx=5, pady=2, anchor="w")
lbl_menu_output_format_desc = ttk.Label(master=frm_output_settings, text="Output coordinates format:")
lbl_menu_output_format_desc.pack()
mb_output_format.pack(pady=5)

# File picker
frm_file = ttk.Frame(root)
frm_file.pack(pady=10)
lbl_filename = ttk.Label(frm_file, text="File:")
lbl_filename.pack(side="left")
var_filename = ttk.StringVar() 
ent_filename = ttk.Entry(frm_file, textvariable = var_filename, state="disabled", width=48, justify="center", foreground="white")
ent_filename.pack(side="left", padx=10)
btn_filename = ttk.Button(frm_file, text="Select file...", command=open_file)
btn_filename.pack()
btn_convert = ttk.Button(root, text="Convert", state="disabled", command=convert)
btn_convert.pack()
frm_status = ttk.Frame(root)
frm_status.pack(pady=10)
lbl_status = ttk.Label(frm_status, text="Status:")
lbl_status.pack(side="left")
var_status = ttk.StringVar()
ent_status = ttk.Entry(frm_status, textvariable=var_status, state="disabled", width=60, justify="center")
ent_status.pack(padx=5)

# app mainloop
root.mainloop()