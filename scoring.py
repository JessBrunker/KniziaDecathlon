from player import Player

import datetime


def updateTotals(players):
    '''updates the total field for each player, then prints out the
    sorted list'''

    for player in players:
        player.update_total()
    print_scores(players)


def print_scores(players):
    '''sorts the players in descending order based on total, then prints
    the ranking, name, and total for each player'''

    score_list = sorted(players,
                        key=lambda player: player.total,
                        reverse=True)
    print('Scores')
    for place, player in enumerate(score_list):
        print('{}: {} - {}'.format(place + 1, player.name, player.total))


def updateScoresFile(players):
    '''creates a new comma-separated line in scores.txt for every score
    from the game'''

    now = datetime.datetime.now()

    with open('scores.txt', 'a') as file:
        for player in players:
            line = '\n{}/{}/{},{}'.format(
                now.month, now.day, now.year, player.name)
            scores = '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}'.format(
                player.scores['100 Metres'],
                player.scores['Long Jump'],
                player.scores['Shot Put'],
                player.scores['High Jump'],
                player.scores['400 Metres'],
                player.scores['110 Metre Hurdles'],
                player.scores['Discus'],
                player.scores['Pole-Vault'],
                player.scores['Javelin'],
                player.scores['1500 Metres'])
            line = line + ',' + scores
            file.write(line)


def updateHighScoresFile(players):
    '''compares the highest scores in each discipline and total scores for
    this play against the overall high scores. any new values higher than
    the ones in the file replace the old.'''

    high_scores = {
        '100 Metres': {'Score': 0, 'Name': ''},
        'Long Jump': {'Score': 0, 'Name': ''},
        'Shot Put': {'Score': 0, 'Name': ''},
        'High Jump': {'Score': 0, 'Name': ''},
        '400 Metres': {'Score': 0, 'Name': ''},
        '110 Metre Hurdles': {'Score': 0, 'Name': ''},
        'Discus': {'Score': 0, 'Name': ''},
        'Pole-Vault': {'Score': 0, 'Name': ''},
        'Javelin': {'Score': 0, 'Name': ''},
        '1500 Metres': {'Score': 0, 'Name': ''},
        'Total': {'Score': 0, 'Name': ''}}

    # finds the highest score in each discipline from this play,
    # then saves the score and the player's name to high_scores
    for player in players:
        for discipline, score in player.scores.items():
            if score > high_scores[discipline]['Score']:
                high_scores[discipline]['Score'] = score
                high_scores[discipline]['Name'] = player.name
        if player.total > high_scores['Total']['Score']:
            high_scores['Total']['Score'] = player.total
            high_scores['Total']['Name'] = player.name

    f = open('highscores.txt', 'r')
    filedata = f.read()
    f.close()

    new_info = []
    now = datetime.datetime.now()

    for line in filedata.split('\n'):
        # protects against blank lines
        if not line.strip():
            continue

        discipline, _, score, _ = line.split(',')

        if high_scores[discipline]['Score'] > int(score):
            new_info.append('{},{},{},{}'.format(
                discipline,
                high_scores[discipline]['Name'],
                high_scores[discipline]['Score'],
                '{}/{}/{}'.format(now.month, now.day, now.year)))
        else:
            new_info.append(line)

    with open('highscores.txt', 'w') as file:
        for line in new_info:
            file.write(str(line))
            file.write('\n')


def displayHighScores():
    '''open highscores.txt, display all high scores'''

    print('\n\nHigh Scores')

    with open('highscores.txt', 'r') as file:
        for line in file:
            if not line.strip():
                continue

            discipline, name, score, date = line.strip().split(',')

            print('{}: {} - {} on {}'.format(
                    discipline, name, score, date))
    print()
