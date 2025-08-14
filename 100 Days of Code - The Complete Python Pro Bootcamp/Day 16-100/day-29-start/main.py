from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def pass_generator():

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = entry_web.get()
    user = entry_user.get()
    password = entry_password.get()

    # Dictionary creation for json writing
    new_data = {
        web: {
            "user" : user,
            "password" : password,
        }

    }

    #get len of inputs, check if they're not zero, only then can I proceed to the rest.
    if len(web) == 0 or len(password) == 0:
        messagebox.showerror(title="STOP", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as f:# Open the file in read mode
                data = json.load(f)  # Read in the existing data
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)  # Add new data to the existing data
            with open("data.json", "w") as f: #Open the file in write mode
                json.dump(data, f, indent=4) #Write all the data back to the file
        finally:
            entry_web.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# logo in col 1, row 0

# Logo graphic
canvas = Canvas(width=200, height=200, highlightthickness=0, highlightbackground="black")
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1, row=0)

# Label1, col 0, row 1,
label_web = Label(text="Website:")
label_web.grid(column=0, row=1, sticky="w")

#Entry1 col 1, row 1, colspan 2

entry_web = Entry(width=30)
entry_web.grid(column=1, row=1, columnspan=2, sticky="we")
entry_web.focus()

# Label2, col 0, row 2,
label_user = Label(text="Email/Username:")
label_user.grid(column=0, row=2, sticky="w")

# Entry2 col 1, row 2, colspan 2
entry_user = Entry(width=30)
entry_user.grid(column=1, row=2, columnspan=2, sticky="we")
entry_user.insert(0, "myemail@email.com")


# Label3, col 0, row 3,
label_password = Label(text="Password:")
label_password.grid(column=0, row=3, sticky="w")

# Entry3 col 1, row 3, colspan 2, smaller width
entry_password = Entry(width=15, show="*")
entry_password.grid(column=1, row=3, sticky="we")

# Button 1 col 3, row 3
button_gen = Button(text="Generate Password", command=pass_generator)
button_gen.grid(column=2, row=3)

# Button 2 col 1, row 4, colspan 2
button_add = Button(text="Add", width=44, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()