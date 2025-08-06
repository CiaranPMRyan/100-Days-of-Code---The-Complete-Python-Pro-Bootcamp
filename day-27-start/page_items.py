from tkinter import *

# Creating a new window and configuring it

window = Tk()
window.title("Widget examples")
window.minsize(width=500, height=500)

# Labels

label = Label(text="This is the old text") # Put text on a label. Lots of other stuff can be config'd
label.config(text="This is the new text") # Config is used to change existing parameters
label.pack() # Pask is needed to display the widget. It also has a ton of options

# Buttons

def action():
    print("Do something")

# This button calls the above function when clicked using the command param.
button = Button(text="Click Me", command=action)
button.pack()

# Entries

entry = Entry(width=30)
# Add some starter text
entry.insert(END, string="Some starter text")
# Get the text from the entry box
print(entry.get()) # The .get() can be assigned to a var and used elsewhere
entry.pack()

# Text box

text = Text(height=5, width=30)
text.focus() # Puts the cursor in the box by default
# Add some default text.
text.insert(END, "Please write the stuff in here")
# Get a character from the box
print(text.get("1.0")) # Line 1, char 0
text.pack()

# Spinbox

def spinbox_used():
    # Gets the current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10 , width=5, command=spinbox_used)
spinbox.pack()

# Scale

def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Check Button

def button_used():
    # Prints 1 is On button checked, otherwise 0
    print(checked_state.get())

# Var to hold the state, 0 or 1.
checked_state = IntVar() # IntVar() is a special int for bool, I think
check_button = Checkbutton(text="Is on?", variable=checked_state, command=button_used)
checked_state.get()
check_button.pack()

# Radio Button

def radio_used():
    print(radio_state.get())

# Var to hold the state, 0 or 1.
radio_state = IntVar() # IntVar() is a special int for bool, I think
radio_button_01 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radio_button_02 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radio_button_01.pack()
radio_button_02.pack()

# Listbox

def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Banana", "Pear", "Orange"] # List to populate the box

for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop() # Keeps the window open