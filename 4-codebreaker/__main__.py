from tkinter import *
import string

window = Tk()
window.minsize('600', '300')
window.title('4 - Codebreaker')

alphabet = list(string.ascii_lowercase + " ") # create a globally-defined alphabet array, with a space at the end :)

decoded=StringVar()
encoded=StringVar()

Label(window, text="Two-way CodeMaker/Breaker").grid(column=1, row=0) # Label for the text field.

Label(window, text="Decoded String (Letters)").grid(column=0, row=1) # Label for the text field.
Entry(window, textvariable=decoded).grid(column=0, row=2)

Label(window, text="Encoded String (Numbers)").grid(column=2, row=1) # Label for the text field.
Entry(window, textvariable=encoded).grid(column=2, row=2)

Button(window, text="Encode", command=lambda : encode()).grid(column=0, row=3) # Clicking this button runs the 'compute' function.
Button(window, text="Decode", command=lambda : decode()).grid(column=2, row=3) # Clicking this button runs the 'compute' function.

def encode():
    to_encode = decoded.get().strip()
    to_encode_array = list(to_encode.lower())
    encoded_string = ""
    for letter in to_encode_array:
        this_letter_as_number = alphabet.index(letter)+1
        encoded_string += f"{this_letter_as_number} "
    encoded.set(encoded_string.strip())

def decode():
    to_decode = encoded.get().strip()
    to_decode_array = to_decode.split(" ")
    decoded_string = ""
    for number in to_decode_array:
        decoded_string += alphabet[int(number)-1]
    decoded.set(decoded_string.strip())
    
window.mainloop()