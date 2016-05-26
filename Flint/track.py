from tkinter import *
import track_helper
import math
from decimal import Decimal


class track:
    def __init__(self,WIDTH,TYPE):
        self.width = WIDTH
        self.type = TYPE        # LINEAR / LOG / DEPTH
        self.num_divisions = 0  # if linear - number of vertical divisions
        self.spacing = 50       # every so many feet display depth
        self.left = 0.2         # logarithmic track left scale
        self.right = 2000       # logarithmic track right scale
        self.horizontal = 10    # horizontal line spacing in ft
        
def Calculate_Canvas_Width(track_list):    
    offset = 2
    width = offset
    for i in range(len(track_list)):
        width += track_list[i].width + offset
    return width

def Draw_Tracks_on_Canvas(track_list, canvas, canvas_height, depth_list):
    offset = 2
    x_counter = offset
    for i in range(len(track_list)):        
        if track_list[i].type == 'linear':            
            div_spacing = track_list[i].width / track_list[i].num_divisions            
            # vertical lines
            for j in range(1, int(track_list[i].num_divisions)):
                 canvas.create_line(int(x_counter + (div_spacing * j)), offset+1, int(x_counter + (div_spacing * j)), canvas_height - offset - 1, fill='gray80')
            depth_step_rate = depth_list[1] - depth_list[0]
            start_index = 0
            for j in range(0,len(depth_list)):
                if depth_list[j] % track_list[i].horizontal == 0:                    
                    start_index = j
                    break
            # horizontal lines
            for j in range(start_index, len(depth_list), int(track_list[i].horizontal / depth_step_rate)):
                canvas.create_line(x_counter+1, j, x_counter + track_list[i].width, j, fill = 'gray80')
        if track_list[i].type == 'depth':
            mid_x = x_counter + (track_list[i].width / 2)
            depth_step_rate = depth_list[1] - depth_list[0]
            start_index = offset
            for j in range(0,len(depth_list)):
                if depth_list[j] % track_list[i].spacing == 0:                    
                    start_index = j
                    break
            for j in range(start_index,len(depth_list),int(track_list[i].spacing / depth_step_rate)):
                canvas.create_text(mid_x, j, text=str(depth_list[j]))
        if track_list[i].type == 'log':            
            num_div = math.log10(track_list[i].right) - math.log10(track_list[i].left)
            #print('Num divisions: ' + str(num_div))
            left = track_list[i].left            
            num = left
            x_offset = math.log10(track_list[i].left)
            for j in range(0, int(num_div)+1):
                #print(str(j) + '\t' + str(num) + '\t' + str(math.log10(num)) + '\t' + str(math.log10(num) - x_offset) + '\t' + str(track_helper.Additive_for_Log_Chart(num)))
                a = track_helper.Additive_for_Log_Chart(num)
                b = track_helper.Additive_for_Log_Chart(num)
                t = num
                while(a == b and (math.log10(t) - x_offset) < num_div):
                    #print(str(t) + '\t' + str(math.log10(t) - x_offset) + '\t' + str(' '))
                    c = track_list[i].width * (math.log10(t) - x_offset) / num_div
                    canvas.create_line(c + x_counter, offset+1, c + x_counter, canvas_height - offset - 1, fill='gray80')
                    t += b                    
                    b = track_helper.Additive_for_Log_Chart(t)
                canvas.create_line(c + x_counter, offset+1, c + x_counter, canvas_height - offset - 1, fill='gray40')
                num *= 10
        canvas.create_rectangle(x_counter, offset, track_list[i].width + x_counter, canvas_height - offset)                    
        x_counter += offset + track_list[i].width

