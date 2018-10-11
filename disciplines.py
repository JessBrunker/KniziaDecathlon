from player import Player
from discipline_descriptions import print_description
from scoring import print_scores, updateTotals
import decathlon

import os


def validateYesOrNo(text):
    '''gets either a y or n for heights function'''
    while not text or text not in ['y', 'n']:
        text = input('Please enter either y or n: ')
    return text


def heights(players, discipline, min_height, max_height):
    '''Players roll to reach an increasing value, starting at min_height,
    and maxing out at max_height'''

    print_description(discipline)

    stopped_count = 0  # number of players who have faulted
    scores = [{'failed': False, 'height': 0} for player in players]

    # loops through all heights
    for height in range(min_height, max_height+1, 2):
        print('Current height: {}'.format(height))
        # loops through players
        for id, player in enumerate(players):
            # player failed
            if scores[id]['failed']:
                continue

            try_it = input('{} - attempt? y/n: '.format(player.name))
            try_it = validateYesOrNo(try_it)
            if try_it == 'y':
                success = input('Did you succeed? y/n: ')
                success = validateYesOrNo(success)
                if success == 'n':
                    scores[id]['failed'] = True
                    stopped_count += 1
                else:
                    scores[id]['height'] = height
            print()

        # all players failed
        if stopped_count == len(players):
            break

        # for showing the currently mastered heights
        os.system('clear')
        print_scores(players)
        print_description(discipline)
        print('Mastered heights:')
        for id, player in enumerate(players):
            if scores[id]['failed']:  # only shows if player failed
                still_going = ' - FAILED'
            else:
                still_going = ''
            print('{}: {}{}'.format(
                    player.name, scores[id]['height'], still_going))
        print('\n')

    # update scores in players dict
    for id, player in enumerate(players):
        player.scores[discipline] = scores[id]['height']
    os.system('clear')

    updateTotals(players)


def one_attempt(players, discipline, min_score, max_score):
    '''Players get one attempt at the discipline. Possible scores are
    min_score <= score <= max_score'''

    print_description(discipline)

    for player in players:
        score = input('Score for {}: '.format(player.name))
        score = decathlon.validateInput(score,
                                        minimum=min_score,
                                        maximum=max_score)
        player.scores[discipline] = score
    os.system('clear')

    updateTotals(players)


def three_attempts(players, discipline, min_score, max_score):
    '''Players have three attempts to get the highest score possible.
    Scores range from min_score <= score <= max_score'''

    print_description(discipline)

    for player in players:
        print('\n{} attempts'.format(player.name))
        best_score = 0

        for attempt in range(1, 4):
            score = input('Attempt {}: '.format(attempt))
            score = decathlon.validateInput(score, minimum=min_score,
                                            maximum=max_score, invalid=True)
            best_score = max(best_score, score)
        player.scores[discipline] = best_score

        print()
    os.system('clear')

    updateTotals(players)
