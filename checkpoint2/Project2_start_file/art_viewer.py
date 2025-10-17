"""
Name: David Martinez Rodriguez
CSC 201
Programming Project 2

Description: This program reads a text file with an art extension and draws
             the "pointillistic" version of an image from the data in the file.
             The largest dimension is specified and the smaller dimension set
             proportionally.

Assistance:
I gave and received no assistance on this project.
"""

from graphics2 import *
import tkinter as tk
from tkinter import filedialog

MAX_WINDOW_DIMENSION = 600

def main():
    #allows you to choose a file
    root = tk.Tk()
    root.withdraw()
    artFileName = filedialog.askopenfilename()
    #artFileName = './gallery/bird_184.art'  # use this code if the file chooser doesn't work on your computer

    #add your code here
    if artFileName[-4:] != '.art':
        print("Invalid file format. Must choose an 'art' file.")
        print("Ending execution.")
        exit(-1)
    
    input_file = open(artFileName, 'r')
    
    first_line = input_file.readline()
    dimensions = first_line.split()
    original_width = int(dimensions[0])
    original_height = int(dimensions[1])
    
    second_line = input_file.readline()
    background_color_number = int(second_line)
    
    if original_width > original_height:
        window_width = MAX_WINDOW_DIMENSION
        window_height = MAX_WINDOW_DIMENSION * (original_height / original_width)
    else:
        window_height = MAX_WINDOW_DIMENSION
        window_width = MAX_WINDOW_DIMENSION * (original_width / original_height)
    
    win = GraphWin("Art Viewer", window_width, window_height)
    
    if background_color_number == 1:
        win.setBackground("white")
    else:
        win.setBackground("black")
    
    for line in input_file:
        parts = line.split()
        x = int(parts[0])
        y = int(parts[1])
        red = int(parts[2])
        green = int(parts[3])
        blue = int(parts[4])
        size = int(parts[5])
        
        scaled_x = x * (window_width / original_width)
        scaled_y = y * (window_height / original_height)
        scaled_width = size * (window_width / original_width)
        scaled_height = size * (window_height / original_height)
        
        top_left = Point(scaled_x, scaled_y)
        bottom_right = Point(scaled_x + scaled_width, scaled_y + scaled_height)
        
        square = Rectangle(top_left, bottom_right)
        square_color = color_rgb(red, green, blue)
        square.setFill(square_color)
        square.setOutline(square_color)
        square.draw(win)
    
    input_file.close()
    
    print("Picture completed.")

main()