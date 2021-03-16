import tkinter as tk
from random import randint

window = tk.Tk()
window.minsize('600', '300')
window.title('1 - Loop')

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def loop():
    clear_window()
    number_to_guess = randint(1,100)
    print(number_to_guess)


loop()