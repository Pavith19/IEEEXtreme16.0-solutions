"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""
code = {'a': 'o', 'b': 'p', 'c': 'q', 'd': 'r', 'e': 's', 'f': 't', 'g': 'u', 'h': 'v', 'i': 'w', 'j': 'x', 'k': 'y', 
        'l': 'z', 'm': 'a', 'n': 'b', 'o': 'c', 'p': 'd', 'q': 'e', 'r': 'f', 's': 'g', 't': 'h', 'u': 'i', 'v': 'j', 
        'w': 'k', 'x': 'l', 'y': 'm', 'z': 'n' ,
        'A': 'O', 'B': 'P', 'C': 'Q', 'D': 'R', 'E': 'S', 'F': 'T', 'G': 'U', 'H': 'V', 'I': 'W', 'J': 'X', 'K': 'Y',
        'L': 'Z', 'M': 'A', 'N': 'B', 'O': 'C', 'P': 'D', 'Q': 'E', 'R': 'F', 'S': 'G', 'T': 'H', 'U': 'I', 'V': 'J',
        'W': 'K', 'X': 'L', 'Y': 'M', 'Z': 'N'}


word = input()

for letter in word:
        if letter in code:
                print(code[letter],end="")
        else:
                print(letter,end="")
