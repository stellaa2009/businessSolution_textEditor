from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("cmndpush")

#Set size of window
root.geometry("300x300")

L1 = Label(root, text="Label" )
L2 = Label(root, text="Label" )
L3 = Label(root, text="Label" )


def change1():
	L1.config(text="updated")
	pass
	
def change2():
	L2.config(text="updated")
	pass

def change3():
	L3.config(text="updated")
	pass


B1 = Button(root, text="update", background='lightGray',command= change1)
B2 = Button(root, text="update", background='lightGray',command= change2)
B3 = Button(root, text="update", background='lightGray',command= change3)




B1.grid(row=1,column=1,)
L1.grid(row=1,column=2)
B2.grid(row=2,column=1)
L2.grid(row=2,column=2)
B3.grid(row=3,column=1)
L3.grid(row=3,column=2)



# Start the GUI event loop
root.mainloop()