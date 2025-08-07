from tkinter import *

from pandas.core.computation.align import align_terms

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = entry_web.get()
    user = entry_user.get()
    password = entry_password.get()
    #print(web)
    with open("data.txt", "a") as f:
         f.write(f"{web} | {user} | {password}\n")

    entry_web.delete(0, END)
    entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# logo in col 1, row 0

# Logo graphic
canvas = Canvas(width=200, height=200, highlightthickness=2, highlightbackground="black")
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1, row=0)

# Label1, col 0, row 1,
label_web = Label(text="Website:")
label_web.grid(column=0, row=1)

#Entry1 col 1, row 1, colspan 2

entry_web = Entry(width=35)
entry_web.grid(column=1, row=1, columnspan=2)
entry_web.focus()

# Label2, col 0, row 2,
label_user = Label(text="Email/Username:")
label_user.grid(column=0, row=2)

# Entry2 col 1, row 2, colspan 2
entry_user = Entry(width=35)
entry_user.grid(column=1, row=2, columnspan=2)
entry_user.insert(0, "myemail@email.com")


# Label3, col 0, row 3,
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Entry3 col 1, row 3, colspan 2, smaller width
entry_password = Entry(width=20, show="*")
entry_password.grid(column=1, row=3)

# Button 1 col 3, row 3
button_gen = Button(text="Generate Password")
button_gen.grid(column=2, row=3)

# Button 2 col 1, row 4, colspan 2
button_add = Button(text="Add", width=30, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()