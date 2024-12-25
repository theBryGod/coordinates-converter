import tkinter as tk
import ttkbootstrap as ttk
import os
import sys
from os.path import dirname, abspath

# cwd to .exe directory
os.chdir(dirname(abspath(sys.argv[0])))

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

# app mainloop
root.mainloop()