import tkinter as tk
import ttkbootstrap as ttk
import os
import sys
from os.path import dirname, abspath
from tkinter import filedialog

# cwd to .exe directory
os.chdir(dirname(abspath(sys.argv[0])))

# app functionality
def change_input_menu_wgs84():
    var_mb_input_format.set("")
    var_input_menu_options = ttk.Menu(mb_input_format)
    options = ["WGS84 Degrees", "WGS84 50N", "WGS84 51N"]
    for option in options:
        var_input_menu_options.add_radiobutton(label=option, command=lambda x=option: var_mb_input_format.set(x))
    mb_input_format["menu"] = var_input_menu_options

def change_input_menu_prs92():
    var_mb_input_format.set("")
    var_input_menu_options = ttk.Menu(mb_input_format)
    options = ["PRS92 Degrees", "PRS92 Zone 1", "PRS92 Zone 2", "PRS92 Zone 3", "PRS92 Zone 4", "PRS92 Zone 5"]
    for option in options:
        var_input_menu_options.add_radiobutton(label=option, command=lambda x=option: var_mb_input_format.set(x))
    mb_input_format["menu"] = var_input_menu_options

def change_output_menu_wgs84():
    var_mb_output_format.set("")
    var_output_menu_options = ttk.Menu(mb_output_format)
    options = ["WGS84 Degrees", "WGS84 50N", "WGS84 51N"]
    for option in options:
        var_output_menu_options.add_radiobutton(label=option, command=lambda x=option: var_mb_output_format.set(x))
    mb_output_format["menu"] = var_output_menu_options

def change_output_menu_prs92():
    var_mb_output_format.set("")
    var_output_menu_options = ttk.Menu(mb_output_format)
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
    pass

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
                                           command=change_input_menu_wgs84)
rdbtn_input_system_wgs84.pack(padx=5, pady=(2, 0), anchor="w")
rdbtn_input_system_prs92 = ttk.Radiobutton(master=lblfrm_input_system,
                                           text="PRS92",
                                           variable=var_input_system,
                                           value="prs92",
                                           command=change_input_menu_prs92)
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
                                           command=change_output_menu_wgs84)
rdbtn_output_system_wgs84.pack(padx=5, pady=(2, 0), anchor="w")
rdbtn_output_system_prs92 = ttk.Radiobutton(master=lblfrm_output_system,
                                           text="PRS92",
                                           variable=var_output_system,
                                           value="prs92",
                                           command=change_output_menu_prs92)
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
ent_status = ttk.Entry(frm_status, textvariable=var_status, state="disabled", width=48, justify="center")
ent_status.pack(padx=5)

# app mainloop
root.mainloop()