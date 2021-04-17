'''md
© Will Pak Poy 2021


# Pseudocode
ANCHOR: Pseudocode

1. We request the user to enter their pin.
    1. If they get this wrong, they have three attempts, and then are sent to the "pin jail" for two minutes.
2. The user is presented with a menu.
    a.  Balance
        The user has the chance to view their balance, and see their highest allowed withdrawal amount.
        This information is pulled from the "datastore" variable, which loads it's imformation from the "atm-data.json" file.
        The highest allowded withdrawal amount is calculated by finding the highest possible power of 10 in the balance. 
    b.  Withdrawal
        The user can "withdraw" money from their account.
        This simply checks if the requesting withdrawal amount is less than the balance, and then if so subtracts the withdrawal amount from the balance
        in the datastore, and then logs this transaction using the "log_transaction" function.
        It then displays a successful completion message.
        If the user requests to withdraw another amount not listed, we check if it is a power of 10, and then follow the steps above, but using a custom number.


'''
from tkinter import *
import json
import time
import math

# Tkinter initialisation and boilerplate
window = Tk()
window.minsize('600', '300')
window.title('5 - ATM')

# This declares "datastore" to be global, and loads information from the "atm-data.json" file to be used by the application.
global datastore
datastore = json.loads(open("5-atm/atm-data.json", "r").read())

# This function clears the window to replace a view.
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

# This function helps convert sets into objects so they can be stored in the JSON file.
def serialize_sets(obj):
    if isinstance(obj, set):
        return list(obj)

    return obj

# This function saves the contents of the "datastore" variable back into the JSON file (if we have mutated the data).
def datastore_save():
    f = open("5-atm/atm-data.json", "w")
    f.seek(0)
    json.dump(datastore, f, default=serialize_sets)

# This function logs a transaction that a user has peformed into the "datastore" variable.
def log_transaction(type, amount):
    new = {"type": type, "amount": amount}
    datastore["transactions"].append(new)

# ANCHOR: Pin
def view_pin():
    clear_window()
    view_pin_frame = Frame(window)
    user_entered_pin = IntVar() # Holds whatever the user has typed into the entry field.
    count_attempts_left = 3 # A count of the incorrect pin attempts.
    incorrect_string = StringVar() # To hold the status of the attempt, eg "Incorrect pin".

    Label(view_pin_frame, text="Welcome to ANZ Banking.\nPlease enter your pin to continue.", anchor="w", justify=LEFT, font="bold").pack()
    Entry(view_pin_frame, textvariable=user_entered_pin).pack() # Binds to "user_entered_pin"
    Button(view_pin_frame, text="Login", command=lambda : validate()).pack() # Clicking this button runs the validate pin function

    Label(view_pin_frame, textvariable=incorrect_string, anchor="w", justify=LEFT).pack() # Simply displays the contents of the "incorrect_string" variable.

    def validate():
        nonlocal count_attempts_left # lets us mutate the "count_attempts_left" defined above
        if datastore["pin"] == user_entered_pin.get():
            home() # if the pin is correct, we send the user to the home view.
        else:
            if count_attempts_left != 1: # if their attempts are not equal to 1 (meaning they have none left)
                count_attempts_left -= 1 # we increment the attempts amount
                incorrect_string.set(f"Incorrect. You have {count_attempts_left} attempts left.") # and alert the user
            else:
                view_pin_jail() # else, we send the user to the pin jail for 120 seconds.
    view_pin_frame.pack()

# ANCHOR: Pin: Jail
def view_pin_jail():
    clear_window()
    count_jail_timer = 5 # we have to make our own timer instead of using time.sleep() to prevent tkinter synchronous code blocking
    view_pin_jail_frame = Frame(window)
    Label(view_pin_jail_frame, text="Welcome to ANZ Banking.", anchor="w", justify=LEFT, font="bold").pack() 
    Label(view_pin_jail_frame, text="You have been locked out due to multiple incorrect attempts.\nPlease wait for 2 minutes.", anchor="w", justify=LEFT).pack()
    continue_button = Button(view_pin_jail_frame, text="Continue", command=lambda : view_pin_frame())
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

