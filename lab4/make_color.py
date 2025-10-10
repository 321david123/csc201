"""
Name(s): David Martinez, Cole Clark
CSC 201
Lab 4--make_color.py

Enter red, green, and blue components to mix a color,
then fill the rectangle with that color

Did you complete this lab file during the class period (yes or no)?
yes
"""
from graphics2 import *

def main():
    #create window and show directions
    window = GraphWin("What's the color?", 600, 600)
    window.setBackground('white')
    directions = Text(Point(300, 30), "Enter the amounts of red, green, and blue.")
    directions.draw(window)
    clickDirections = Text(Point(300, 60), "Click mouse when done.")
    clickDirections.draw(window)
   
    #draw the rectangle
    colorRect = Rectangle(Point(100, 250), Point(500, 550))
    colorRect.draw(window)
   
    #setup red label and entry box for input
    redLabel = Text(Point(100, 150), "red")
    redLabel.draw(window)
    inputRed = Entry(Point(150, 150), 5)
    inputRed.setTextColor('red')
    inputRed.draw(window)

    #setup green label and entry box for input
    greenLabel = Text(Point(250, 150), "green")
    greenLabel.draw(window)
    inputGreen = Entry(Point(300, 150), 5)
    inputGreen.setTextColor('green')
    inputGreen.draw(window)

   
   
    #setup blue label and entry box for input
   
    blueLabel = Text(Point(400, 150), "blue")
    blueLabel.draw(window)
    inputBlue = Entry(Point(450, 150), 5)
    inputBlue.setTextColor('blue')
    inputBlue.draw(window)
   
    window.getMouse()


    #get numbers from entry boxes to mix the color
    colorGreen = int(inputGreen.getText())
    colorBlue = int(inputBlue.getText())
    colorRed = int(inputRed.getText())


 
 
   
   
    # make color from red, green, blue numbers

   
    rgb = color_rgb(colorRed, colorGreen, colorBlue)
   
    # add the color to the rectangle that is already drawn

    colorRect.setFill(rgb)
   



   
main()
