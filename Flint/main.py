import las_file
import os
import settings
import curve
import track
from tkinter import *

file_path = r'..\data\42383394070000_PETRO.las'
#file_path = r'..\data\test.las'
log_template = r'..\data\log_template.xml'

canvas_width = ''
canvas_height = ''

if os.path.exists(file_path):
    
    las = las_file.read(file_path)
    tracks, curves = settings.read_log_template(log_template)
    canvas_width = track.Calculate_Canvas_Width(tracks)
    canvas_height = len(las.curve_data[0]) + (2 * 2)
    header_height = 200
    master = Tk()

    header_frame = Frame(master)
    header_canvas = Canvas(header_frame, width = canvas_width, height = header_height, scrollregion = (0,0,canvas_width,header_height))

    xscrollbarheader = Scrollbar(header_frame, orient=HORIZONTAL)
    xscrollbarheader.pack(side = BOTTOM, fill = X)
    xscrollbarheader.config(command = header_canvas.xview)
    yscrollbarheader = Scrollbar(header_frame, orient=VERTICAL)
    yscrollbarheader.pack(side = RIGHT, fill = Y)
    yscrollbarheader.config(command = header_canvas.yview)
    header_canvas.config(xscrollcommand = xscrollbarheader.set, yscrollcommand = yscrollbarheader.set)
    header_canvas.pack(side = LEFT, expand = True, fill = BOTH)
    header_frame.pack(side = TOP)

    frame = Frame(master)
    canvas = Canvas(frame, width = canvas_width, height = canvas_height,scrollregion = (0,0,canvas_width,canvas_height))    
    
    #track.Draw_Tracks_on_Canvas(tracks, canvas, canvas_height,las.curve_data[0])
    track.Draw_Tracks_and_Curves_on_Canvas(tracks, canvas, canvas_height, las.curve_data, curves, las.curve_names)

    xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
    xscrollbar.pack(side = BOTTOM, fill = X)
    xscrollbar.config(command = canvas.xview)
    yscrollbar = Scrollbar(frame, orient=VERTICAL)
    yscrollbar.pack(side = RIGHT, fill = Y)
    yscrollbar.config(command = canvas.yview)
    canvas.config(xscrollcommand = xscrollbar.set, yscrollcommand = yscrollbar.set)
    canvas.pack(side = LEFT, expand = True, fill = BOTH)
    frame.pack(side = LEFT)

    master.wm_title(str(las.well_name))
    mainloop()
