"""
>>> rotate_13_forward(0)
13

>>> convert_ascii_to_alphabet(65)
0
>>> convert_ascii_to_alphabet(98)
1
>>> alphabet_index_to_ascii_character(0)
'A'

>>> decryptor("V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL!")
'I AM LEARNING PYTHON WITH SHE CODES ACADEMY!'

>>> encryptor('I AM LEARNING PYTHON WITH SHE CODES ACADEMY!')
'V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL!'
"""

# This program is implying encryption and decryption method in which each letter is replaced with another letter in a permanent shift of 13.
# Try to decifer this: V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL!


def ascii_index(letter: chr):
    return ord(letter)


def convert_ascii_to_alphabet(ascii_index: int):
    """function that converts ascii index to alphabet index"""
    # take the index from ascii
    # if its (upper/lower) case letter:
    first_letter = ""
    # upper
    if ascii_index <= 90:
        first_letter = "A"
    else:
        first_letter = "a"
    # reduce the ascii index of (A/a) from it
    return ascii_index - ord(first_letter)


def rotate_13_forward(alphabet_index: int):
    length_of_alphabet = 26
    return (alphabet_index + 13) % length_of_alphabet


def rotate_13_backward(alphabet_index: int):
    length_of_alphabet = 26
    return (alphabet_index - 13) % length_of_alphabet


def alphabet_index_to_ascii_character(alphabet_index: int):
    """function that converts alphabetic index to an ascii character"""
    return chr(alphabet_index + 65)


def cryptor(message: str, strategy):
    # dependecy injection and strategy pattern
    """function that connects all the functions"""
    crypted_message = ""
    for char in message:
        if char.isalpha() == True:
            crypted_message += alphabet_index_to_ascii_character(
                strategy(convert_ascii_to_alphabet(ascii_index(char))))
        else:
            crypted_message += char
    return crypted_message


def encryptor(message: str):
    return cryptor(message, rotate_13_backward)


def decryptor(message: str):
    return cryptor(message, rotate_13_forward)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
