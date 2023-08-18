"""Calculate score for a word
Different letters carry different score
Take an input string loop through each char
check its score from a dictionary
sum scores """
import string
from random import randint
alphabet = string.ascii

letter_dict = {
    1 : ["E" , "A", "I", "O", "N", "R", "T", "L", "S", "U"],
    2 : "DG",
    3 : "BCMP",
    4: "FHWVY",
    5: "K",
    8 : "JX",
    10 : "QZ"
}



def calculate_score(string):
    score = 0
    for char in string:
        for k,v in letter_dict.items():
            if char in v:
                score += k
    return score



def seven_random_tiles(tile_list):
    
    players_rack = []
    for i in range(7):
        char_index = randint(0, len(tile_list) - 1)

        players_rack.append(tile_list.pop(char_index))
    return players_rack


def create_tile_list():
    tile_str = ""
    tile_str += "KJXQZ"
    tile_str += "BCMPFHVWY" * 2
    tile_str += "G" * 3
    tile_str += "LSUD" * 4
    tile_str += "NRT" * 6
    tile_str += "O" * 8
    tile_str += "AI" * 9
    tile_str += "E" * 12

    tile_list = [char for char in tile_str]

    return tile_list

def check_words(word, wordlist):
    pass

def generate_word_from_rack(rack):
    "Task 4 unfinished"
    word = ""
    for letter in rack:
        word += letter
        check_words()
        for 


print(seven_random_tiles(create_tile_list()))

# print(calculate_score("HI"))

