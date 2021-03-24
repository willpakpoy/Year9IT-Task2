'''md
© Will Pak Poy 2021


# Pseudocode

1. Build and generate the Tkinter window.
2. Pick a random number
3. Create the dynamic variables for Tkinter.
4. On button click:
    1. Print the two number values.
    2. Compare the generated number to the inputted one.
        1. If the inputted number is correct, print correct and **TD** unpack the other UI elements.
        2. If the number is higher or lower than the generated number, increment the guesses counter and update the status variable.
'''
from tkinter import *
from random import randint

window = Tk()
window.minsize('600', '300')
window.title('2 - Round')

joe_rounds = IntVar(0) # Number of rounds Joe has won.
jane_rounds = IntVar(0) # Number of rounds Jane has won.
total_rounds = IntVar(0) # Number of rounds in total.
win_status = StringVar()

Label(window, text="Total number of rounds").grid(column=0, row=0) # Label for the text field.
Entry(window, textvariable=total_rounds).grid(column=0, row=1)

Label(window, text="Rounds Joe has won").grid(column=0, row=4) # Label for the text field.
Entry(window, textvariable=joe_rounds).grid(column=0, row=5)

Label(window, text="Rounds Jane has won").grid(column=1, row=4) # Label for the text field.
Entry(window, textvariable=jane_rounds).grid(column=1, row=5)

Button(window, text="Submit", command=lambda : compute()).grid(column=0, row=7) # Clicking this button runs the 'compute' function.

Label(window, text="Possibility for Jane to win").grid(column=0, row=8) # Label for the text field.
Label(window, textvariable=win_status).grid(column=0, row=9) # Label for the text field.

def compute():
    joe=joe_rounds.get()
    jane=jane_rounds.get()
    total=total_rounds.get()

    if total <= 1:
        win_status.set("Total rounds must be greater than zero.")
        return
    
    if joe > total or jane > total:
        win_status.set("Personal number of rounds is higher than total.")
        return

    if joe+jane > total:
        win_status.set("Personal number of rounds is higher than total.")
        return
    
    if total / 2 < joe:
        win_status.set("Impossible, Joe has won more than half of the rounds.")
        return
    elif total / 2 < jane:
        win_status.set("Jane has already won.")
        return

    else:
        jane_win_by = total / 2 +1 - jane
        win_status.set(f"Jane must win {int(jane_win_by)} more rounds to secure a win against Joe.")
        return

col_count, row_count = window.grid_size()
for row in range(row_count):
    window.grid_rowconfigure(row, minsize=5)

window.mainloop()

# TODO: comments + pseudocode