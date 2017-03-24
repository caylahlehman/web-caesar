upper_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_alphabet="abcdefghijklmnopqrstuvwxyz"

def alphabet_position(letter):
    letter=letter.lower()
    return lower_alphabet.index(letter)


def rotate_character(char,rot):
    if char not in upper_alphabet and char not in lower_alphabet:
        return char
    starting_position=alphabet_position(char)
    ending_position=(starting_position+rot)%26
    if char in upper_alphabet:
        return upper_alphabet[ending_position]
    else:
        return lower_alphabet[ending_position]

def encrypt(text,rot):
    encrypt_string=""
    for char in text:
        encrypt_string=encrypt_string+rotate_character(char,rot)
    return encrypt_string
