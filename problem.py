"""
Name(s): Lab 7 Solution
CSC 201
Lab7

This file implements the QuizProblem class which creates randomly generated
arithmetic problems with whole number answers for use in a quiz application.

Lab completed with AI assistance.
"""

import random

class QuizProblem:
    
    OPERATION_LIST = ['+', '-', '*', '/']
    
    """
    This class represents one (randomly generated) problem for
     use in a simple arithmetic quiz.
    Each problem must be generated so that the answers are always
    positive whole numbers (ie. 0, 1, 2, 3, ...)
    
    instance variables:
    operand1 (int): number to the left of the operation symbol
    operand2 (int): number to the right of the operation symbol
    answer (int): the answer to the quiz problem
    operation (str): the symbol for the operation ('+','-','*', '/')
    """
    
    def __init__(self, maxRandom):
        """
        Constructor that creates a random arithmetic problem.
        
        Params:
            maxRandom (int): the largest allowable integer for generating random numbers
        """
        # Choose a random operation
        self.operation = random.choice(QuizProblem.OPERATION_LIST)
        
        # Call the appropriate helper method based on the operation
        if self.operation == '+':
            self._randomizeAddition(maxRandom)
        elif self.operation == '-':
            self._randomizeSubtraction(maxRandom)
        elif self.operation == '*':
            self._randomizeMultiplication(maxRandom)
        elif self.operation == '/':
            self._randomizeDivision(maxRandom)
    
    def _randomizeAddition(self, maxRandom):
        """
        Private helper method to generate random addition problem.
        
        Params:
            maxRandom (int): the largest allowable integer for generating random numbers
        """
        self.operand1 = random.randint(0, maxRandom)
        self.operand2 = random.randint(0, maxRandom)
        self.answer = self.operand1 + self.operand2
    
    def _randomizeSubtraction(self, maxRandom):
        """
        Private helper method to generate random subtraction problem.
        Ensures answer is non-negative by working backwards.
        
        Params:
            maxRandom (int): the largest allowable integer for generating random numbers
        """
        self.operand2 = random.randint(0, maxRandom)
        self.answer = random.randint(0, maxRandom)
        self.operand1 = self.answer + self.operand2
    
    def _randomizeMultiplication(self, maxRandom):
        """
        Private helper method to generate random multiplication problem.
        
        Params:
            maxRandom (int): the largest allowable integer for generating random numbers
        """
        self.operand1 = random.randint(0, maxRandom)
        self.operand2 = random.randint(0, maxRandom)
        self.answer = self.operand1 * self.operand2
    
    def _randomizeDivision(self, maxRandom):
        """
        Private helper method to generate random division problem.
        Ensures answer is a whole number and divisor is not zero.
        
        Params:
            maxRandom (int): the largest allowable integer for generating random numbers
        """
        self.operand2 = random.randint(1, maxRandom)  # Avoid division by zero
        self.answer = random.randint(0, maxRandom)
        self.operand1 = self.answer * self.operand2
    
    def getAnswer(self):
        """
        Public accessor method that returns the answer to the problem.
        
        Returns:
            int: the answer to the arithmetic problem
        """
        return self.answer
    
    def getQuestionString(self):
        """
        Public accessor method that returns the question without the answer.
        
        Returns:
            str: the question string in format "operand1 operation operand2 ="
        """
        return f"{self.operand1} {self.operation} {self.operand2} ="
    
    def __str__(self):
        """
        Special method that returns a string representation of the full equation.
        
        Returns:
            str: the full equation in format "operand1 operation operand2 = answer"
        """
        return f"{self.operand1} {self.operation} {self.operand2} = {self.answer}"
    



    

    
def main():
    prob1 = QuizProblem(1)
    print('Question: ', prob1.getQuestionString())
    print('Answer: ', prob1.getAnswer())
    print('Equation:', prob1) #printing prob1 calls the prob1.__str__() method implicitly
    print()
    
    for count in range(25):
        prob = QuizProblem(10)
        print(prob)
        
if __name__ == '__main__':
    main()
        