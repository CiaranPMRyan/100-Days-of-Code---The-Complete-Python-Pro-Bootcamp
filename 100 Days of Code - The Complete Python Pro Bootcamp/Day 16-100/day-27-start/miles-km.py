from tkinter import *

def calculate():
    if radio_state.get() == 1:
        answer = float(entry.get()) * 8 / 5
    else:
        answer = float(entry.get()) * 5 / 8
    label_answer.config(text=str(answer))

def change_layout():
    '''Change the layout of the interface depending on which conversion is being done'''
    if radio_state.get() == 2:
        label_miles.config(text="km")
        label_km.config(text="Miles")
    else:
        label_miles.config(text="Miles")
        label_km.config(text="Km")

window = Tk()
window.title("Distance Converter")
window.config(padx=20, pady=20)

radio_state = IntVar()
miles = Radiobutton(text="Miles to Km", value=1, variable=radio_state, command=change_layout)
km = Radiobutton(text="Km to Miles", value=2, variable=radio_state, command=change_layout)
miles.grid(column=0, row=0)
km.grid(column=1, row=0)

entry = Entry(width=7)
entry.insert(END, 0)
entry.grid(column=1, row=1)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=1)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=2)

label_answer = Label(text="0")
label_answer.grid(column=1, row=2)

label_km = Label(text="Km")
label_km.grid(column=2, row=2)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)

window.mainloop()