# Poetkoe's version of ratkaisin for hirsipuutin

print('Poetkoe :D')

# reset the test output file
f = open('testi.txt', 'w')
f.write('')
f.close()

# SETUP PHASE ##################################################################
words = []

word = input().strip()
while word:
    words.append(word)
    word = input().strip()

temp_words = []
for word in words:
    temp_words.append(word)

letters = {letter for word in words for letter in word} #set
frequencies = [(letter, sum(word.count(letter) for word in words)) for letter in letters] #list
guess_order = sorted(frequencies, key=lambda a: a[1], reverse=True) #list

unique_letters = []

for word in temp_words:
    for letter in word:
        if letter not in unique_letters:
            unique_letters.append(letter)


fil = open('letters.txt', 'a')
for o in guess_order:
    fil.write(o + '\n')
fil.close()

################################################################################

results = []

# removes all the words that don't have correct letters ########################
def remove_wrong_words_on_correct_letter(correct_letter, temp_words):
    #wrong_letters.append(letter)
    remaining_words = []

    for word in temp_words:
        if correct_letter in word:
            remaining_words.append(word)

    temp_words = remaining_words

    unique_letters.remove(correct_letter)


# removes all the words that don't have correct letters ########################
def remove_wrong_words_on_wrong_letter(wrong_letter, temp_words):
    #wrong_letters.append(letter)
    remaining_words = []

    for word in temp_words:
        if wrong_letter not in word:
            remaining_words.append(word)

    temp_words = remaining_words

    unique_letters.remove(wrong_letter)


# update the letter frequencies based on the new possible words ################
def count_new_frequencies():
    frequencies = [(letter, sum(word.count(letter) for word in words)) for letter in letters]
    guess_order = sorted(frequencies, key=lambda a: a[1], reverse=True)


# remove all words of wrong length #############################################
def remove_words_of_wrong_length(temp_words, word_length):
    remaining_words = []

    for word in temp_words:
        if len(word) == word_length:
            remaining_words.append(word)

    temp_words = remaining_words


# THIS IS WHERE THE PLAYING HAPPENS ############################################
try:
    status = input()

    #remove all words of wrong length
    word_length = len(status)
    remove_words_of_wrong_length(temp_words, word_length)

    while status:
        # this loop does the original game logic
        for letter, frequency in guess_order:
            print(letter)
            result = input() # this is the score row

            previous_status = status

            #print(result)
            #results.append(result)
            # trying this to check if the letter was included
            #if status == result:
            #    print('ei osunu :D')
            #    remove_wrong_words(letter)
            #    count_new_frequencies()

            status = input() # this is the status of the word with hidden and exposed letters

            # compare status to previous_status to find out if the letter guessed is or isn't in the word
            if status == previous_status:
                f = open('testi.txt', 'a')
                f.write('NYTTON SAMAT :D\n')
                f.close()
                remove_wrong_words_on_wrong_letter(letter, temp_words)
            else:
                remove_wrong_words_on_correct_letter(letter, temp_words)

            count_new_frequencies()


            if status.startswith('WIN') or status.startswith('LOSE') or not status:
                break

            f = open('testi.txt', 'a')
            f.write('_________status: ' + status + '\n' + 'previous_status: ' + previous_status + '\n\n')
            f.close()

except EOFError:
    pass

################################################################################


'''
Eli:
Testataan järjestyksessä yleisimpiä kirjaimia, mutta jos kirjainta
ei löydy, eliminoidaan kaikki sanat, joissa se kirjain olisi
    => yleisimpien kirjainten lista päivittyy (ei oteta mukaan jo arvattuja kirjaimia tietenkään)
    => jatketaan uuden yleisimpien kirjainten listan läpikäyntiä
'''
