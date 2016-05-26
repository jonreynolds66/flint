

def right_align_text(value, width):
    t = str(value)
    for i in range(len(str(value)), int(width)):
        t = ' ' + str(t)
    return t

def left_align_text(value, width):
    t = str(value)
    for i in range(len(str(value)), int(width)):
        t = t + ' '
    return t

def entry(value, unit, width):
    temp = str(unit)
    for i in range(len(unit), (int(width) - len(str(value)))):
        temp = temp + ' '
    temp = temp + str(value)
    return temp

def curve_line(curve_name, units, description):
    width1 = 12
    width2 = 35
    temp = str(curve_name)
    for i in range(len(str(curve_name)), int(width1)):
        temp += ' '
    temp += '.' + str(units)
    for i in range(len(str(units)), int(width2)):
        temp += ' '
    temp += ' : ' + str(description)
    return temp