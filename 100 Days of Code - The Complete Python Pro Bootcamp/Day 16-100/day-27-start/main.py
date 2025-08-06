from tkinter import * # Using the asterisk means we bring in all Classes from Tkinter. Means we don't have to type
                      # tkinter.button() etc each time we want to use a class.
                      # Saves on typing when using a lot of classes

def button_clicked():
    my_label.config(text=input.get())

window = Tk()
window.title("My first Interface")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

my_label = Label(text="My Label", font="Arial")
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


# Button

button2 = Button(text="New Button")
button2.grid(column=2, row=0)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Entry

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()