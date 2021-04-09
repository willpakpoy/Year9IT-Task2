from tkinter import *
import json
import time

window = Tk()
window.minsize('600', '300')
window.title('3 - Rock')

global datastore
datastore = json.loads(open("5-atm/atm-data.json", "r").read())
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def view_pin():
    clear_window()
    user_entered_pin = IntVar()
    count_attempts_left = 3
    incorrect_string = StringVar()

    Label(window, text="Welcome to ANZ Banking.\nPlease enter your pin to continue.", anchor="w", justify=LEFT, font="bold").grid(column=0, row=1) # Label for the text field.
    Entry(window, textvariable=user_entered_pin).grid(column=0, row=2)
    Button(window, text="Login", command=lambda : validate()).grid(column=0, row=3) # Clicking this button runs the 'compute' function.

    Label(window, textvariable=incorrect_string, anchor="w", justify=LEFT).grid(column=0, row=4) # Label for the text field.

    def validate():
        nonlocal count_attempts_left
        if datastore["pin"] == user_entered_pin.get():
            print("home")
        else:
            if count_attempts_left != 1:
                count_attempts_left -= 1
                incorrect_string.set(f"Incorrect. You have {count_attempts_left} attempts left.")
            else:
                view_pin_jail()
                return
    
def view_pin_jail():
    clear_window()
    Label(window, text="Welcome to ANZ Banking.\nPlease enter your pin to continue.", anchor="w", justify=LEFT, font="bold").grid(column=0, row=0) # Label for the text field.
    Label(window, text="You have been locked out due to multiple incorrect attempts.\nPlease wait for 2 minutes.", anchor="w", justify=LEFT).grid(column=0, row=1) # Label for the text field.

view_pin()
window.mainloop()