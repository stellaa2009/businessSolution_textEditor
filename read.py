from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("read")

#Set size of window
root.geometry("300x300")



def writing():
	txt = inputtxt.get("1.0",END)
	with open("demofile.txt", "w") as f:
  		f.write(txt)
	pass

def reading():
	with open("demofile.txt","r") as f:
		content = f.read()
		print(content)

inputtxt = Text(root, height = 10,width=30)
writ = Button(root, text="write file", background='lightGray',command= writing)
read = Button(root, text="read file", background='lightGray',command=reading)


inputtxt.grid(row=1,column=1)
writ.grid(row=2,column=1)
read.grid(row=3,column=1)

root.mainloop()