"""
Name(s): David Martinez and Ryan Sigale
CSC 201
Lab 2-Circle Designs with Loops

This program will draw a design using multiple circles. The
number of circles and radius of the circles is entered
by the user.

Did you complete the lab during the class period (yes or no)? No


    I completed circle_design_with_loops.py with my partner from class (outside of class).

    Document any assistance you get if you complete the lab after the class period: N/A we worked together on this.


"""
from graphics2 import *


def main():
    numCircles = int(input('Enter a number: '))
    radius = int(input('Enter the radius: '))
   
    # Create a window to draw the circle design in
    window = GraphWin("Circles", 800, 800)
    window.setBackground('white')
   
    # Loop to draw a stack of circles
    x = 5+radius
    y = 5+radius
    for num in range(numCircles):    # first one
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')        
        circle.draw(window)
        y = y + 2 * radius #how much does the y coordinate need to increase for each circle?  
   
    x= 5+radius
    y= 5+radius
    for num in range(numCircles):# second one 
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')        
        circle.draw(window)
        x = x + 2 * radius
        print(x)
   
    x = x - radius * 2
    print(x)
    y = radius+5
    for num in range(numCircles):# third one
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')        
        circle.draw(window)
        y = y + 2 * radius
       
    y = y - radius * 2
    for num in range(numCircles):# how many circles, use a variable?
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')        
        circle.draw(window)
        x = x - radius*2
        
    x = 5+radius
    y = 5+radius
    for num in range(numCircles):# how many circles, use a variable?
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('blue')        
        circle.draw(window)
        x = x + 2 * radius
        y = y + 2 * radius
    
    x = x - radius * 2
    y = 5 + radius
    for num in range(numCircles):# how many circles, use a variable?
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('blue')        
        circle.draw(window)
        x = x - 2 * radius
        y = y + 2 * radius
    window.getMouse()  # wait for the mouse to be clicked in the window.
    window.close()     # close the window after the mouse is clicked in the window.


main()
