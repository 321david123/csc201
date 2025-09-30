"""
Name(s): David Martinez
CSC 201
Lab 3

This program draws polygons in a window from a file. 

Did you complete this lab file during the class period (yes or no)?
no 
If no, leave the one that applies. If yes, delete this entire section!
    ##I completed file_polygons.py without my partner from class.##

    Document any assistance you get if you complete the lab after the class period:
    none


"""
from graphics2 import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
BORDER = 10

def main():
    # Enter file name and open to read
    filename = input("Enter the name of the file: ")
    file = open(filename, 'r')

    # Create window where polygons will be drawn
    window = GraphWin("File Polygons", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground('white')

    lines = file.readlines()
    for line in lines:
        data = line.split()
        if len(data) > 0:
            red = int(data[0])
            green = int(data[1])
            blue = int(data[2])
            color = color_rgb(red, green, blue)
            
            vertexList = []
            
            for i in range(3, len(data), 2): 
                x = int(data[i])
                y = int(data[i + 1])
                
                if x < BORDER:
                    x = BORDER
                elif x > WINDOW_WIDTH - BORDER:
                    x = WINDOW_WIDTH - BORDER
                    
                if y < BORDER:
                    y = BORDER
                elif y > WINDOW_HEIGHT - BORDER:
                    y = WINDOW_HEIGHT - BORDER
                vertex = Point(x, y)
                vertexList.append(vertex)
            if len(vertexList) >= 3: 
                polygon = Polygon(vertexList)
                polygon.setFill(color)
                polygon.draw(window)
    file.close()
    window.getMouse()
    window.close()

main()