from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("solution")

#Set size of window
root.geometry("500x500")


#textbox
inputtxt = Text(root, height = 10,
                width = 25)

inputtxt.grid(row = 5, column =3)



# Start the GUI event loop
root.mainloop()

# Start the GUI event loop
root.mainloop()