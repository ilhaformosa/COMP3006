
import sys

need_count_word = "abcdefghijklmnopqrstuvwxyz"


def add_frequencies(d, file, remove_case):
    line = file.readline()
    if remove_case: # remove cases in letters
        line = line.lower()
    letters = "".join([char for char in line.split() if char.isalpha()])

    for letter in letters:
        if need_count_word is not None:
            # handle lower and upper case letters
            if letter.lower() in need_count_word or letter.upper() in need_count_word:
                d[letter] = d.get(letter, 0)+1
                continue
            else:
                continue
        else:
            d[letter] = d.get(letter, 0)+1

# main() defined in count_to_csv.py
def count_letter(remove_case, selected_count_word, fill_zero, file_list):
    global need_count_word
    if selected_count_word is not None:
        need_count_word = selected_count_word
    d = {}

    # process multiple files
    for filename in file_list:
        with open(filename, 'r') as file:
            add_frequencies(d, file, remove_case)

    # add frequencies for letters not in the need_count_word
    if fill_zero:
        for word in need_count_word:
            if word not in d:
                d[word] = 0
            if not remove_case and word.upper() not in d:
                d[word.upper()] = 0
    return d






