class Player:
    '''Stores the name, scores, and total score for each player'''

    def __init__(self, name):
        self.name = name
        self.total = 0
        self.scores = {
            '100 Metres': 0,
            'Long Jump': 0,
            'Shot Put': 0,
            'High Jump': 0,
            '400 Metres': 0,
            '110 Metre Hurdles': 0,
            'Discus': 0,
            'Pole-Vault': 0,
            'Javelin': 0,
            '1500 Metres': 0
            }

    def update_total(self):
        self.total = sum(self.scores.values())
