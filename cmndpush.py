from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("cmndpush")

#Set size of window
root.geometry("700x700")

L = Label(root, text="Label" )

def changeTitle():
	Word = T.get("1.0", END)
	L.config(text=Word)
	pass
	

T =Text(root, height=5, width=52)
B = Button(root, text="change me.", background='lightGray',command= changeTitle)



B.grid(row=1,column=1,)
T.grid(row=1,column=2)
L.grid(row=1,column=3)



# Start the GUI event loop
root.mainloop()