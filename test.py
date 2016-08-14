import hashlib
import sys
from threading import Thread

anagram = "poultry outwits ants"
m = hashlib.md5()
m.update(anagram)
test_hash = m.hexdigest()
my_dict = {}  # will hold the list of remaining letter combinations

letters = {}
list_letters = []
repeat_list_letters = []
new_wordlist = []

# hold the lengths of words

longest_word = 1
for i in list(anagram):
    if i in letters:
        letters[i] += 1
        repeat_list_letters.append(i)
    elif i != ' ':
        letters[i] = 1
        list_letters.append(i)
        repeat_list_letters.append(i)
repeat_list_letters.sort()
print(repeat_list_letters)

with open('wordlist', 'r') as wl:
    for word in wl:
        word = word.rstrip('\n')
        is_valid = True
        for letter in word:
            if letter == "'":
                is_valid = False
                break
                # pass
            elif letter not in list_letters:
                is_valid = False
                break
            elif letters[letter] < word.count(letter):
                is_valid = False
                break
            elif len(word) > 18:
                is_valid = False
                break
        if new_wordlist == [] and is_valid:
            new_wordlist.append(word)
        elif is_valid and new_wordlist[-1] != word:
            new_wordlist.append(word)
new_wordlist.sort(key=len)  # sorts by descending length
print(len(new_wordlist))

keys = []
def create_keys(letters_list):
    key = ()
    for letter in letters_list:
        key = key + (letter,)
        keys.append(key)


def create_keys_iter(letters_list):
    letters_list_copy = letters_list[:]
    for letter in letters_list:
        create_keys(letters_list_copy)
        letters_list_copy.remove(letter)

create_keys_iter(repeat_list_letters)
print(len(keys))


def is_word_possible(word, possible_letters):
    possible_letters = list(possible_letters)
    for letter in list(word):
        if letter in possible_letters:
            possible_letters.remove(letter)
        else:
            return False
    return True


def iter_dictionary(word_list, key):
    my_dict[key] = []
    for word in word_list:
        if len(word) > len(key):
            break
        elif is_word_possible(word, key):
            my_dict[key].insert(0, word)
            # my_dict[key].append(word)


def iter_keys(word_list, keys):
    for key in keys:
        iter_dictionary(word_list, key)

iter_keys(new_wordlist, keys)


def anagram_it(letters_remaining, phrase=()):
    length = len(letters_remaining)  # end loop if more letters in word than in list
    key = tuple(letters_remaining)
    try:
        words = my_dict[key]
    except KeyError:
        iter_dictionary(new_wordlist, key)
        words = my_dict[key]
    for word in words:
        if len(word) > length:
            break
        else:
            word_as_list = list(word)
            letter_absent = any(True for x in word_as_list if x not in letters_remaining)
            if not letter_absent:
                multiletter_out_of_bounds = False
                letters_remaining_copy = list(key)
                for i in word_as_list:
                    try:
                        letters_remaining_copy.remove(i)
                    except ValueError:
                        multiletter_out_of_bounds = True

                if not multiletter_out_of_bounds:
                    phrase = phrase + (word,)
                    if letters_remaining_copy == []:
                        new_string = " ".join(phrase)
                        m.update(new_string)
                        if m.hexdigest() == test_hash:
                            printSuccess(new_string)
                        elif m.hexdigest() == "4624d200580677270a54ccff86b9610e":
                            printSuccess(new_string)
                            sys.exit(0)
                        phrase = phrase[:-1]
                    else:
                        anagram_it(letters_remaining_copy, phrase)
                        phrase = phrase[:-1]



def printSuccess(phrase):
    print('####################################')
    print('####################################')
    print('####################################')
    print('####################################')
    print('WOW')
    print(phrase)
    print('WOW')
    print('####################################')
    print('####################################')
    print('####################################')
    print('####################################')



for word in new_wordlist:
    repeat_list_letters_copy = repeat_list_letters[:]
    word_as_list = list(word)
    multiletter_out_of_bounds = False
    for i in word_as_list:
        try:
            repeat_list_letters_copy.remove(i)
        except ValueError:
            multiletter_out_of_bounds = True
            break
    if not multiletter_out_of_bounds:
        phrase = (word,)
        if repeat_list_letters_copy != []:
            anagram_it(repeat_list_letters_copy, phrase)
            phrase = phrase[:-1]
        else:
            new_string = " ".join(phrase)
            m.update(new_string)
            if m.hexdigest() == test_hash:
                printSuccess(new_string)
            elif m.hexdigest() == "4624d200580677270a54ccff86b9610e":
                printSuccess(new_string)
                sys.exit(0)
    phrase = (word,)

