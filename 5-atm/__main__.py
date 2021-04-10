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
    view_pin_frame = Frame(window)
    user_entered_pin = IntVar()
    count_attempts_left = 3
    incorrect_string = StringVar()

    Label(view_pin_frame, text="Welcome to ANZ Banking.\nPlease enter your pin to continue.", anchor="w", justify=LEFT, font="bold").pack() # Label for the text field.
    Entry(view_pin_frame, textvariable=user_entered_pin).pack()
    Button(view_pin_frame, text="Login", command=lambda : validate()).pack() # Clicking this button runs the 'compute' function.

    Label(view_pin_frame, textvariable=incorrect_string, anchor="w", justify=LEFT).pack()# Label for the text field.

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
    view_pin_frame.pack()
    
def view_pin_jail():
    clear_window()
    count_jail_timer = 5 # we have to make our own timer instead of using time.sleep() to prevent tkinter synchronous code blocking
    view_pin_jail_frame = Frame(window)
    Label(view_pin_jail_frame, text="Welcome to ANZ Banking.", anchor="w", justify=LEFT, font="bold").pack() # Label for the text field.
    Label(view_pin_jail_frame, text="You have been locked out due to multiple incorrect attempts.\nPlease wait for 2 minutes.", anchor="w", justify=LEFT).pack() # Label for the text field.
    continue_button = Button(view_pin_jail_frame, text="Continue", command=lambda : view_pin_frame()) # Clicking this button runs the 'compute' function.
    def update_clock():
        nonlocal count_jail_timer
        if count_jail_timer > 0:
            time.sleep(1000)
            count_jail_timer += 1
            update_clock()
        else:
            continue_button.pack()
    view_pin_jail_frame.pack()
    update_clock()

def view_home():
    clear_window()
    view_home_frame = Frame(window)
    
view_pin()
window.mainloop()