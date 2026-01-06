from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("command push")

#Set size of window
root.geometry("700x700")

voice = Button(root, text="change me.", background='lightGray')
txt =Text(root, height 5, width 52)


voice.grid(row=1,column=1, )
txt.grid(row=1,column=2)




# Start the GUI event loop
root.mainloop()