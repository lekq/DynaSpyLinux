import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile

def open_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = askopenfile(
        title='Open a file',
        initialdir='/Documents',
        filetypes=filetypes)
    if filename:
    	print(filename)

# create the root window
root = tk.Tk()
root.title('DynaSpy')
root.resizable(False, False)
root.geometry("1000x600")
        

canvas = tk.Canvas(root, width=1000, height=600)

instructions = tk.Label(root, text='Select file to extract dll files', font='Raleway')
instructions.pack()

browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, font='Raleway', bg='#000000', fg='white', height=2, width=15, command=open_file)
browse_text.set('Browse')
browse_btn.pack()

filedll = ['apple', 'ball', 'cat', 'dog']
#def applytoLabel():
#    n = len(filedll)
#    element = ''
#    for i in range(n):
#        element = element + filedll[i]+'\n' 
#    return element

#filename = tk.Label(canvas, text=applytoLabel(), font= "calibri 13", bg="white")
#canvas.create_window(33,33, window=filename, anchor=tk.NW)
 
scroll_bar = tk.Scrollbar(root)
scroll_bar.pack( side = 'right', fill='both' )
   
mylist = tk.Listbox(root, yscrollcommand = scroll_bar.set , width=150, height=28)
   
for line in filedll:
    mylist.insert('end', line)
  
mylist.pack(side='left')
  
scroll_bar.config( command = mylist.yview )

# run the application
root.mainloop()
