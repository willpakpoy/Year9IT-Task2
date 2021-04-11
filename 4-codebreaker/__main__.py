'''md
© Will Pak Poy 2021


# Pseudocode

1. First up, we make a list of every character in the alphabet, plus a space at the end.
2. We then present the user with fields to enter their number string or letter string.
3. They then have the option to encode or decode their strings.
    a. If they choose encode, the letter string is passed to the encode function.
        1. We first strip away any stray spaces.
        2. We convert the letter strings to be entirely lower case, and create a list array containing each individual character.
        3. For each character, we find the index of the character from the alphabet list array and append it to the "encoded_string" string.
        4. We then set the "encoded" dynamic variable to "encoded_string".
    b. If they choose decode, the number string is passed to the decode function.
        1. We first strip away any stray spaces.
        2. We split the string into a list array of each individual number.
        3. For each number, we search for the character corresponding to the number by the index. We append this to the "decoded_string" array.
        4. We then set the "decoded" dynamic variable to "decoded_string".
4. This means overall that it is simple to encode and decode the strings.
'''

from tkinter import *
import string

# Tkinter initialisation and boilerplate.
window = Tk()
window.minsize('600', '300')
window.title('4 - Codebreaker')

# Our alphabet array
alphabet = list(string.ascii_lowercase + " ") # create a globally-defined alphabet array, with a space at the end.

# Tkinter bindable values.
decoded=StringVar()
encoded=StringVar()

# Tkinter widgets that are rendered.
Label(window, text="Two-way CodeMaker/Breaker").grid(column=1, row=0) # Title

Label(window, text="Decoded String (Letters)").grid(column=0, row=1) # Label for the text field.
Entry(window, textvariable=decoded).grid(column=0, row=2)

Label(window, text="Encoded String (Numbers)").grid(column=2, row=1) # Label for the text field.
Entry(window, textvariable=encoded).grid(column=2, row=2)

Button(window, text="Encode", command=lambda : encode()).grid(column=0, row=3) # Clicking this button runs the 'encode' function.
Button(window, text="Decode", command=lambda : decode()).grid(column=2, row=3) # Clicking this button runs the 'decode' function.

def encode():
    to_encode = decoded.get().strip()
    to_encode_array = list(to_encode.lower()) # an array of each character waiting to be encoded
    encoded_string = ""
    for letter in to_encode_array: # We loop over the "to_encode" array,
        this_letter_as_number = alphabet.index(letter)+1 # search for the index of the letter,
        encoded_string += f"{this_letter_as_number} " # and append this to the encoded_string array.
    encoded.set(encoded_string.strip()) # We then set the "encoded" dynamic variable to "encoded_string"

def decode():
    to_decode = encoded.get().strip()
    to_decode_array = to_decode.split(" ") # all of the individual numbers that correspond to the letters.
    decoded_string = ""
    for number in to_decode_array: # For each number in the array,
        decoded_string += alphabet[int(number)-1] # we search for the letter from the index and append the letter to tne "decoded_string" string.
    decoded.set(decoded_string.strip()) # We then set the "decoded" dynamic variable to "decoded_string".

window.mainloop()