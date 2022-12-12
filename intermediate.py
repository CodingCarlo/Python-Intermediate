def shift_letter(letter, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        index = alphabet.index(letter)
        shift += index
        if shift < 25:
            shifted_letter = alphabet[shift]
        else:
            shifted_letter = alphabet[shift - 26]
    except:
        shifted_letter = '" "'

    return shifted_letter

def caesar_cipher(message, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = list(message)
    word = ""
    
    for letter in message:
        index = alphabet.index(letter)
        new_shift = shift + index
        if new_shift < 25:
            shifted_letter = alphabet[new_shift]
        else:
            shifted_letter = alphabet[new_shift - 26]
        word += shifted_letter

    return word

def shift_by_letter(letter, letter_shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        index = alphabet.index(letter)
        shift = alphabet.index(letter_shift)
        shift += index - 1
        if shift < 25:
            shifted_letter = alphabet[shift]
        else:
            shifted_letter = alphabet[shift - 26]
    except:
        shifted_letter = '" "'

    return shifted_letter

def vigenere_cipher(message, key):
    import math

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = list(key)
    key_int = []
    word = ""

    if len(key) < len(message):
        key = key * math.ceil(len(message) / len(key))
        while len(key) != len(message):
            del key[len(key) - 1]
            
    for letter in key:
        int = key.index(letter)
        key_int.append(int)

    for letter in message:
        index = alphabet.index(letter)
        new_shift = key_int[message.index(letter)] + index
        if new_shift < 25:
            shifted_letter = alphabet[new_shift]
        else:
            shifted_letter = alphabet[new_shift - 26]
        word += shifted_letter
    
    return word

print(vigenere_cipher("BITCH", 'ABC'))
    
    