def Draw_Tracks_and_Curves_on_Canvas(track_list, canvas, canvas_height, data_list, curve_list, curve_names):
    depth_list = data_list[0]
    offset = 2
    x_counter = offset
    for i in range(len(track_list)):        
        if track_list[i].type == 'linear':            
            div_spacing = track_list[i].width / track_list[i].num_divisions            
            # vertical lines
            for j in range(1, int(track_list[i].num_divisions)):
                 canvas.create_line(int(x_counter + (div_spacing * j)), offset+1, int(x_counter + (div_spacing * j)), canvas_height - offset - 1, fill='gray80')
            # horizontal lines
            depth_step_rate = depth_list[1] - depth_list[0]
            start_index = 0
            for j in range(0,len(depth_list)):
                if depth_list[j] % track_list[i].horizontal == 0:                    
                    start_index = j
                    break            
            for j in range(start_index, len(depth_list), int(track_list[i].horizontal / depth_step_rate)):
                canvas.create_line(x_counter+1, j, x_counter + track_list[i].width, j, fill = 'gray80')
        if track_list[i].type == 'depth':
            mid_x = x_counter + (track_list[i].width / 2)
            depth_step_rate = depth_list[1] - depth_list[0]
            start_index = offset
            for j in range(0,len(depth_list)):
                if depth_list[j] % track_list[i].spacing == 0:                    
                    start_index = j
                    break
            for j in range(start_index,len(depth_list),int(track_list[i].spacing / depth_step_rate)):
                canvas.create_text(mid_x, j, text=str(depth_list[j]))
        if track_list[i].type == 'log':            
            num_div = math.log10(track_list[i].right) - math.log10(track_list[i].left)
            #print('Num divisions: ' + str(num_div))
            left = track_list[i].left            
            num = left
            x_offset = math.log10(track_list[i].left)
            #print('X offset' + str(x_offset))
            # vertical lines
            for j in range(0, int(num_div)+1):
                #print(str(j) + '\t' + str(num) + '\t' + str(math.log10(num)) + '\t' + str(math.log10(num) - x_offset) + '\t' + str(track_helper.Additive_for_Log_Chart(num)))
                a = track_helper.Additive_for_Log_Chart(num)
                b = track_helper.Additive_for_Log_Chart(num)
                t = float(num)
                #print('A: ' + str(a) + '\tB: ' + str(b) + '\tT: ' + str(t))
                while(a == b and (math.log10(t) - x_offset) < num_div):                
                    #print(str(t) + '\t' + str(math.log10(t) - x_offset) + '\t' + str(' '))
                    c = track_list[i].width * (math.log10(t) - x_offset) / num_div
                    #print(str(c) + '\t' + str(x_counter) + '\t' + str(t))
                    canvas.create_line(c + x_counter, offset+1, c + x_counter, canvas_height - offset - 1, fill='gray80')
                    if t < 1:
                        decimal_places = len(str(t)) - 2
                        t = round(t + b, decimal_places)
                    else:
                        t = float(t) + float(b)
                    b = track_helper.Additive_for_Log_Chart(t)
                    #print('t:' + str(t) + '\tb: ' + str(b))
                canvas.create_line(c + x_counter + offset, offset+1, c + x_counter + offset, canvas_height - offset - 1, fill='gray40')
                num *= 10
            # horizontal lines
            depth_step_rate = depth_list[1] - depth_list[0]
            start_index = 0
            for j in range(0,len(depth_list)):
                if depth_list[j] % track_list[i].horizontal == 0:                    
                    start_index = j
                    break            
            for j in range(start_index, len(depth_list), int(track_list[i].horizontal / depth_step_rate)):
                canvas.create_line(x_counter+1, j, x_counter + track_list[i].width, j, fill = 'gray80')
        canvas.create_rectangle(x_counter, offset, track_list[i].width + x_counter, canvas_height - offset)   
        # draw curves in track
        for j in range(len(curve_list)):
            if curve_list[j].track_num - 1 == i:
                #print('put ' + str(curve_list[j].name) + ' in track ' + str(i+1))
                index = -1
                try:                    
                    curve_num = curve_names.index(curve_list[j].name)                    
                    if curve_list[j].type == 'linear':
                        if curve_list[j].left < curve_list[j].right:
                            for k in range(1, len(depth_list)):
                                x1 = ((data_list[curve_num][k-1] - curve_list[j].left) / math.fabs(curve_list[j].right - curve_list[j].left)) * track_list[i].width                            
                                x1 = limit_value(x1, 0, track_list[i].width)
                                x2 = ((data_list[curve_num][k] - curve_list[j].left) / math.fabs(curve_list[j].right - curve_list[j].left)) * track_list[i].width
                                x2 = limit_value(x2, 0, track_list[i].width)
                                if x1 > 0 and x2 > 0 and x2 < track_list[i].width and x1 < track_list[i].width:
                                    canvas.create_line(x1 + x_counter, offset + k - 1, x2 + x_counter, offset + k, fill=curve_list[j].color)
                        if curve_list[j].left > curve_list[j].right:
                            for k in range(1, len(depth_list)):
                                x1 = ((data_list[curve_num][k-1] - curve_list[j].right) / math.fabs(curve_list[j].left - curve_list[j].right)) * track_list[i].width                            
                                x1 = limit_value(x1, 0, track_list[i].width)
                                x2 = ((data_list[curve_num][k] - curve_list[j].right) / math.fabs(curve_list[j].left - curve_list[j].right)) * track_list[i].width
                                x2 = limit_value(x2, 0, track_list[i].width)
                                if x1 > 0 and x2 > 0 and x2 < track_list[i].width and x1 < track_list[i].width:
                                    canvas.create_line(x_counter + track_list[i].width - x1, offset + k - 1, x_counter + track_list[i].width - x2, offset + k, fill=curve_list[j].color)
                    if  curve_list[j].type == 'log':
                        if curve_list[j].left < curve_list[j].right:
                            for k in range(1, len(depth_list)):
                                if data_list[curve_num][k-1] != -9999 and data_list[curve_num][k] != -9999:
                                    x1 = ((math.log10(data_list[curve_num][k-1]) - math.log10(curve_list[j].left)) / num_div) * track_list[i].width                            
                                    x1 = limit_value(x1, 0, track_list[i].width)
                                    x2 = ((math.log10(data_list[curve_num][k]) - math.log10(curve_list[j].left)) / num_div) * track_list[i].width                            
                                    x2 = limit_value(x2, 0, track_list[i].width)
                                    #if data_list[0][k] % 50 == 0:
                                        #print('log value: ' + str(data_list[curve_num][k]) + '\tlog10(' + str(data_list[curve_num][k]) + '): ' + str(math.log10(data_list[curve_num][k])))
                                    if x1 >= 0 and x2 >= 0 and x2 <= track_list[i].width and x1 <= track_list[i].width:
                                        canvas.create_line(x1 + x_counter, offset + k - 1, x2 + x_counter, offset + k, fill=curve_list[j].color)                                
                    if curve_list[j].type == 'fill_right':
                        if curve_list[j].left < curve_list[j].right:
                            coords = []                            
                            x1 = x_counter + track_list[i].width
                            y1 = offset
                            x2 = 0
                            y2 = 0
                            coords.append(x1)
                            coords.append(y1)
                            for k in range(1, len(depth_list)):
                                x1 = ((data_list[curve_num][k-1] - curve_list[j].left) / math.fabs(curve_list[j].right - curve_list[j].left)) * track_list[i].width                            
                                x1 = limit_value(x1, 0, track_list[i].width)
                                x2 = ((data_list[curve_num][k] - curve_list[j].left) / math.fabs(curve_list[j].right - curve_list[j].left)) * track_list[i].width
                                x2 = limit_value(x2, 0, track_list[i].width)
                                if x1 > 0 and x2 > 0 and x2 < track_list[i].width and x1 < track_list[i].width:
                                    coords.append(x_counter + x1)
                                    coords.append(offset + k - 1)                                    
                            coords.append(x_counter + x2)
                            coords.append(offset + k)
                            coords.append(x_counter  + track_list[i].width)
                            coords.append(canvas_height)                            
                            canvas.create_polygon(coords, outline=curve_list[j].color, fill=curve_list[j].fill_color)
                        else:
                            coords = []                            
                            x1 = x_counter + track_list[i].width
                            y1 = offset
                            x2 = 0
                            y2 = 0
                            coords.append(x1)
                            coords.append(y1)
                            for k in range(1, len(depth_list)):
                                x1 = ((data_list[curve_num][k-1] - curve_list[j].right) / math.fabs(curve_list[j].left - curve_list[j].right)) * track_list[i].width                            
                                x1 = limit_value(x1, 0, track_list[i].width)
                                x2 = ((data_list[curve_num][k] - curve_list[j].right) / math.fabs(curve_list[j].left - curve_list[j].right)) * track_list[i].width
                                x2 = limit_value(x2, 0, track_list[i].width)
                                if x1 > 0 and x2 > 0 and x2 < track_list[i].width and x1 < track_list[i].width:
                                    coords.append(x_counter + track_list[i].width - x1)
                                    coords.append(offset + k - 1)                                    
                            coords.append(x_counter + track_list[i].width - x2)
                            coords.append(offset + k)
                            coords.append(x_counter + track_list[i].width)
                            coords.append(canvas_height)                            
                            canvas.create_polygon(coords, outline=curve_list[j].color, fill=curve_list[j].fill_color)
                    if curve_list[j].type == 'fill_left':
                        if curve_list[j].left < curve_list[j].right:
                            coords = []                            
                            x1 = x_counter 
                            y1 = offset
                            x2 = 0
                            y2 = 0
                            coords.append(x1)
                            coords.append(y1)
                            for k in range(1, len(depth_list)):
                                x1 = ((data_list[curve_num][k-1] - curve_list[j].left) / math.fabs(curve_list[j].right - curve_list[j].left)) * track_list[i].width                            
                                x1 = limit_value(x1, 0, track_list[i].width)
                                x2 = ((data_list[curve_num][k] - curve_list[j].left) / math.fabs(curve_list[j].right - curve_list[j].left)) * track_list[i].width
                                x2 = limit_value(x2, 0, track_list[i].width)
                                if x1 > 0 and x2 > 0 and x2 < track_list[i].width and x1 < track_list[i].width:
                                    coords.append(x_counter + x1)
                                    coords.append(offset + k - 1)                                    
                            coords.append(x_counter + x2)
                            coords.append(offset + k)
                            coords.append(x_counter)
                            coords.append(canvas_height)                            
                            canvas.create_polygon(coords, outline=curve_list[j].color, fill=curve_list[j].fill_color)
                        else:
                            coords = []                            
                            x1 = x_counter
                            y1 = offset
                            x2 = 0
                            y2 = 0
                            coords.append(x1)
                            coords.append(y1)
                            for k in range(1, len(depth_list)):
                                x1 = ((data_list[curve_num][k-1] - curve_list[j].right) / math.fabs(curve_list[j].left - curve_list[j].right)) * track_list[i].width                            
                                x1 = limit_value(x1, 0, track_list[i].width)
                                x2 = ((data_list[curve_num][k] - curve_list[j].right) / math.fabs(curve_list[j].left - curve_list[j].right)) * track_list[i].width
                                x2 = limit_value(x2, 0, track_list[i].width)
                                if x1 > 0 and x2 > 0 and x2 < track_list[i].width and x1 < track_list[i].width:
                                    coords.append(x_counter + track_list[i].width - x1)
                                    coords.append(offset + k - 1)                                    
                            coords.append(x_counter + track_list[i].width - x2)
                            coords.append(offset + k)
                            coords.append(x_counter)
                            coords.append(canvas_height)                            
                            canvas.create_polygon(coords, outline=curve_list[j].color, fill=curve_list[j].fill_color)

                except Exception as exc:                
                    print('Error on curve ' + str(curve_list[j].name) + ' ' + str(exc))    
                    print('Row: ' + str(k))
                    pass                        
        x_counter += offset + track_list[i].width

def limit_value(value, min_value, max_value):
        if value < min_value:
            return min_value
        if value > max_value:
            return max_value
        return value