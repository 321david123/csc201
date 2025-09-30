"""
Name(s): David Martinez
CSC 201
Lab 3

This program draws polygons in a window from a file. 

Did you complete this lab file during the class period (yes or no)?
no 
If no, leave the one that applies. If yes, delete this entire section!
    I completed file_polygons.py without my partner from class.

    Document any assistance you get if you complete the lab after the class period:


"""
from graphics2 import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BORDER = 30


def main():
    # Enter file name and open to read
    filename = input("Enter the name of the file: ")
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        # Try looking in the Lab3 2 directory if file not found in current directory
        try:
            file = open("Lab3 2/" + filename, 'r')
        except FileNotFoundError:
            print(f"Error: Could not find file '{filename}' in current directory or Lab3 2 folder")
            return
    
    # Create window where polygons will be drawn
    window = GraphWin("File Polygons", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground('white')
    
    # Read and process each line of the file
    for line in file:
        # Split the line into a list of strings
        data = line.split()
        
        # Skip empty lines
        if len(data) == 0:
            continue
        
        # Get color components (first three values)
        red = int(data[0])
        green = int(data[1])
        blue = int(data[2])
        color = color_rgb(red, green, blue)
        
        # Initialize vertex list
        vertexList = []
        
        # Loop through remaining data (coordinates) starting from index 3
        for i in range(3, len(data), 2):  # step by 2 to get x,y pairs
            x = int(data[i])
            y = int(data[i + 1])
            
            # Check boundaries and adjust if necessary
            if x < BORDER:
                x = BORDER
            elif x > WINDOW_WIDTH - BORDER:
                x = WINDOW_WIDTH - BORDER
                
            if y < BORDER:
                y = BORDER
            elif y > WINDOW_HEIGHT - BORDER:
                y = WINDOW_HEIGHT - BORDER
            
            # Create vertex and add to list
            vertex = Point(x, y)
            vertexList.append(vertex)
        
        # Create polygon, set color, and draw
        if len(vertexList) >= 3:  # Need at least 3 vertices for a polygon
            polygon = Polygon(vertexList)
            polygon.setFill(color)
            polygon.draw(window)
    
    # Close file
    file.close()
    
    # Wait for click to close window
    window.getMouse()
    window.close()

      
main()