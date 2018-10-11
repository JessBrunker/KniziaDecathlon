#!/usr/bin/python3


from player import Player
from discipline_descriptions import print_description
import decathlon

import os


def d100Metres(players):
    print_description('100 Metres')
    for player in players:
        score = input('Score for {}: '.format(player.name))
        while not decathlon.validateInput(score, 40):
            score = input('Please enter a number from 0 - 40: ')
        score = int(score)
        player.scores['100 Metres'] = score
    os.system('clear')


def dLongJump(players):
    print_description('Long Jump')
    for player in players:
        print('\n{} attempts'.format(player.name))
        best_score = 0
        for attempt in range(1, 4):
            score = input('Attempt {}: '.format(attempt))
            while not decathlon.validateInput(score, 30):
                score = input('Please enter a number from 0-30: ')
            score = int(score)
            best_score = max(best_score, score)
        player.scores['Long Jump'] = best_score
        print()
    os.system('clear')


def dShotPut(players):
    print_description('Shot Put')
    for player in players:
        print('\n{} attempts'.format(player.name))
        best_score = 0
        for attempt in range(1, 4):
            score = input('Attempt {}: '.format(attempt))
            while not decathlon.validateInput(
                    score, 40, minimum=8, invalid=True):
                score = input('Please enter a valid number from 0-40: ')
            score = int(score)
            best_score = max(best_score, score)
        player.scores['Shot Put'] = best_score
        print()
    os.system('clear')


def dHighJump(players):
    print_description('High Jump')
    stopped_count = 0  # number of players who have faulted
    scores = [{'going': True, 'height': 0} for player in players]
    # loops through all heights
    for height in range(10, 31, 2):
        print('Current height: {}'.format(height))
        # loops through players
        for id, player in enumerate(players):
            # player failed
            if not scores[id]['going']:
                continue
            try_it = input('{} - attempt? y/n '.format(player.name))
            while not try_it or try_it not in ['y', 'n']:
                try_it = input('Please enter either y or n')
            if try_it == 'y':
                success = input('Did you succeed? y/n ')
                while not success or try_it not in ['y', 'n']:
                    success = input('Please enter either y or n')
                if success == 'n':
                    scores[id]['going'] = False
                    stopped_count += 1
                else:
                    scores[id]['height'] = height
        # all players failed
        if stopped_count == len(players):
            break
    # update scores in players dict
    for id, player in enumerate(players):
        player.scores['High Jump'] = scores[id]['height']
    os.system('clear')


def d400Metres(players):
    print_description('400 Metres')
    for player in players:
        score = input('Score for {}: '.format(player.name))
        while not decathlon.validateInput(score, 40, minimum=0):
            score = input('Please enter a valid number from 0 - 40: ')
        score = int(score)
        player.scores['400 Metres'] = score
    os.system('clear')


def d110MetreHurdles(players):
    print_description('110 Metre Hurdles')
    for player in players:
        score = input('Score for {}: '.format(player.name))
        while not decathlon.validateInput(score, 30, minimum=5):
            score = input('Please enter a valid number between 5-30: ')
        score = int(score)
        player.scores['110 Metre Hurdles'] = score
    os.system('clear')


def dDiscus(players):
    print_description('Discus')
    for player in players:
        print('\n{} attempts'.format(player.name))
        best_score = 0
        for attempt in range(1, 4):
            score = input('Attempt {}: '.format(attempt))
            while not decathlon.validateInput(
                    score, 30, minimum=10, invalid=True):
                score = input('Please enter a valid number between 10-30: ')
            score = int(score)
            best_score = max(best_score, score)
        player.scores['Discus'] = best_score
        print()
    os.system('clear')


def dPoleVault(players):
    print_description('Pole Vault')
    stopped_count = 0  # number of players who have faulted
    scores = [{'going': True, 'height': 0} for player in players]
    # loops through all heights
    for height in range(10, 49, 2):
        print('Current height: {}'.format(height))
        # loops through players
        for id, player in enumerate(players):
            # player failed
            if not scores[id]['going']:
                continue
            try_it = input('{} - attempt? y/n '.format(player.name))
            while not try_it or try_it not in ['y', 'n']:
                try_it = input('Please enter either y or n: ')
            if try_it == 'y':
                success = input('Did you succeed? y/n ')
                while not success or success not in ['y', 'n']:
                    success = input('Please enter either y or n: ')
                if success == 'n':
                    scores[id]['going'] = False
                    stopped_count += 1
                else:
                    scores[id]['height'] = height
            print()
        # all players failed
        if stopped_count == len(players):
            break
    # update scores in players dict
    for id, player in enumerate(players):
        player.scores['Pole-Vault'] = scores[id]['height']
    os.system('clear')


def dJavelin(players):
    print_description('Javelin')
    for player in players:
        print('\n{} attempts'.format(player.name))
        best_score = 0
        for attempt in range(1, 4):
            score = input('Attempt {}: '.format(attempt))
            while not decathlon.validateInput(
                    score, 30, minimum=5, invalid=True):
                score = input('Please enter a number from 0-30: ')
            score = int(score)
            best_score = max(best_score, score)
        player.scores['Javelin'] = best_score
        print()
    os.system('clear')


def d1500Metres(players):
    print_description('1500 Metres')
    for player in players:
        score = input('Score for {}: '.format(player.name))
        while not decathlon.validateInput(score, 40, minimum=8):
            score = input('Please enter a valid number from 8-40: ')
        score = int(score)
        player.scores['1500 Metres'] = score
    os.system('clear')
