# Simple hangman solver, guesses letters in order of frequency

print('anttispitkanen')

words = []
temp_words = []

word = input().strip()
while word:
    words.append(word)
    word = input().strip()

for word in words:
    temp_words.append(word)

letters = {letter for word in words for letter in word}
frequencies = [(letter, sum(word.count(letter) for word in words)) for letter in letters]
guess_order = sorted(frequencies, key=lambda a: a[1], reverse=True)

lett = open('letters.txt', 'w')
lett.write(str(guess_order) + '\n')
lett.close()


def remove_words_of_wrong_length(corr_length):
    remaining_words = []
    for word in words:
        if len(word) == corr_length:
            remaining_words.append(word)

    return remaining_words


def readjust(new_set_of_words):
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


# GAMEPLAY #####################################################################
try:
    status = input()
    word_length = len(status)

    while status:

        temp_words = remove_words_of_wrong_length(word_length)
        guess_order = readjust(temp_words)
        used_letters = []

        sp = open('sanapituus.txt', 'w')
        sp.write('olen päätellyt että sanan pituus on ' + str(word_length) + ' eli mahdollisia ovat:\n')
        for word in temp_words:
            sp.write(word + '\n')
        sp.close()

        lett = open('letters.txt', 'a')
        lett.write(str(guess_order) + '\n')
        lett.close()


        while True:
            most_common_letter = find_most_common_letter(guess_order, used_letters)
            used_letters.append(most_common_letter)
            print(most_common_letter)

            result = input()

            previous_status = status
            status = input()

#            if previous_status == status:
#                #update based on a wrong letter
#                continue
#            else:
#                #update based on a correct letter
#                continue

        #for letter, frequency in guess_order:
        #    print(letter)
        #    result = input()
        #    status = input()
#            if status.startswith('WIN') or status.startswith('LOSE') or not status:
#                break

            if status.startswith('WIN') or status.startswith('LOSE') or not status:
                used_letters = []
                status = input()
                word_length = len(status)

                break

            #guess_order = readjust(temp_words)

except EOFError:
    pass
