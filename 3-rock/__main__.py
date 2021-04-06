from tkinter import *
from random import randint

window = Tk()
window.minsize('600', '300')
window.title('3 - Rock')

num_rounds = 3

most_recent_user_choice = StringVar()


Label(window, text=f"Number of rounds: {num_rounds}", anchor="w", justify=LEFT).grid(column=0, row=0) # Label for the text field.
Label(window, text=f"Please make a choice.", anchor="w", justify=LEFT).grid(column=0, row=1) # Label for the text field.

Button(window, text="Submit", command=lambda : compute()).grid(column=0, row=1)


Label(window, text="Rounds Joe has won").grid(column=0, row=4) # Label for the text field.
Entry(window, textvariable=joe_rounds).grid(column=0, row=5)

Label(window, text="Rounds jane has won").grid(column=1, row=4) # Label for the text field.
Entry(window, textvariable=jane_rounds).grid(column=1, row=5)


Label(window, text="Possibility for Jane to win").grid(column=0, row=8) # Label for the text field.
Label(window, textvariable=win_status).grid(column=0, row=9) # Label for the text field.

window.mainloop()