"""
Name(s): Lab 7 Solution
CSC 201
Lab7

This program randomly generates arithmetic problems to quiz a student.
All of the problems use only whole numbers. A progress bar shows the
student's progress when taking the quiz. The number of problems the
student answered correctly and the student's percentage is displayed
when the quiz is completed.

Lab completed with AI assistance. ProgressBar integration added to main()
to show quiz progress.
"""

from problem import QuizProblem
from progress_bar import ProgressBar
from button import Button
import time
from graphics2 import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
NUM_PROBLEMS = 10

def setUp():
    """
    Create the window and gives directions.
    
    Returns:
        window created to use in the quiz
    """
    window = GraphWin("Arthimetic quiz", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground('white')
    directions = Text(Point(WINDOW_WIDTH/2, WINDOW_HEIGHT/4), f"You'll be given {NUM_PROBLEMS} problems.\n\n"
                                                                "Enter the answer in the box and click submit.")
    goOnText = Text(Point(WINDOW_WIDTH/2, 3 *WINDOW_HEIGHT/4), "Click to continue")
    directions.setSize(18)
    directions.draw(window)
    goOnText.draw(window)
    window.getMouse()
    directions.undraw()
    goOnText.undraw()
    return window

def displayProblem(window, problem):
    """
    displays the problem and and entry box for the answer
    
    Params:
        window (GraphWin): window displaying the quiz
        problem (QuizProblem): the problem that will be displayed
    
    Returns:
        the Text object displaying the problem and the Entry object for the answer as a tuple
    """
    questionString = problem.getQuestionString()
    offset = len(questionString) * 5
    problemText = Text(Point(WINDOW_WIDTH/2 - offset, WINDOW_HEIGHT/5), questionString)
    problemText.setSize(18)
    problemText.draw(window)
    answerBox = Entry(Point(WINDOW_WIDTH/2 + offset + 20, WINDOW_HEIGHT/5), 3)
    answerBox.setSize(18)
    answerBox.setText('')
    answerBox.draw(window)
    return (problemText, answerBox)

def getAnswerFromStudent(window, answerBox, submit):
    """
    requires the user to enter a whole number for the answer.
    
    Params:
        window (GraphWin): the window displaying the quiz
        answerBox (Entry): the Entry object which the answer is entered in
        submit (Button): the button clicked to submit an answer
    
    Returns:
        the answer entered in the answer box when it is finally a whole number
    """
    click = window.getMouse()
    while not submit.isClicked(click):
        click = window.getMouse()
    studentAnswer = answerBox.getText()
    while not studentAnswer.isdigit():
        error = Text(Point(WINDOW_WIDTH/2,WINDOW_HEIGHT/2), "Try again")
        error.draw(window)
        time.sleep(1)
        error.undraw()
        answerBox.setText('')
        click = window.getMouse()
        while not submit.isClicked(click):
            click = window.getMouse()
        studentAnswer = answerBox.getText()
    return int(studentAnswer)

def reportResults(window, numCorrect):
    """
    Displays the number of problems answered correctly and the percent correct
    
    Params:
        window (GraphWin): the window displaying the quiz
        numCorrect (int): the number of problems answered correctly.
    """
    reportText = f'{numCorrect} correct out of {NUM_PROBLEMS} problems'
    text = Text(Point(WINDOW_WIDTH/2, WINDOW_HEIGHT/2), reportText)
    text.setSize(24)
    text.draw(window)
    percentText = f'{round(100 *(numCorrect/NUM_PROBLEMS))}%'
    percent = Text(Point(WINDOW_WIDTH/2, 3 * WINDOW_HEIGHT / 4), percentText)
    percent.setSize(24)
    percent.draw(window)
    
    
            
def main():
    #set up the window and the submit button
    window = setUp()
    submit = Button(Point(WINDOW_WIDTH/2, WINDOW_HEIGHT/3), 100, 30, "Submit")
    submit.activate()
    submit.draw(window)

    # Create a ProgressBar object and draw it in the window
    ### write you code here!
    progressBar = ProgressBar(Point(50, WINDOW_HEIGHT - 50), WINDOW_WIDTH - 100, 30, 'green')
    progressBar.draw(window)



    
    # display the quiz problems comparing the user's answer with the correct one
    numberCorrect = 0
    for count in range(NUM_PROBLEMS):
        problem = QuizProblem(10) # new random problem using numbers 0...10
        problemText, answerBox = displayProblem(window, problem)
        
        studentAnswer = getAnswerFromStudent(window, answerBox, submit)
       
        if studentAnswer == problem.getAnswer():
            numberCorrect = numberCorrect + 1 
    
        problemText.undraw()
        answerBox.undraw()
        
        #compute percent completed and update ProgressBar
        ### write you code here!
        percentCompleted = ((count + 1) / NUM_PROBLEMS) * 100
        progressBar.update(window, percentCompleted)




    submit.undraw()
    
    # undraw the ProgressBar
    ### write you code here!
    progressBar.undraw()
  
    
    reportResults(window, numberCorrect)
    
    time.sleep(3)
    window.close()
      
main()