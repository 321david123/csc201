"""
Name: David Martinez
CSC 201
Lab 3

This program makes random polygons in a window.

Did you complete this lab file during the class period (yes or no)?
no 
If no, leave the one that applies. If yes, delete this entire section!
    ##I completed random_polygons.py without my partner from class.##
    
    Document any assistance you get if you complete the lab after the class period:
    none 


"""
from graphics2 import *
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BORDER = 10

def main():
    # Prompt user for shape type
    shape_choice = input("Should I draw triangles(T) or quads(Q)? ")
    
    # Determine number of sides based on user choice
    if shape_choice.upper() == 'T':
        numSides = 3
    else:  # Assume 'Q' or 'q'
        numSides = 4
    
    # Prompt for number of shapes to draw
    num_shapes = int(input("How many should I draw? "))
    
    # Create window
    window = GraphWin('Random Polygons', WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground('white')
    
    # Draw the specified number of shapes
    for shape_count in range(num_shapes):
        # Create list of vertices
        vertexList = []
        for count in range(numSides):  # loop to get enough Points
            x = random.randrange(BORDER, WINDOW_WIDTH - BORDER)
            y = random.randrange(BORDER, WINDOW_HEIGHT - BORDER)
            vertex = Point(x, y)
            vertexList.append(vertex)
        
        # Create polygon
        polygon = Polygon(vertexList)
        
        # Generate random color
        redNum = random.randrange(0, 256)
        greenNum = random.randrange(0, 256)
        blueNum = random.randrange(0, 256)
        color = color_rgb(redNum, greenNum, blueNum)
        
        # Set color and draw
        polygon.setFill(color)
        polygon.draw(window)
    
    # Wait for click to close
    window.getMouse()
    window.close()

main()