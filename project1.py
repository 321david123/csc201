"""
David Martinez Rodriguez
CSC 201
Project 1

This first project allows us to calculate statistics and performance 
of a team in a league across different games.

### External sources used in the project:
---ternary operations-- https://www.geeksforgeeks.org/python/one-liner-for-python-if-elif-else-statements/
### 
# I gave and received no assistance on this project other than the external sources listed above
"""


def main():
    print("#### Welcome to Sports League Match Tracker System ####\n")
    
    team = input("Enter a sports team name: ")
    games = int(input(f'How many games did ### {team} ### play? '))
    # Declaring variables
    wins, totalWeighted = 0, 0.0
    noViolations, withViolations = 0, 0
    highestScore = -1000
    lowestScore = 1000    
    fewestViolations = 1000  
    bestCity = ""
    worstCity = ""
    bestRuleCity = ""
    
    for i in range(games):
        city = input(f'\nEnter the city where the ## Game {i+1} ## was held: ')
        points = int(input(f'Enter points scored by ## {team} ## in {city}: '))
        allowed = int(input(f'Enter points allowed against ## {team} ## in {city}: '))
        rule = int(input(f'Enter number of rule violations by ## {team} ## in {city}: '))
        winFlag = 1.0 if points > allowed else 0.5 if points == allowed else 0.0
        if points > allowed:
            wins += 1
        pointDifference = points - allowed
        weightedScore = 1.0 * winFlag + 0.5 * pointDifference - 0.1 * rule
        totalWeighted += weightedScore
        
        # Tracking rule violations
        if rule == 0:
            noViolations += 1
        else:
            withViolations += 1
            
        # Conditioanls to track best and worst games
        if weightedScore > highestScore:
            highestScore = weightedScore
            bestCity = city
        if weightedScore < lowestScore:
            lowestScore = weightedScore
            worstCity = city
        if rule < fewestViolations:
            fewestViolations = rule
            bestRuleCity = city
            
        if winFlag == 1:
            print(f'\nWin! Point difference = {pointDifference} with a weighted score of {weightedScore}')
        elif winFlag == 0:
            print(f'\nLoss! Point difference = {pointDifference} with a weighted score of {weightedScore}')
        elif winFlag == 0.5:
            print(f'\nTie! Point difference = {pointDifference} with a weighted score of {weightedScore}')        
        # Printing outcome message based on point difference
        if pointDifference > 20:
            print(f"Dominant win in {city} with a margin of {pointDifference} points!")
        elif pointDifference > 0:
            print(f"Solid win in {city} by {pointDifference} points.")
        else:
            print(f"No win in {city}, :( Better luck next time.")
            
    print(f'\n#### OVERALL STATISTICS ####')
    print(f'Number of games with rule violations: {withViolations}')
    print(f'Number of games with no rule violations: {noViolations}')
    winPercentage = round((wins / games) * 100, 3)
    avgWeighted = round(totalWeighted / games, 3)
    print(f'Total wins={wins}, Win percentage={winPercentage}%, Average weighted score per game={avgWeighted}')
    
    # Print awards if more than one game was played
    if games > 1:
        print(f'\nThe highest weighted score is {round(highestScore, 3)}, achieved in {bestCity}.')
        print(f'The lowest weighted score is {round(lowestScore, 3)}, recorded in {worstCity}.')
        print(f'The fewest rule violations is {int(fewestViolations)}, occurring in {bestRuleCity}.')

main()