import tkinter

window = tkinter.Tk()
window.title("Graphical Interface")
window.minsize(width=500, height=300)


label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold")   )
label.pack(expand="true")

window.mainloop()
