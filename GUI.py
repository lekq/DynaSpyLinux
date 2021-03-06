import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import Radiobutton, BooleanVar
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from DLLReader import DLLReader
import time

class GUI:

    def __init__ (self):
        self.width_screen = 1000
        self.height_screen = 600
        self.dll_reader = DLLReader ()
        # create the root window
        self.root = tk.Tk()
        self.root.title('DynaSpy')
        self.root.resizable(False, False)
        self.root.geometry(str (self.width_screen) + "x" + str (self.height_screen))

        # initialize reading mode
        self.in_single_mode = BooleanVar () 
        Radiobutton(self.root, text = 'Single mode (suitable for program with long running time)', variable = self.in_single_mode, value = True, command = self.enable_stop_button).pack()
        Radiobutton(self.root, text = 'Iterative mode (suitable for program with short running time)', variable = self.in_single_mode, value = False, command = self.disable_stop_button).pack()
        # create the canvas
        self.canvas = tk.Canvas(self.root, width = self.width_screen, height = self.height_screen)
        
        # create the instruction
        self.instructions = tk.Label(self.root, text='Select file to extract dll files', font='Raleway')
        self.instructions.pack()

        # create the scroll bar
        self.scroll_bar = tk.Scrollbar(self.root)
        self.scroll_bar.pack( side = 'right', fill='both' )

        self.dll_list = tk.Listbox(self.root, yscrollcommand = self.scroll_bar.set , width=150, height=28)
        
        self.browse_text = tk.StringVar()
        self.browse_btn = tk.Button(self.root, textvariable = self.browse_text, font='Raleway', bg='#000000', fg='white', height=2, width=18, command = self.open_file)
        self.browse_text.set('Browse')
        self.browse_btn.pack()
        
        self.export_text = tk.StringVar()
        self.export_btn = tk.Button(self.root, textvariable = self.export_text, font='Raleway', bg='#000080', fg='white', height=2, width=18, command = self.save_file)
        self.export_text.set('Save')
        self.export_btn.pack()

        self.stop_text = tk.StringVar()
        self.stop_btn = tk.Button(self.root, textvariable = self.stop_text, font='Raleway', bg='#FF0000', fg='white', height=2, width=18, command = self.stop_all_current_process)
        self.stop_text.set('Stop (only single mode)')
        self.stop_btn["state"] = "disable"
        self.stop_btn.pack ()

        self.dll_list.pack(side='left')
        self.debug_process_list = []
        self.scroll_bar.config( command = self.dll_list.yview )

    def disable_stop_button (self):
        self.stop_btn["state"] = "disable"

    def enable_stop_button (self):
        self.stop_btn["state"] = "normal"
    
    def stop_all_current_process (self):
        self.debug_process_list.append (-1)

    def handle_interactive_dll_result (self, debug_process, prev_dll_map):
        update_dll_map = prev_dll_map
        if (debug_process.pid == self.debug_process_list[-1]):
            if (self.dll_reader.check_process_alive (debug_process)):
                temp_dll_map = self.dll_reader.single_dll_reading (debug_process)
                if (prev_dll_map == None or len (temp_dll_map) > len (prev_dll_map)):
                    update_dll_map = temp_dll_map
                self.dll_list.delete (0, 'end')
                for dll in update_dll_map:
                    self.dll_list.insert('end', dll.path)
                self.root.after (100, self.handle_interactive_dll_result, debug_process, update_dll_map)


    def open_file (self):
        filetypes = (
            ('All files', '*'),
        )

        filename = askopenfilename(
            title='Open a file',
            initialdir='/Documents',
            filetypes=filetypes)
        
        if filename:
            dll_map = None
            if (self.in_single_mode.get ()):
                self.stop_all_current_process ()
                debug_process = self.dll_reader.create_debug_process (filename)
                self.debug_process_list.append (debug_process.pid)
                self.root.after (100, self.handle_interactive_dll_result, debug_process, None)
            else:
                self.stop_all_current_process ()
                dll_map = self.dll_reader.iterative_dll_reading (filename)
                self.dll_list.delete (0, 'end')
                for dll in dll_map:
                    self.dll_list.insert('end', dll.path)

    def save_file (self):
        filetypes = (
            ("Text files", "*.txt"),
        )
        filename = asksaveasfilename (
            title='Save a file',
            initialdir='/Documents',
            filetypes=filetypes)
        if (filename):
            output_file = open (filename, 'w')
            for index, value in enumerate (self.dll_list.get(0, 'end')):
                output_file.write (str (value) + '\n')
            output_file.close ()

    def run (self):
        # run the application
        self.root.mainloop ()


        





        






   






  

