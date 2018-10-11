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
    num_players = validateInput(num_players, 10, minimum=1)

    print()

    # initializes players array with Player objects
    for player_num in range(1, num_players + 1):
        name = input('Player {} name: '.format(player_num))
        players.append(Player(name))
    os.system('clear')
    run(players)


def run(players):
    '''calls the function for each discipline in order, updates the total
    score between each call, then shows the winner at the end'''

    scoring.updateTotals(players)
    one_attempt(players, '100 Metres', min_score=0, max_score=40)
    three_attempts(players, 'Long Jump', min_score=0, max_score=30)
    three_attempts(players, 'Shot Put', min_score=0, max_score=40)
    heights(players, 'High Jump', min_height=10, max_height=30)
    one_attempt(players, '400 Metres', min_score=0, max_score=40)
    one_attempt(players, '110 Metre Hurdles', min_score=5, max_score=30)
    three_attempts(players, 'Discus', min_score=10, max_score=30)
    heights(players, 'Pole-Vault', min_height=10, max_height=48)
    three_attempts(players, 'Javelin', min_score=0, max_score=30)
    one_attempt(players, '1500 Metres', min_score=8, max_score=40)

    # end of game upkeep / stats
    os.system('clear')
    scoring.updateScoresFile(players)
    scoring.updateHighScoresFile(players)
    scoring.updateTotals(players)
    scoring.displayHighScores()


def validateInput(text, maximum, minimum=0, invalid=False):
    '''validates input to make sure input is not text, or is within
    the valid range, and returns the validated input'''

    if text.isdigit():
        if (invalid and int(text) == 0) or (minimum <= int(text) <= maximum):
            return int(text)

    text = input(
        'Please enter a number from {} - {}: '.format(minimum, maximum))

    return validateInput(text, maximum, minimum, invalid)


if __name__ == "__main__":
    init()
