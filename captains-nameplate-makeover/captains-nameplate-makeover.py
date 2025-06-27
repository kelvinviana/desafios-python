# Captain's Nameplate Makeover

# Challenge

# Easy
# Create a function named redecorate_ship_name that receives ship_name as its parameter.

# As a valorous ship captain, you've decided to redecorate your vessel by creating a unique nameplate. Your task is to implement a function that modifies the ship's name according to specific rules.

# Follow these steps to redecorate the ship's name:

# Reverse the entire ship name.
# For each word in the reversed name:
# If the word starts with a vowel (a, e, i, o, u), keep it as is.
# If the word starts with a consonant, remove all vowels from that word.
# Stop the process if you encounter the word "dock" (case-insensitive) in the reversed name.
# Use basic loop control statements, such as break and continue, to implement this logic.

# Parameters:

# ship_name (str): A string representing the name of the ship. It may contain one or more words separated by spaces. (1 <= len(ship_name) <= 100)
# The function returns a string representing the redecorated ship name after applying the modification rules.

def redecorate_ship_name(ship_name):
    reversed_ship_name = ship_name[::-1].split()
    vogais = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    processed_ship_name = []
    for word in reversed_ship_name:
        if word.startswith(vogais):
            processed_ship_name.append(word)
        else:
            word_withou_vowel = "".join(letter for letter in word if letter not in vogais)
            processed_ship_name.append(word_withou_vowel)


    return " ".join(processed_ship_name)

nome_navio = input()

print(redecorate_ship_name(nome_navio))