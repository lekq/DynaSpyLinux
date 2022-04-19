import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename
import logic

# create the root window
root = tk.Tk()
root.title('DynaSpy')
root.resizable(False, False)
root.geometry("1000x600")
        

canvas = tk.Canvas(root, width=1000, height=600)

instructions = tk.Label(root, text='Select file to extract dll files', font='Raleway')
instructions.pack()

scroll_bar = tk.Scrollbar(root)
scroll_bar.pack( side = 'right', fill='both' )
   
mylist = tk.Listbox(root, yscrollcommand = scroll_bar.set , width=150, height=28)

def open_file():
    filetypes = (
        ('All files', '*'),
    )

    filename = askopenfilename(
        title='Open a file',
        initialdir='/Documents',
        filetypes=filetypes)
    if filename:
    	a = logic.iterative_read (filename, 10) # please replace it with your program here
    	mylist.delete (0, 'end')
    	for dll in a:
    	    mylist.insert('end', dll.path)

browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, font='Raleway', bg='#000000', fg='white', height=2, width=15, command=open_file)
browse_text.set('Browse')
browse_btn.pack()

  
mylist.pack(side='left')
  
scroll_bar.config( command = mylist.yview )

# run the application
root.mainloop()
