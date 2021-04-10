from tkinter import *
import json
import time
import math

window = Tk()
window.minsize('600', '300')
window.title('5 - ATM')

global datastore
datastore = json.loads(open("5-atm/atm-data.json", "r").read())

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()
    
def datastore_save():
    f = open("5-atm/atm-data.json", "w")
    f.seek(0)
    json.dump(datastore, f)


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
            home()
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
    Label(view_home_frame, text="Welcome to ANZ Banking.", anchor="w", justify=LEFT, font="bold").pack() # Label for the text field.
    Button(view_home_frame, text="1 - Display balance", command=lambda : view_1_display_balance()).pack() # Clicking this button runs the 'compute' function.
    Button(view_home_frame, text="2 - Withdraw funds", command=lambda : view_2_withdraw()).pack() # Clicking this button runs the 'compute' function.
    Button(view_home_frame, text="3 - Deposit funds", command=lambda : print()).pack() # Clicking this button runs the 'compute' function.
    Button(view_home_frame, text="4 - Display transactions", command=lambda : print()).pack() # Clicking this button runs the 'compute' function.
    Button(view_home_frame, text="9 - Return card and exit", command=lambda : print()).pack() # Clicking this button runs the 'compute' function.

    view_home_frame.pack() 

def view_1_display_balance():
    clear_window()
    view_1_display_balance_frame = Frame(window)
    Button(view_1_display_balance_frame, text="Back", command=lambda : view_home()).grid(row=0, column=0) # Clicking this button runs the 'compute' function.
    
    max_withdrawal_amount = 10**( int( math.log10(datastore["balance"]) ) )

    exact_balance_2dp = "{:.2f}".format(datastore["balance"])
    max_withdrawal_2dp = "{:.2f}".format(max_withdrawal_amount)

    display_balance = f"${exact_balance_2dp}"
    display_withdrawal = f"${max_withdrawal_2dp}"

    Label(view_1_display_balance_frame, text="Exact Balance", anchor="w", justify=LEFT, font="bold").grid(row=1, column=0) # Label for the text field.
    Label(view_1_display_balance_frame, text=display_balance, anchor="w", justify=LEFT, font="bold").grid(row=2, column=0) # Label for the text field.

    Label(view_1_display_balance_frame, text="Max Withdrawal", anchor="w", justify=LEFT, font="bold").grid(row=1, column=1) # Label for the text field.
    Label(view_1_display_balance_frame, text=display_withdrawal, anchor="w", justify=LEFT, font="bold").grid(row=2, column=1) # Label for the text field.

    view_1_display_balance_frame.pack()

def view_2_withdraw():
    print("withdraw")
    clear_window()
    view_2_withdraw_frame = Frame(window)
    Button(view_2_withdraw_frame, text="Back", command=lambda : view_home()).pack() # Clicking this button runs the 'compute' function.
    
    Label(view_2_withdraw_frame, text="Select withdrawal amount", anchor="w", justify=LEFT, font="bold").pack() # Label for the text field.

    Button(view_2_withdraw_frame, text="$10", command=lambda : withdraw(10)).pack() # Clicking this button runs the 'compute' function.
    Button(view_2_withdraw_frame, text="$20", command=lambda : withdraw(20)).pack() # Clicking this button runs the 'compute' function.
    Button(view_2_withdraw_frame, text="$50", command=lambda : withdraw(50)).pack() # Clicking this button runs the 'compute' function.
    Button(view_2_withdraw_frame, text="$100", command=lambda : withdraw(100)).pack() # Clicking this button runs the 'compute' function.
    Button(view_2_withdraw_frame, text="Other", command=lambda : view_withdraw_other_amount()).pack() # Clicking this button runs the 'compute' function.

    def withdraw(amount):
        balance = datastore["balance"]
        if amount > balance:
            view_withdraw_completion("Sorry, you have insufficient funds to complete this transaction.")
        else:
            datastore["balance"] -= amount
            datastore_save()
            view_withdraw_completion("Thank you. Please take your cash.")

    def view_withdraw_completion(status):
        clear_window()
        view_2_withdraw_completion_frame = Frame(window)
        Label(view_2_withdraw_completion_frame, text=status, anchor="w", justify=LEFT, font="bold").pack() # Label for the text field.
        Button(view_2_withdraw_completion_frame, text="Return to main menu", command=lambda : view_home()).pack() # Clicking this button runs the 'compute' function.
        view_2_withdraw_completion_frame.pack()


    view_2_withdraw_frame.pack()
    
view_home()
window.mainloop()