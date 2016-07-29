import random


def main():
    # Let's define all our messages up here
    # Go through and broadcast all the different ciphers on different channels
    print('Encryption begin!')
    # The answer to the caesar cipher
    caesar_message = "LEARN TO CODE!"
    # How much we're shifting the message by
    caesar_message_shift = 12

    # The answer to the addition cipher
    addition_message = "MICRO BIT"
    # How often we add random letters
    n = 3

    # The answer to the image puzzle: a smiley face
    image_message = [[0, 9, 0, 9, 0],
                     [0, 9, 0, 9, 0],
                     [0, 0, 0, 0, 0],
                     [9, 0, 0, 0, 9],
                     [0, 9, 9, 9, 0]]

    # The pad we're using to mask the image
    image_pad = [[1, 0, 0, 1, 1],
                 [0, 1, 1, 0, 0],
                 [1, 1, 1, 0, 0],
                 [0, 0, 1, 0, 1],
                 [1, 1, 1, 1, 1]]

    # The answer to the vignere cipher
    vignere_message = "WAYNE ROONEY IS SMARTER THAN YOU"

    # The key for the vignere cipher (ONLY USE A-Z UPPERCASE)
    vignere_key = "BADGER"

    # Now that we have all the messages, let's make the encryptions

    # Caesar cipher
    caesar_cipher_message = caesar_shift(caesar_message, caesar_message_shift)

    # Character addition cipher
    addition_cipher_message = add_nth_char(addition_message, n)

    # Image mask cipher
    image_cipher_message = apply_mask2D(image_message, image_pad)

    # Vignere cipher
    vignere_cipher_message = vignere_enc(vignere_message, vignere_key)

    # For this last one let's get a little more complicated. Why not combine a few of the cipher methods together?
    composite_message = "NOW YOU'RE A CRYPTOGRAPHY MASTER"

    # First let's apply a caesar cipher. For this we'll need a shift amount
    composite_shift_amount = -5

    # Next we'll add a few random characters, so assign an n value
    composite_n_value = 2

    # Finally we'll apply a vignere cipher, so let's pick a key
    composite_vignere_key = "ACORN"

    # Let's make a variable for the cipher message. We can keep updating it so we only need one variable
    composite_cipher_message = composite_message

    # Start with the caesar cipher
    composite_cipher_message = caesar_shift(composite_cipher_message, composite_shift_amount)
    # The cipher message should now be 'IJR TJP'MZ V XMTKOJBMVKCT HVNOZM'

    # Now apply the addition cipher
    composite_cipher_message = add_nth_char(composite_cipher_message, composite_n_value)
    # The cipher message should look something like 'ICJORZ DTWJJPJ'AMLZH KVI VXVMQTIKPOSJNBRMOVRKFCSTF YHLVLNZOIZSMW'
    # Remember that the letters being added are random, so it may look a bit different

    # Finally, apply the vignere cipher
    composite_cipher_message = vignere_enc(composite_cipher_message, composite_vignere_key)
    # The final cipher message should be close to  'CXRJYM YELDPXV'XIUKQ VDF MTPXPNZSWVZFQMGGEDZRUYQEK CPACTJVZGTWUD'
    # Remember that we added random letters, so it might look a bit different

    # Now that we have all the ciphers, let's turn on the radio and start broadcasting!


def caesar_shift(word, shift_amount):
    # Given a word, shift every character's ASCII value by shift_amount. For example, "hello world" would become
    # "ifmmp xprme".
    # param input: The word you'd like to shift.
    # param shift_amount: The amount you'd like to shift. This can be a negative number.
    # return: The shifted word, or the input if it isn't a word
    if not isinstance(word, str) or not isinstance(shift_amount, int):
        return word
    word = word.lower()
    return shift_word(word, shift_amount)


def shift_word(word, shift_amount):
    # Shifts each letter in a word alphabetically by the amount specified by shift_amount. Wraps around, so the
    # value can be negative. For example, HI shifted by 2 would become JK (J is two after H, K is two after I)
    # param word: The word to shift
    # param shift_amount: The amount to shift
    # return: The shifted word, or the original word if the arguments are wrong.

    # Make sure word is actually a word
    if not isinstance(word, str):
        return word
    # Make sure shift_amount is a number
    if not isinstance(shift_amount, int):
        return word
    # We're only working with upper case, so make it upper case
    word = word.upper()
    return_word = ""
    # Shift each character in the word using shift_char
    for character in word:
        return_word = return_word + shift_char(character, shift_amount)
    return return_word


