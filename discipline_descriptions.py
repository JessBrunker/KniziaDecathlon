import textwrap
import re


class DescWrapper(textwrap.TextWrapper):
    '''Wrap TextWrapper to handle multiple paragraphs'''

    def wrap(self, text):
        '''Override TextWrapper to process multiple paragraphs properly'''
        para_edge = re.compile(r'(\n\s*\n)', re.MULTILINE)
        paragraphs = para_edge.split(text)
        wrapped_lines = []
        for para in paragraphs:
            if para.isspace():
                wrapped_lines.append(para[1:-1])
            else:
                wrapped_lines.extend(textwrap.TextWrapper.wrap(self, para))
        return wrapped_lines


wrapper = DescWrapper(width=80)

# descriptions = {discipline_name: discipline_description,...}
descriptions = {
    '100 Metres': '''

--------------------------------------------------------------------------

100 Metres (8 dice, 1 attempt)

Divide the eight dice into two sets of four. Throw the first four dice. If you are not satisfied with the result, pick up all four dice and rethrow them. This can be repeated several times until you freeze the first set. Then throw the other four dice and proceed in the same manner. Try to freeze sets of dice with high values but which contain no sixes.

You have a maximum of seven throws, one initial throw for each set and up to five rethrows which may be divided between the sets as desired.

Scoring: Total the value of the dice for numbers one to five, but subtract any sixes from the result.

--------------------------------------------------------------------------

''',
    'Long Jump': '''

--------------------------------------------------------------------------

Long Jump (5 dice, 3 attempts)

Run-up: Start by throwing all five dice. Then freeze at least one die. If you wish, rethrow all the remaining dice. You may rethrow several times, but after each throw you must freeze at least one more die. Try to freeze many dice with low values. If the total of all frozen dice exceeds 8, you suffer an invalid attempt by stepping over. If you decide to stop throwing with a total of 8 or less on all frozen dice, you then jump.

Jump: Pick up your frozen dice and throw them all. Freeze at least one die and rethrow the remainder. Proceed in this manner until you freeze all dice. Try to freeze dice of high values.

Scoring: Total the value of all frozen dice used in your jump.

Enter "0" for an invalid attempt.

--------------------------------------------------------------------------

''',
    'Shot Put': '''

--------------------------------------------------------------------------

Shot Put (8 dice, 3 attempts)

Throw one die after the other. At any point you can stop. Your attempt must end after all eight dice. If you throw a one you suffer an invalid attempt.

Scoring: Total the value of all thrown dice.

Enter "0" for an invalid attempt.

--------------------------------------------------------------------------

''',
    'High Jump': '''

--------------------------------------------------------------------------

High Jump (5 dice, 3 jumps per height)

Jumping starts at the height of 10 and is increased by increments of 2. At each height you can decide, on your turn, if you try to jump the height or if you skip it. If you go for that height, you have three jumps in which to master it. Take all three attempts before the next player takes his turn. On each jump you throw all five dice. The jump is successful if the total of all dice equals or exceeds the current height. If you have three invalid attempts at one height you have to stop.

Scoring: The maximum height which was successfully mastered.

--------------------------------------------------------------------------

''',
    '400 Metres': '''

--------------------------------------------------------------------------

400 Metres (8 dice, 1 attempt)

Divide the dice into four sets of two. Throw the first two dice. If you are not satisfied with the result, pick up both dice and rethrow them. This can be repeated several times until you freeze the first set. Then proceed with the second, third and fourth sets in the same manner. Try to freeze sets of dice with high values but which contain no sixes.

You have a maximum of nine throws, one inital throws for each set and up to five rethrows which may be divided between the four sets as desired.

Scoring: Total the value of the dice for the numbers one to five, but subtract any sixes from the result.

--------------------------------------------------------------------------

''',
    '110 Metre Hurdles': '''

--------------------------------------------------------------------------

110 Metre Hurdles (5 dice, 1 attempt)

Start by throwing all five dice. If you are not satisfied with the result, pick up all the dice and rethrow them. You are allowed up to five pickups of the dice.

Scoring: Total value of all five dice.

--------------------------------------------------------------------------

''',
    'Discus': '''

--------------------------------------------------------------------------

Discus (5 dice, 3 attempts)

Start by throwing all five dice, then freeze at least one die. If you wish, rethrow all the remaining dice. You may rethrow several times, but after each throw you must freeze at least one more die. Only dice with even values may be frozen. Try to freeze dice with high (even) values.

You can decide to stop throwing and finish your attempt at any time. An attempt ends automatically when all five dice are frozen.

If, after one of your throws, you cannot freeze another die because all the remaining dice show odd numbers, you show an invalid attempt.

Scoring: Total the value of all frozen dice.

Enter "0" for an invalid attempt.

--------------------------------------------------------------------------

''',
    'Pole-Vault': '''

--------------------------------------------------------------------------

Pole-Vault (8 dice, 3 jumps per height)

Jumping starts at the height of 10 and is increased by increments of 2. At each height you can decide, on your turn, if you try to jump the height or if you skip it.

If you decide to go for that height, you have three jumps in which to master it. Take all three attempts before the next player takes his turn. On each jump you decide how many dice you want to use and then throw them. The jump is successful if the total of the dice is equal to or higher than the current height, and if the throw does not show any ones.

If you suffer three invalid jumps at one height you have to stop.

Scoring: The maximum height which was successfully mastered.

--------------------------------------------------------------------------

''',
    'Javelin': '''

--------------------------------------------------------------------------

Javelin (6 dice, 3 attempts)

Start by throwing all six dice. Then freeze at least one die. If you wish, rethrow all the remaining dice. You may rethrow several times, but after each throw you must freeze at least one more die. Only dice with odd values may be frozen. Try to freeze dice with high (odd) values.

You can stop throwing and finish your attempt at any time. An attempt ends automatically when all six dice are frozen.

If, after one of your throws, you cannot freeze another die because all the remaining dice show even numbers, you suffer an invalid attempt.

Scoring: Total the value of all frozen dice.

Enter "0" for an invalid attempt.

--------------------------------------------------------------------------

''',
    '1500 Metres': '''

--------------------------------------------------------------------------

1500 Metres (8 dice, 1 attempt)

Start by throwing the first die. If you are not satisfied with the result, pick up the die and rethrow it. This can be repeated several times until you freeze the first die. Then proceed in the same manner with the other seven dice. Try to freeze dice with high values but no sixes.

You have a maximum of thirteen throws, one initial throw for each die and up to five rethrows which may be divided between the dice as desired.

Scoring: Total the value of the dice, but subtract any sixes from that result.

--------------------------------------------------------------------------

'''}


def print_description(discipline):
    print(wrapper.fill(descriptions[discipline]))
