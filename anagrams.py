__author__ = 'stevenbarnhurst'
import hashlib

anagram = "poultry outwits ants"
md5 = "4624d200580677270a54ccff86b9610e"

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
new_wordlist.sort(key=len, reverse=True)  # sorts by descending length
m = hashlib.md5()  # prepare hashing

combo_dict = {}

def anagram_it(letters_remaining, phrase=()):
    length = len(letters_remaining)  # end loop if more letters in word than in list
    for word in new_wordlist:
        if not letters_remaining:
            new_string = " ".join(phrase)
            print(new_string)
            return phrase
        elif len(word) > length:
            return phrase
        else:
            word_as_list = list(word)
            letter_absent = any(True for x in word_as_list if x not in letters_remaining)
            if not letter_absent:
                multiletter_out_of_bounds = False
                letters_remaining_copy = letters_remaining[:]
                for i in word_as_list:
                    try:
                        letters_remaining_copy.remove(i)
                    except ValueError:
                        multiletter_out_of_bounds = True
                        break
                if not multiletter_out_of_bounds:
                    phrase = phrase + (word,)
                    anagram_it(letters_remaining_copy, phrase)
                    phrase = phrase[:-1]

print(new_wordlist)
m.update("poultry outwits ants")
print m.hexdigest()
anagram_it(repeat_list_letters)

