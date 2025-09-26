"""
David Martinez Rodriguez
CSC 201
Project 1

This first project allows us to calculate statistics and performance 
of a team in a league across different games.

### I gave and received no assistance on this project. ###
ternary operations used in the project:
https://www.geeksforgeeks.org/python/one-liner-for-python-if-elif-else-statements/
"""


def main():
    print("#### Welcome to Sports League Match Tracker System ####\n")
    
    team = input("Enter a sports team name: ")
    games = int(input(f'How many games did ### {team} ### play? '))
    wins, totalWeighted = 0, 0.0
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
        if winFlag == 1:
            print(f'\nWin! Point difference = {pointDifference} with a weighted score of {weightedScore}')
        elif winFlag == 0:
            print(f'\nLoss! Point difference = {pointDifference} with a weighted score of {weightedScore}')
        elif winFlag == 0.5:
            print(f'\nTie! Point difference = {pointDifference} with a weighted score of {weightedScore}')
    print(f'\n#### OVERALL STATISTICS ####\nTotal wins={wins}, Win Percentage={round(wins/games, 3)}, Average weighted score per game={round(totalWeighted/games, 3)}')
main()