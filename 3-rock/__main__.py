from tkinter import *
from random import randint

window = Tk()
window.minsize('600', '300')
window.title('3 - Rock')


num_rounds = 3

user_chooses_text = StringVar()
python_chooses_text = StringVar()
winner_text = StringVar()

Label(window, text=f"Number of rounds: {num_rounds}", anchor="w", justify=LEFT).grid(column=0, row=0) # Label for the text field.
Label(window, text=f"Please make a choice.", anchor="w", justify=LEFT).grid(column=0, row=1) # Label for the text field.

Button(window, text="Rock", command=lambda : make_choice("rock")).grid(column=1, row=2)
Button(window, text="Paper", command=lambda : make_choice("paper")).grid(column=2, row=2)
Button(window, text="Scissors", command=lambda : make_choice("scissors")).grid(column=3, row=2)

Label(window, textvariable=user_chooses_text, anchor="w", justify=LEFT).grid(column=0, row=4) # Label for the text field.
Label(window, textvariable=python_chooses_text, anchor="w", justify=LEFT).grid(column=0, row=5) # Label for the text field.
Label(window, textvariable=winner_text, anchor="w", justify=LEFT).grid(column=0, row=6) # Label for the text field.

def calculate_python_choice():
    number_choice = randint(0,99)
    if number_choice < 33:
        return "rock"
    elif number_choice >= 33 and number_choice < 66:
        return "paper"
    else:
        return "scissors"

def declare_winner(winner):
    winner_text.set(winner)

def make_choice(user_choice):
    python_choice = calculate_python_choice()

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

    

window.mainloop()