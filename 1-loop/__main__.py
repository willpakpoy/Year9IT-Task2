'''md
© Will Pak Poy 2021


# Pseudocode

1. Build and generate the Tkinter window.
2. Pick a random number
3. Create the dynamic variables for Tkinter.
4. On button click:
    1. Print the two number values.
    2. Compare the generated number to the inputted one.
        1. If the inputted number is correct, print correct and TODO: unpack the other UI elements.
        2. If the number is higher or lower than the generated number, increment the guesses counter and update the status variable.
'''
from tkinter import *
from random import randint

window = Tk()
window.minsize('600', '300')
window.title('1 - Loop')

number_to_guess = randint(1,100) # This is the computer-generated number that we want the user to guess.
count_guesses = IntVar(0) # This is a dynamic variable that stores how many 'guesses' the user has had.
status = StringVar() # This is the status of the guess, displayed at the bottom (either "Correct!", "Higher!", or "Lower!")

guess = IntVar() # This is storing the user's guess for easy access.
Label(window, text="Please enter a number").pack() # Label for the text field.

guess_field = Entry(window, textvariable=guess).pack() # We bind the text field to the 'guess' variable.
Button(window, text="Submit", command=lambda : compute()).pack() # Clicking this button runs the 'compute' function.

Label(window, text="Number of guesses:").pack() # Label for dynamic guesses and status.
Label(window, textvariable=count_guesses).pack()
Label(window, textvariable=status).pack()


def compute():
    print(guess.get())
    print(number_to_guess) # Print the guess that the user has made, and the random number generated before.
    if guess.get() == number_to_guess: # If the user's entered number equals the number to guess, set the status to correct.
        count_guesses.set(count_guesses.get()+1)
        status.set("Correct!")
    elif guess.get() < number_to_guess: # If the user's entered number is less than the number to guess, set the status to higher and increment the counter..
        count_guesses.set(count_guesses.get()+1)
        status.set("Higher!")
    elif guess.get() > number_to_guess: # If the user's entered number is greater than the number to guess, set the status to higher and increment the counter.
        count_guesses.set(count_guesses.get()+1)
        status.set("Lower!")

window.mainloop()