from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("solution")

#Set size of window
root.geometry("700x700")

voice = Button(root, text="voice", background='lightGray')
hightlight = Button(root, text="highlight", background='yellow')
li = Button(root, text="list", background='lightGray')




#textbox
inputtxt = Text(root, height = 30)

voice.grid(row=1,column=0, )
hightlight.grid(row=1,column=1)
li.grid(row=1,column=2,pady=30)
inputtxt.grid(row = 5, column =0,columnspan=3,padx=40)



# Start the GUI event loop
root.mainloop()