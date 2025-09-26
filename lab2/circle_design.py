"""
Name(s): David Martinez and Ryan Sigale
CSC 201
Lab 2-Circle Designs


Did you complete the lab during the class period (yes or no)? No


    I completed circle_design_with_loops.py with my partner from class (outside of class).

    Document any assistance you get if you complete the lab after the class period: N/A we worked together on this.



When completed this program will draw a stack of
5 circles with radius 50.
"""
from graphics2 import *


def main():
    numCircles = 5
    
    # Create a window to draw the circle design in
    window = GraphWin("Circles", 800, 800)
    window.setBackground('white')
    
    # Circle 1
    radius = 50
    x = 55
    y = 55
    center = Point(55, 55) 
    circle = Circle(center, radius)
    circle.setOutline('red')        
    circle.draw(window)            

    # Circle 2
    radius = 50                     
    x = 55
    y = 155
    center = Point(x, y) 
    circle = Circle(center, radius)
    circle.setOutline('red')        
    circle.draw(window)            

    # Circle 3
    radius = 50                     
    x = 55
    y = 255
    center = Point(x, y) 
    circle = Circle(center, radius)
    circle.setOutline('red')        
    circle.draw(window)            

    # Circle 4
    radius = 50                     
    x = 55
    y = 355
    center = Point(x, y) 
    circle = Circle(center, radius)
    circle.setOutline('red')        
    circle.draw(window)            

    # Circle 5
    radius = 50                     
    x = 55
    y = 455
    center = Point(x, y) 
    circle = Circle(center, radius)
    circle.setOutline('red')        
    circle.draw(window)            

    window.getMouse()  # wait for the mouse to be clicked in the window.
    window.close()     # close the window after the mouse is clicked in the window.


main()