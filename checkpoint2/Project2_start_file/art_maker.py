"""
 Name: David Martinez Rodriguez
 Assignment: Programming Project 2
 
 Description: This program reads a text file with an art extension and draws
              the "pointillistic" version of an image from the data in the file.
              The largest dimension is specified and the smaller dimension set
              proportionally.   
     
 Document Assistance: (who and what  OR  declare that you gave or received no assistance):
"""

from graphics2 import *
import random
import sys
import tkinter as tk
from tkinter import filedialog

MOSAIC_TILE_SIZE=10

def main():
    #allows you to choose a file 
    root = tk.Tk()
    root.withdraw()
    filenameWithPath = filedialog.askopenfilename()
    #filenameWithPath = 'gallery/bird_184.gif' # use this code if the file chooser doesn't work on your computer

    #add you code here
    if not '.gif' in filenameWithPath:
        print(f"Invalid file format. Must choose a 'gif' file. \nEnding execution.")
        exit(-1)      
    newfile = filenameWithPath[:-4] + ".art"
    
    background_color = int(input("Color for background? (1 white, 2 black) "))
    if background_color == 1:
        background_color = "white"
    elif background_color == 2:
        background_color = "black"
    else:
        print("Invalid color choice. Using black.")
        background_color = "black"

    window = GraphWin("Art Maker", 800, 800)
    window.setBackground(background_color)
main()