# ANCHOR: Home
def view_home():
    clear_window()
    view_home_frame = Frame(window)
    Label(view_home_frame, text="Welcome to ANZ Banking.", anchor="w", justify=LEFT, font="bold").pack()
    Button(view_home_frame, text="1 - Display balance", command=lambda : view_1_display_balance()).pack() 
    Button(view_home_frame, text="2 - Withdraw funds", command=lambda : view_2_withdraw()).pack() 
    Button(view_home_frame, text="3 - Deposit funds", command=lambda : view_3_deposit()).pack() 
    Button(view_home_frame, text="4 - Display transactions", command=lambda : view_4_transactions()).pack() 
    Button(view_home_frame, text="9 - Return card and exit", command=lambda : window.quit()).pack() 

    view_home_frame.pack() 

# ANCHOR: 1. Balance
def view_1_display_balance():
    clear_window()
    view_1_display_balance_frame = Frame(window)
    Button(view_1_display_balance_frame, text="Back", command=lambda : view_home()).grid(row=0, column=0) # Universal back button to home view.
    
    max_withdrawal_amount = (datastore["balance"] // 10) * 10 # calculate the max withdrawal amount, by finding the highest power of 10 possible in the balance.

    # format the two numbers with two decimal points
    exact_balance_2dp = "{:.2f}".format(datastore["balance"]) 
    max_withdrawal_2dp = "{:.2f}".format(max_withdrawal_amount)

    # add the dollar sign
    display_balance = f"${exact_balance_2dp}"
    display_withdrawal = f"${max_withdrawal_2dp}"

    # display these values
    Label(view_1_display_balance_frame, text="Exact Balance", anchor="w", justify=LEFT, font="bold").grid(row=1, column=0) 
    Label(view_1_display_balance_frame, text=display_balance, anchor="w", justify=LEFT, font="bold").grid(row=2, column=0) 

    Label(view_1_display_balance_frame, text="Max Withdrawal", anchor="w", justify=LEFT, font="bold").grid(row=1, column=1) 
    Label(view_1_display_balance_frame, text=display_withdrawal, anchor="w", justify=LEFT, font="bold").grid(row=2, column=1) 

    view_1_display_balance_frame.pack()

# ANCHOR: 2. Withdraw
def view_2_withdraw():
    clear_window()
    view_2_withdraw_frame = Frame(window)
    Button(view_2_withdraw_frame, text="Back", command=lambda : view_home()).pack()  # universal back button
    
    Label(view_2_withdraw_frame, text="Select withdrawal amount", anchor="w", justify=LEFT, font="bold").pack() # title

    # let the user choose how much they would like to withdraw
    Button(view_2_withdraw_frame, text="$10", command=lambda : withdraw(10)).pack() 
    Button(view_2_withdraw_frame, text="$20", command=lambda : withdraw(20)).pack() 
    Button(view_2_withdraw_frame, text="$50", command=lambda : withdraw(50)).pack() 
    Button(view_2_withdraw_frame, text="$100", command=lambda : withdraw(100)).pack() 
    Button(view_2_withdraw_frame, text="Other", command=lambda : view_withdraw_other()).pack() # if they select this, they are sent to the "other" view.

    # This function updates the user's actual balance.
    def withdraw(amount):
        balance = datastore["balance"]
        if amount > balance: # insufficient funds
            view_withdraw_completion("Sorry, you have insufficient funds to complete this transaction.") # alert the user through the "completion" view.
        else:
            datastore["balance"] -= amount # subtract the amount from the balance
            log_transaction(type="withdraw", amount=amount) # log the transaction
            datastore_save() # save the datastore to the JSON file
            view_withdraw_completion("Thank you. Please take your cash.") # alert the user through the "completion" view.

    # ANCHOR: 2.1. Withdraw: Completion
    def view_withdraw_completion(status):
        clear_window()
        view_withdraw_completion_frame = Frame(window)
        Label(view_withdraw_completion_frame, text=status, anchor="w", justify=LEFT, font="bold").pack() 
        Button(view_withdraw_completion_frame, text="Return to main menu", command=lambda : view_home()).pack() 
        view_withdraw_completion_frame.pack()

    # ANCHOR: 2.2. Withdraw: Other
    def view_withdraw_other():
        clear_window()
        view_withdraw_other_frame = Frame(window)
        requesting_withdrawal_amount = IntVar() # the amount the user would like to withdraw
        status = StringVar() # the status of the withdrawal

        Label(view_withdraw_other_frame, text="Withdraw another amount", anchor="w", justify=LEFT, font="bold").pack() 
        Entry(view_withdraw_other_frame, textvariable=requesting_withdrawal_amount).pack()
        Button(view_withdraw_other_frame, text="Submit", command=lambda : check_other_amount(requesting_withdrawal_amount.get())).pack() 
        Label(view_withdraw_other_frame, textvariable=status, anchor="w", justify=LEFT, font="bold").pack() 

        def check_other_amount(amount):
            if amount % 10 == 0: # check if amount is a power of 10, if so pass to withdraw function to check balance and withdraw.
                withdraw(amount)
            else:
                status.set("Number must be a multiple of 10") # alert the user that their number is not a power of 10.
        view_withdraw_other_frame.pack()



    view_2_withdraw_frame.pack()

# ANCHOR: 3. Deposit
def view_3_deposit():
    clear_window()
    view_3_deposit_frame = Frame(window)

    deposit_amount = DoubleVar() # the depositing amount, stored in a float.
    status = StringVar() # the status of the deposit

    Button(view_3_deposit_frame, text="Back", command=lambda : view_home()).pack() 
    Label(view_3_deposit_frame, text="Please enter the amount in which you would like to deposit.", anchor="w", justify=LEFT, font="bold").pack() 
    Entry(view_3_deposit_frame, textvariable=deposit_amount).pack()
    Button(view_3_deposit_frame, text="Submit", command=lambda : deposit_monies(deposit_amount.get())).pack() 
    Label(view_3_deposit_frame, textvariable=status, anchor="w", justify=LEFT, font="bold").pack() 

    def deposit_monies(amount):
        datastore["balance"] += amount # update datastore with added amount
        log_transaction(type="deposit", amount=amount) # log the transaction
        datastore_save() # save the datastore
        status.set(f"{amount} dollars has been deposited into your account.") # alert the user

    view_3_deposit_frame.pack() 
    
# ANCHOR: 4. Transactions
def view_4_transactions():
    clear_window()
    view_4_transactions_frame = Frame(window)
    Button(view_4_transactions_frame, text="Back", command=lambda : view_home()).grid(column=0, row=0)  # universal back button

    Label(view_4_transactions_frame, text="Type", font="bold").grid(row=1, column=1) # column in table for type of transaction (either withdrawal or deposit)
    Label(view_4_transactions_frame, text="Amount", font="bold").grid(row=1, column=2) # column in table for amount of money

    transactions = datastore["transactions"] # gets the transactions from the datastore.
    item_loop = 0 # we use a while loop instead of a for-loop to allow for us to access the item's index

    while item_loop < len(transactions):
        item = transactions[item_loop] # the current item being looped over in the transactions list
        amount_2dp = "{:.2f}".format(item["amount"]) # convert to 2dp


        Label(view_4_transactions_frame, text=item["type"].title(), font="bold").grid(row=item_loop+2, column=1) # type of transaction
        Label(view_4_transactions_frame, text=f"${amount_2dp}", font="bold").grid(row=item_loop+2, column=2) # amount, with dollar symbol


        item_loop += 1 # increment the item loop
    view_4_transactions_frame.pack()

view_home()
window.mainloop()