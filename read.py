from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("read")

#Set size of window
root.geometry("300x300")

inputtxt = Text(root, height = 30)
write = Button(root, text="write file", background='lightGray',command=)
read = Button(root, text="read file", background='lightGray')
