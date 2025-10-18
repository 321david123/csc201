"""
Name: David Martinez Rodriguez
CSC 201
Programming Project 2

Description: This program converts a GIF image into a text file format (.art)
             that describes colored squares which form a mosaic version of the image.

Assistance:
I gave and received no assistance on this project.
"""

from graphics2 import *
import random
import sys
import tkinter as tk
from tkinter import filedialog

MOSAIC_TILE_SIZE = 10

def main():
    #allows you to choose a file 
    root = tk.Tk()
    root.withdraw()
    filenameWithPath = filedialog.askopenfilename()
    #filenameWithPath = 'gallery/bird_184.gif' # use this code if the file chooser doesn't work on your computer

    #add you code here
    if filenameWithPath[-4:] != '.gif':
        print("Invalid file format. Must choose a 'gif' file.")
        print("Ending execution.")
        exit(-1)
    
    output_filename = filenameWithPath[:-4] + ".art"
    
    background_color = int(input("Color for background? (1 white, 2 black) "))
    if background_color != 1 and background_color != 2:
        print("Invalid color choice. Using black.")
        background_color = 2
    
    img = Image(Point(0, 0), filenameWithPath)
    
    img_width = img.getWidth()
    img_height = img.getHeight()
    
    output_file = open(output_filename, 'w')
    
    output_file.write(str(img_width) + " " + str(img_height) + "\n")
    output_file.write(str(background_color) + "\n")
    
    y = 0
    while y < img_height:
        x = 0
        while x < img_width:
            left = x
            right = x + MOSAIC_TILE_SIZE
            if right > img_width:
                right = img_width
            
            top = y
            bottom = y + MOSAIC_TILE_SIZE
            if bottom > img_height:
                bottom = img_height
            
            random_x = random.randint(left, right - 1)
            random_y = random.randint(top, bottom - 1)
            
            pixel_color = img.getPixel(random_x, random_y)
            red = pixel_color[0]
            green = pixel_color[1]
            blue = pixel_color[2]
            
            square_size = random.randint(7, 13)
            
            line_to_write = str(random_x) + " " + str(random_y) + " " + str(red) + " " + str(green) + " " + str(blue) + " " + str(square_size) + "\n"
            output_file.write(line_to_write)
            
            x = x + MOSAIC_TILE_SIZE
        
        y = y + MOSAIC_TILE_SIZE
    
    output_file.close()
    print("File created: " + output_filename)
    print("Program ending.")

main()