import tkinter as tk
from tkinter import messagebox
import random#
computer_number=2
#computer_number=random.randint(0,50)
user_number=None
#functions
def guess_function():
    user_number=int(guess_entry.get())
    if user_number==computer_number:
        messagebox.showinfo("Congratulations!","You guessed the right number")

    else:
        messagebox.showerror("Wrong!","Try again")


#window
window=tk.Tk()
window.title=("Guess the number game", 12)
window.geometry("500x500")

#label
welcomelabel=tk.Label(window, text="Welcome to our game!", font=("Arial", 16),fg="black")
welcomelabel.grid(row=1, column=2, pady=50)

#name label
username=tk.Label(window, text="What is your name?", font=("arial", 12), fg="black")
username.grid(row=2, column=1)

#name entry
name_entry=tk.Entry(window,bd=2)
name_entry.grid(row=3, column=1)

#ok button
ok=tk.Button(window, text="OK", font=("Arial", 12), fg="black", bd=2)
ok.grid(row=3, column=2)

#take a guess label
guess=tk.Label(window, text="Take a guess between 0 to 50", font=("arial", 12), fg="black")
guess.grid(row=4, column=1,pady=50)

#guess entry
guess_entry=tk.Entry(window,bd=2)
guess_entry.grid(row=4, columnspan=3)

#guess button
guess_button=tk.Button(window, text="Guess", font=("Arial", 12), fg="black", bd=2, command=guess_function )
guess_button.grid(row=4, column=3)




window.mainloop()