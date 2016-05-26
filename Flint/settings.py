import os
from curve import *
from track import *
import xml.etree.ElementTree as etree

def read_log_template(file_path):
    if os.path.exists(file_path):
        lines = []
        tracks = []
        curves = []
        tree = etree.parse(file_path)
        root = tree.getroot()        
        for child in root:
            #print(child.tag)
            #for element in child:
                #print(child.tag, child.attrib, element.tag, element.text)
            if child.tag == 'track':
                t = track(100, 'linear')
                for element in child:
                    #print(str('\t') + str(element.text))
                    if element.tag == 'width':
                        try:
                            t.width = float(element.text)
                        except:
                            print('Error getting width of track for ' + child.tag, child.attrib, element.tag, element.text)
                    if element.tag == 'type':                        
                        t.type = element.text
                    if element.tag == 'num_divisions':
                        try:
                            t.num_divisions = float(element.text)
                        except:
                            print('Error getting number of track divisions for ' + child.tag, child.attrib, element.tag, element.text)
                    if element.tag == 'spacing':
                        try:
                            t.spacing = float(element.text)
                        except:
                            print('Error getting spacing for ' + child.tag, child.attrib, element.tag, element.text)
                    if element.tag == 'left':
                        try:
                            t.left = float(element.text)
                        except:
                            print('Error getting left scale for ' + child.tag, child.attrib, element.tag, element.text)
                    if element.tag == 'right':
                        try:
                            t.right = float(element.text)
                        except:
                            print('Error getting right scale for ' + child.tag, child.attrib, element.tag, element.text)
                    if element.tag == 'horizontal':
                        try:
                            t.horizontal = float(element.text)
                        except:
                            print('Error getting horizontal line spacing for ' + child.tag, child.attrib, element.tag, element.text)
                tracks.append(t)
            if child.tag == 'curve':
                c = curve('', '', '', '', '' , True)
                for element in child:
                    #print(str('\t') + str(element.text))
                    if element.tag == 'name':
                        c.name = element.text
                    if element.tag == 'left':
                        try:
                            c.left = float(element.text)
                        except:
                            print('Error getting curve left scale for ' + child.tag, child.attrib, element.tag, element.text)
                    if element.tag == 'right':
                        try:
                            c.right = float(element.text)
                        except:
                            print('Error getting curve right scale for ' + child.tag, child.attrib, element.tag, element.text)
                    if element.tag == 'color':
                        c.color = element.text
                    if element.tag == 'track_num':
                        try:
                            c.track_num = int(element.text)
                        except:
                            print('Error getting track number for curve' + child.tag, child.attrib, element.tag, element.text)
                    if element.tag == 'type':
                        c.type = element.text
                    if element.tag == 'fill_color':
                        c.fill_color = element.text
                curves.append(c)
        return tracks, curves
