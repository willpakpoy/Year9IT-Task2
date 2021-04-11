'''md
© Will Pak Poy 2021


# Pseudocode

1. Ask the user the three numerical values, being counts of total, joe and jane's rounds.
2. On submit, we run the compute function.
    1. First, we check to ensure the total number of rounds is higher than zero.
    2. Next, we check if Joe or Jane's number of rounds is higher than the total.
    3. We then check if their combined number of rounds is higher than the total.
    4. We divide the number of rounds by 2, and check if Joe or Jane's number of rounds is higher. We then alert the user accordingly through the win_status variable.
    5. If none of the other requirements are met, we calculate how many more rounds Jane must win to win the game.
'''
from tkinter import *
from random import randint

window = Tk()
window.minsize('600', '300')
window.title('2 - Round')

# Our Tkinter bindable values.
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
    # We get the numbers from our Tkinter bindable values, to allow for easier computation, and cleaner looking code.
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

# This code is to ensure the sizes of the individual cells in the grid layout are large enough to not appear crowded.
col_count, row_count = window.grid_size()
for row in range(row_count):
    window.grid_rowconfigure(row, minsize=5)

window.mainloop()

# TODO: Move this layout code into the other three areas. 