def shift_char(char, shift_amount):
    # Shifts a character by an amount specified by shift_amount. For example, shifting character A by 2 produces C.
    # param char: Character to be shifted. Must be uppercase A-Z to have an effect.
    # param shift_amount: The amount to shift, which wraps around. Can be negative.
    # return: The shifted character, or the original character if the input isn't A-Z (uppercase).

    try:
        # Make sure nothing bad happens getting the character value
        char_val = ord(char)
    except Exception:
        # If something unexpected happens, return the input
        return char
    # Ensure the character is valid (65 is ASCII for A and 90 is ASCII for Z)
    if char_val > 90 or char_val < 65:
        # If not, return the character
        return char
    # Get the alphabetical value of the character, with A at 0, B at 1, etc.
    char_alpha_value = char_val - 65
    # Now add the shift amount
    char_shift_alpha_value = char_alpha_value + shift_amount
    # Wrap around if the value is too large
    char_shift_alpha_value = char_shift_alpha_value % 26
    # Finally, convert back to the ascii value
    char_shift_value = char_shift_alpha_value + 65
    return chr(char_shift_value)


def remove_nth_char(word, n):
    # Removes every nth character from a word. For example, n = 3 will remove every third character from a word,
    # starting at index 2 (the third character). Note that a space counts as a character.
    # param input: The input word from which to remove characters.
    # param n: remove every nth character. n must be greater than 1
    # return: The word with every nth character removed, or the original word if n isn't greater than 1
    if not isinstance(n, int):
        return word
    if n < 2:
        return word
    output = ""
    # Look through each letter in the word and remove the nth character
    for i in range(len(word)):
        if i % n != n - 1:
            output = output + word[i]
    return output


