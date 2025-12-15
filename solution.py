from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("solution")

#Set size of window
root.geometry("600x700")

button = Button(root, text="Red", background='red')


#textbox
inputtxt = Text(root, height = 30,
                width = 50)

button.grid(row=1,collum=2)
inputtxt.grid(row = 5, column =5,columnspan=3)



# Start the GUI event loop
root.mainloop()