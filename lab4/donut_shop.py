"""
Name(s): David Martinez, Cole Clark
CSC 201
Lab 4--donut_shop.py

When completed, the user will click in the window 3 times
to draw 3 donuts (with sprinkles if you got to the bonus!).

Did you complete this lab file during the class period (yes or no)?
yes 

"""

from graphics2 import *
import random
import math

COLOR_LIST = ['red','blue','lime','black', 'magenta', 'darkviolet', 'deeppink3', 'dodgerblue1', 'firebrick2']
NUM_SPRINKLES = 150
SPRINKLE_RADIUS = 3
HOLE_RATIO = 1/3

def drawOneDonut(window, glazeColor, backgroundColor, radius, center):
    """
    The function draws one donut with color, size, and placement given by the parameters.
   
    Parameters:
    window (GraphWin): the window to draw the donut in
    glazeColor (str): a string for the color of the donut
    backgroundColor (str): a string for the color of the background used to draw the hole
    radius (int): the outer radius of the donut
    center (Point): the center point of the donut
    """
    pass
    outerCircle = Circle(center, radius)
    outerCircle.draw(window)
    outerCircle.setFill(glazeColor)
    outerCircle.setOutline(backgroundColor)
    innerCircle = Circle(center, radius/3)
    innerCircle.draw(window)
    innerCircle.setFill(backgroundColor)
    innerCircle.setOutline(backgroundColor)

def drawSprinkles(window, donut):
    """
    The function draws sprinkles(circles) with a randomly chosen color and position
    so that all are draw on the donut's surface.
   
    Parameters:
    window (GraphWin): the window to draw the sprinkles in
    donut (Circle): the large circle making the donut
    """
    pass



def main():
    # create window
    window = GraphWin("Donut Shop", 500, 500)
    window.setBackground('cyan')
    directions = Text(Point(250, 30), "Click three times to get your donuts!")
    directions.draw(window)
    click1 = window.getMouse()
    donutOneCenter = click1
    drawOneDonut(window, 'pink', 'cyan', 100, click1)
    click2 = window.getMouse()
    donutTwoCenter = click2
    drawOneDonut(window, 'yellow', 'cyan', 75, donutTwoCenter)
    click3 = window.getMouse()
    donutThreeCenter = click3
    drawOneDonut(window, 'brown', 'cyan', 85, donutThreeCenter)
   

    # draw donuts in window

   

main()

   