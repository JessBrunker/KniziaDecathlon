#!/usr/bin/python3


import os

from disciplines import *
from player import Player
import scoring


def init():
    '''initializes the array that holds the information about the players'''
    os.system('clear')
    players = []

    print('Welcome to Reiner Knizia\'s Decathlon!\n')

    num_players = input('How many players? ')
    while not validateInput(num_players, 10, minimum=1):
        num_players = input('Please enter a number greater than 1: ')
    num_players = int(num_players)

    print()

    # initializes players array with Player objects
    for player_num in range(num_players):
        name = input('Player {} name: '.format(player_num + 1))
        players.append(Player(name))
    os.system('clear')
    run(players)


def run(players):
    '''calls the function for each discipline in order, updates the total
    score between each call, then shows the winner at the end'''
    
    scoring.updateTotals(players)
    d100Metres(players)
    scoring.updateTotals(players)
    dLongJump(players)
    scoring.updateTotals(players)
    dShotPut(players)
    scoring.updateTotals(players)
    dHighJump(players)
    scoring.updateTotals(players)
    d400Metres(players)
    scoring.updateTotals(players)
    d110MetreHurdles(players)
    scoring.updateTotals(players)
    dDiscus(players)
    scoring.updateTotals(players)
    dPoleVault(players)
    scoring.updateTotals(players)
    dJavelin(players)
    scoring.updateTotals(players)
    d1500Metres(players)
    scoring.updateTotals(players)

    # end of game upkeep / stats
    os.system('clear')
    scoring.updateScoresFile(players)
    scoring.updateHighScoresFile(players)
    scoring.updateTotals(players)
    scoring.displayHighScores()


def validateInput(text, maximum, minimum=0, invalid=False):
    '''validates input to make sure input is not text, or is within
    the valid range'''
    if not text.isdigit():
        return False
    if invalid and int(text) == 0:  # allows zero regardless of max/min
        return True
    return minimum <= int(text) <= maximum


if __name__ == "__main__":
    init()
