import tkinter as tk
import ttkbootstrap as ttk
import os
import sys
from os.path import dirname, abspath

# cwd to .exe directory
os.chdir(dirname(abspath(sys.argv[0])))

# app functionality
def change_input_menu_wgs84():
    pass

def change_input_menu_prs92():
    pass

def change_output_menu_wgs84():
    pass

def change_output_menu_prs92():
    pass

# app geometry
root = ttk.Window(title="CBA's Coordinates Converter", themename="darkly")
root.iconbitmap("converter-icon.ico")
root_width = 425
root_height = 400
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

# app mainloop
root.mainloop()