def add_nth_char(word, n):
    # Modifies a word by adding a random character at every nth position. For example, n = 3 will cause the word
    # to have a random character every 3rd letter. "Hello world" might become "Hecllpo two,rlxd". Note that a space
    # counts as a character.
    # param input: The input word to which to add the random characters.
    # param n: Add a random character at every nth position. n must be greater than 1.
    # return: The word with a random character added every nth position, or the original word if n isn't greater than 1
    if not isinstance(n, int):
        return word
    if n < 2:
        return word
    output = ""
    # Look through the word, keeping count of characters. Every n-1 characters, add a random character
    # The end result will be that every nth character is a randomly added character.
    for i in range(len(word)):
        output = output + word[i]
        if i % (n - 1) == n - 2:
            output = output + random.choice(
                ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z'])
    return output


def apply_mask1D(image1, image2):
    # XOR together two 1-D arrays. Nonzero represents 1, zero represents 0.
    # param image1: The first array. Must be the same dimensions as the second array
    # param image2: The second array. Must be the same dimensions as the first array
    # return: The masked array result, or the first array if the operation fails.
    # Make sure both are lists
    if not isinstance(image1, list) or not isinstance(image2, list):
        return image1
    # Make sure neither list is null
    if not image1 or not image2:
        return image1
    # Make sure both lists are the same length
    if len(image1) != len(image2):
        return image1
    # Set the eventual return image to the first image
    return_image = image1
    # Go through each spot in the array and see if both are on or off. If they are, the end result is off.
    # If only one of the arrays is on, then the end result is on.
    # A useful operation for this is XOR, which is denoted by the '^' symbol, and does exactly what we want.
    for i in range(len(image1)):
        mask = bool(return_image[i]) ^ bool(image2[i])
        if mask:
            return_image[i] = 9
        else:
            return_image[i] = 0
    return return_image


def apply_mask2D(image1, image2):
    # XOR together two 2-D arrays. Nonzero represents 1, zero represents 0.
    # param image1: The first array. Must be the same dimensions as the second array.
    # param image2: The second array. Must be the same dimensions as the first array.
    # return: The masked array result, or the first array if the operation fails.

    # Make sure neither list is null
    if not image1 or not image2:
        return image1
    # Make sure both lists are 2-D
    if not isinstance(image1, list) or not isinstance(image1[0], list) or not isinstance(image2,
                                                                                         list) or not isinstance(
        image2[0], list):
        return image1
    if not image1 or not image2:
        return image1
    # Make sure the lists are the same length
    if len(image1) != len(image2):
        return image1
    if len(image1[0]) != len(image2[0]):
        return image1
    # Perform the mask
    return_image = image1
    # Because it's a 2-D array, we need to go through each row and column and apply our XOR function, which turns
    # on the array location if only one of the incoming arrays is on. It is turned off if both arrays are either
    # on or off
    for i in range(len(image1)):
        for j in range(len(image1[i])):
            mask = bool(return_image[i][j]) ^ bool(image2[i][j])
            if mask:
                return_image[i][j] = 9
            else:
                return_image[i][j] = 0
    return return_image


def vignere_enc(word, key):
    # Encrypts a word using the vignere cipher on all alphabet characters using a specified key
    # param input: The word to encrypt.
    # param key: The key with which to encrypt the word
    # return: An encrypted version of the input word.
    if not isinstance(word, str):
        return word
    if not isinstance(key, str) or len(key) < 1:
        return word
    key = key.upper()
    output = ""
    # We want to go through each word and alter each character
    for i in range(len(word)):
        # Determine which character of the key we're currently on
        key_char = key[i % len(key)]
        shift_char_val = ord(key_char)
        # Shift the character by the amount specified by the key character. We calculate this by determining its
        # distance in the alphabet from A. In computer world, A is represented by the value 65
        shift_amount = shift_char_val - 65
        output = output + shift_char(word[i], shift_amount)
    return output


def vignere_dec(word, key):
    # Decrypes a word using the vignere cihper on all alphabet characters using a specified key. The key should be the
    # same as the key used for encryption for the message to make sense.
    # param input: Input word (the encrypted word).
    # param key: The key that was used to encrypt the word.
    # return: The original word, decrypted.
    if not isinstance(word, str):
        return word
    if not isinstance(key, str) or len(key) < 1:
        return word
    key = key.upper()
    output = ""
    for i in range(len(word)):
        # Determine which character of the key we're currently on
        key_char = key[i % len(key)]
        shift_char_val = ord(key_char)
        # Shift the character backwards by the amount specified by the key character. We calculate this by determining
        # its distance in the alphabet from A. In computer world, A is represented by the value 65
        shift_amount = shift_char_val - 97
        output = output + shift_char(word[i], -shift_amount)
    return output


def flip_word(word):
    # Given a word, returns the word backwards. For example, "HELLO" would be returned as "OLLEH"
    # param word: The word you want to flip, in upper case
    # return: A flipped version of the word supplied, or the original word if it isn't a valid word

    if not isinstance(word, str):
        return word
    # This statement magically does exactly what we want
    return word[::1]


def mirror_word(word):
    # Given a word, this function takes every letter and flips it across the center of the alphabet.
    # For example, A becomes Z, B becomes Y, etc. The word "HELLO" would become
    # param word: The word you want to mirror, in upper case
    # return:

    # Make sure word is actually a word
    if not isinstance(word, str):
        return word
    word = word.upper()
    output_word = ""
    for character in word:
        # Figure out where the character is in the alphabet
        char_val = ord(character)
        # Figure out how far into the alphabet it is
        char_val = char_val - 65
        # We're doing this in two steps, depending on if the character is in the first or second half of the
        # alphabet
        if 13 > char_val >= 0:
            output_word = output_word + chr(90 - char_val)
        elif 26 > char_val >= 13:
            output_word = output_word + chr(65 + (25 - char_val))
        else:
            output_word = output_word + character
    return output_word


def pig_latin_enc_phrase(phrase):
    # Encodes an entire phrase into pig latin. For example, "DO YOU SPEAK PIG LATIN?" would be encoded to
    # "ODAY OUYAY PEAKSAY IGPAY ATINLAY?"
    # param word:
    # return:

    # Separate by space and make an array of words
    if not isinstance(phrase, str):
        return phrase
    phrase = phrase.upper()
    string_array = phrase.split()
    output_word = ""
    # Scramble each word and add it to the eventual final result
    for word in string_array:
        output_word = output_word + " " + pig_latin_enc_word(word)
    return output_word


def pig_latin_enc_word(word):
    # Encodes a single word in "pig latin", which takes the beginning letter of a word and moves it to the end, adding
    # "ay" as well. For example "LATIN" becomes "ATINLAY". You shouldn't be calling this function yourself.
    # Use pig_latin_enc_phrase instead (that function will call this one for you).
    # param word: The word to encode to pig latin.
    # return: The word, encoded in pig latin

    if not isinstance(word, str):
        return word
    word = word.upper()
    # take the first character in the word and put it at the end
    output_word = word[1:len(word)] + word[0] + "AY"
    return output_word


def pig_latin_dec_phrase(phrase):
    # Decodes an entire phrase that was encoded into pig latin. For example, "ODAY OUYAY PEAKSAY IGPAY ATINLAY?" would be
    # decoded to "DO YOU SPEAK PIG LATIN?"
    # param phrase:
    # return:

    # Separate by space and make an array of words
    if not isinstance(phrase, str):
        return phrase
    phrase = phrase.upper()
    string_array = phrase.split()
    output_word = ""
    # Un-scramble each word and add it to the eventual final result
    for word in string_array:
        output_word = output_word + " " + pig_latin_dec_word(word)
    return output_word


def pig_latin_dec_word(word):
    # Decodes a single word from "pig latin", which takes the beginning letter of a word and moves it to the end, adding
    # "ay" as well. For example "ATINLAY" becomes "LATIN". You shouldn't be calling this function yourself.
    # Use pig_latin_dec_phrase instead (that function will call this one for you).
    # param word: The word to encode to pig latin.
    # return: The word, encoded in pig latin

    if not isinstance(word, str):
        return word
    word = word.upper()
    # Re-arrange the word back to its original state
    output_word = word[len(word) - 3] + word[:len(word) - 3]
    return output_word


if __name__ == "__main__":
    main()
