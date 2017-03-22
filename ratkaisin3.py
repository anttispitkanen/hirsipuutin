# Simple hangman solver, guesses letters in order of frequency

import re

print('anttispitkanen')

words = []
temp_words = []

word = input().strip()
while word:
    words.append(word)
    temp_words.append(word)
    word = input().strip()


letters = {letter for word in words for letter in word}
frequencies = [(letter, sum(word.count(letter) for word in words)) for letter in letters]
guess_order = sorted(frequencies, key=lambda a: a[1], reverse=True)


def remove_words_of_wrong_length(corr_length):
    remaining_words = []
    for word in words:
        if len(word) == corr_length:
            remaining_words.append(word)

    return remaining_words


def recount_guess_order(new_set_of_words):
    letters = {letter for word in new_set_of_words for letter in word}
    frequencies = [(letter, sum(word.count(letter) for word in new_set_of_words)) for letter in letters]
    guess_order = sorted(frequencies, key=lambda a: a[1], reverse=True)
    return guess_order


def find_most_common_letter(guess_order, forbidden_letters):
    i = 0
    while True:
        if guess_order[i][0] not in forbidden_letters:
            return guess_order[i][0]
            break
        else:
            i+=1


def filter_words_with_wrong_letter(letter, words):
    new_words = []
    for word in words:
        if letter not in word:
            new_words.append(word)
    return new_words


def match_regex(reg_string, words):
    new_words = []
    for word in words:
        if re.match(reg_string, word):
            new_words.append(word)
    return new_words


def remove_guessed_words(temp_words, guessed_words):
    new_words = []
    for word in temp_words:
        if word not in guessed_words:
            new_words.append(word)
    return new_words



# GAMEPLAY #####################################################################
try:
    status = input()
    word_length = len(status)

    while status:

        temp_words = remove_words_of_wrong_length(word_length)
        guess_order = recount_guess_order(temp_words)
        used_letters = []
        guessed_words = [] #for full words that are guessed already

        while True:
            most_common_letter = find_most_common_letter(guess_order, used_letters)
            #remove possibly guessed full words
            temp_words = remove_guessed_words(temp_words, guessed_words)


            #if there's only one possible word, try that
            if len(temp_words) < 4:
                print(temp_words[0])
                guessed_words.append(temp_words[0]) #add to guessed_words
                result = input()
                status = input()
            else:
                print(most_common_letter)
                used_letters.append(most_common_letter)
                result = input()
                status = input()

                #this shit intended
                if result.startswith('HIT'):
                   #update based on a correct letter
                   temp_words = match_regex(status, temp_words)
                   guess_order = recount_guess_order(temp_words)
                else:
                   #update based on a wrong letter
                   temp_words = filter_words_with_wrong_letter(most_common_letter, temp_words)
                   guess_order = recount_guess_order(temp_words)




            if status.startswith('WIN') or status.startswith('LOSE') or not status:
                used_letters = []
                status = input()
                word_length = len(status)
                break

except EOFError:
    pass
