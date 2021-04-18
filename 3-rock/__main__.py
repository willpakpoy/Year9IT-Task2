'''md
© Will Pak Poy 2021


# Pseudocode

1. Ask the user to make a choice, between Rock, Paper and Scissors. We pass this choice to the make_choice function.
2. This function then checks who has won that round by:
    1. Getting the computers choice, via the calculate_python_choice function.
    2. And then simply following the rules of the game to check who has won.
    3. The winner is then passed to the declare_winner function, which updates the winner_text variable, therefore displaying the winner to the user.
'''

from tkinter import *
from random import randint

# Tkinter initialisation and boilerplate
window = Tk()
window.minsize('600', '300')
window.title('3 - Rock')

# Our Tkinter bindable values.
user_chooses_text = StringVar()
python_chooses_text = StringVar()
winner_text = StringVar()

Label(window, text=f"Please make a choice.", anchor="w", justify=LEFT).grid(column=0, row=1)

# These buttons call the make_choice function with their respective choice.
Button(window, text="Rock", command=lambda : make_choice("rock")).grid(column=1, row=2)
Button(window, text="Paper", command=lambda : make_choice("paper")).grid(column=2, row=2)
Button(window, text="Scissors", command=lambda : make_choice("scissors")).grid(column=3, row=2)

# These labels dynamically bind to their respective variables, using the Tkinter StringVar().
Label(window, textvariable=user_chooses_text, anchor="w", justify=LEFT).grid(column=0, row=4) # Label for the text field.
Label(window, textvariable=python_chooses_text, anchor="w", justify=LEFT).grid(column=0, row=5) # Label for the text field.
Label(window, textvariable=winner_text, anchor="w", justify=LEFT).grid(column=0, row=6) # Label for the text field.

# We use the logic provided in the assesment task sheet to determine "Python's choice".
def calculate_python_choice():
    number_choice = randint(0,99)
    if number_choice < 33:
        return "rock"
    elif number_choice >= 33 and number_choice < 66:
        return "paper"
    else:
        return "scissors"

# This function simply updates the text field.
def declare_winner(winner):
    if winner == "draw":
        winner_text.set("Draw! Play again!")
    else:
        winner_text.set(f"{winner.capitalize()} wins this round.")

# This uses the logic of the game to determine the winner.
def make_choice(user_choice):
    python_choice = calculate_python_choice()

    # Updating the dynamic variables.
    user_chooses_text.set(f"User chooses {user_choice}")
    python_chooses_text.set(f"Python chooses {python_choice}")

    if user_choice == python_choice:
        declare_winner("draw")
    
    elif user_choice == "rock":
        if python_choice == "scissors":
            declare_winner("user")
            
        else:
            declare_winner("python")

    elif user_choice == "scissors":
        if python_choice == "paper":
            declare_winner("user")
            
        else:
            declare_winner("python")

    elif user_choice == "paper":
        if python_choice == "scissors":
            declare_winner("user")
        else:
            declare_winner("python")
            
col_count, row_count = window.grid_size()
for row in range(row_count):
    window.grid_rowconfigure(row, minsize=5)

window.mainloop()