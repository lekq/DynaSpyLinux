from DLLReader import DLLReader
from GUI import GUI
import os
from argparse import ArgumentParser 

parser = ArgumentParser()
parser.add_argument('-file', action='store', dest='file_path', help='Specify absolute path to executable file')
parser.add_argument('-output', action='store', dest='output', help='Specify absolute path to output file')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

parser.add_argument('-single', action='store_true', default=False, dest='single_read', help='Switch to single mode of DLL reader')
parser.add_argument('-iterative', action='store_false', default=False, dest='single_read', help='Swich to iterative mode of DLL reader')
parser.add_argument('-gui', action='store_true', default=False, dest='gui_mode', help='Use DynaSpy with GUI')

parser.set_defaults (single_read = False)
parser.set_defaults (gui_mode = False)

argument = parser.parse_args()
if (argument.gui_mode):
    app = GUI ()
    app.run ()
else:
    dll_reader = DLLReader ()
    filename = argument.file_path
    output_file = argument.output
    dll_map = None
    if (filename):
        if (os.path.exists (filename)):
            if (argument.single_read):
                debug_process = dll_reader.create_debug_process (filename)
                while (dll_reader.check_process_alive (debug_process)):
                    temp_dll_map = dll_reader.single_dll_reading (debug_process)
                    if (dll_map is None or (temp_dll_map is not None and len (temp_dll_map) > len (dll_map))):
                        dll_map = temp_dll_map
                    for dll in dll_map:
                        print (dll.path)

            else:
                dll_map = dll_reader.iterative_dll_reading (filename)

            if (output_file):
                file = open (output_file, 'w')
                for dll in dll_map:
                    file.write (str (dll.path) + '\n')
                file.close ()
            else:
                for dll in dll_map:
                    print (dll.path)
        else:
            print ('Cannot find your executable file')
    else:
        print ('Please specify absolute path to your executable file or use GUI mode')






