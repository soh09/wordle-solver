# from nltk.corpus import words
import enchant

d = enchant.Dict('en_US')

def solve_wordle(current):
    """
    Takes in current, a string representing the current status of the wordle.
    Unknown letters will be substitued with '_'. Returns a list of strings
    that are possible solutions.
    """

    possible_letters = []
    letter_combinations = []
    word_combinations = []
    possible_words = []
    missing = 0
    current = current.lower()
    

    for i in range(len(current)):
        if current[i] == '_':
            missing += 1
            possible_letters.append(
                input(
                    'Possible letters for the ' + str(i + 1) + 'th letter: '
                )
            )
    
    if missing == 1:
        letter_combinations = list(possible_letters[0])
        word_combinations = [current.replace('_', letters) \
            for letters in letter_combinations]

    else:
        if missing == 2:
            letter_combinations = [first + second \
                for first in list(possible_letters[0]) \
                    for second in list(possible_letters[1])]
        elif missing == 3:
            letter_combinations = [first + second + third \
                for first in list(possible_letters[0]) \
                    for second in list(possible_letters[1]) \
                        for third in list(possible_letters[2])]
        elif missing == 4:
            letter_combinations = [first + second + third + fourth\
                for first in list(possible_letters[0]) \
                    for second in list(possible_letters[1]) \
                        for third in list(possible_letters[2]) \
                            for fourth in list(possible_letters[3])]

        for comb in letter_combinations:
            word_combination = ""
            for char in current:
                if char != "_":
                    word_combination += char
                else:
                    word_combination += comb[0]
                    comb = comb[1:]

            word_combinations.append(word_combination)


    for word in word_combinations:
        if d.check(word):
            possible_words.append(word)


    return possible_words if len(possible_words) != 0 else 'No matches'
