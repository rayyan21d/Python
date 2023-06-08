from tkinter import *

window = Tk()
window.title("Graphical Interface")
window.minsize(width=500, height=300)


label = Label(text="I am a label", font=("Arial", 24, "bold")   )
label.pack()

label["text"] = "Edited text"

#Button
def button_clicked():
    print("I got clicked")
    label.config(text=f"{input.get()}")
    
button = Button(text="Click me to change text", command=button_clicked)
button.pack()

#Input
input = Entry(width=10)
input.pack()


window.mainloop()
