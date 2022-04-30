from DLLReader import DLLReader
from GUI import GUI
import os
import math
from argparse import ArgumentParser 

parser = ArgumentParser()
parser.add_argument('-file', action='store', dest='file_path', help='Specify absolute path to executable file')
parser.add_argument('-output', action='store', dest='output', help='Specify absolute path to output file')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

parser.add_argument('-single', action='store_true', default=False, dest='single_read', help='Switch to single mode of DLL reader')
parser.add_argument('-iterative', action='store_false', default=False, dest='single_read', help='Swich to iterative mode of DLL reader')
parser.add_argument('-gui', action='store_true', default=False, dest='gui_mode', help='Use DynaSpy with GUI')

parser.add_argument('-threshold_to_break', type=int, help = 'If the program did not load any new library after this number of checks, it will ask you whether you want to continue. Only useful in single mode. Default value is infinite')

parser.set_defaults (single_read = False)
parser.set_defaults (gui_mode = False)
parser.set_defaults (threshold_to_break = math.inf)

argument = parser.parse_args()
if (argument.gui_mode):
    app = GUI ()
    app.run ()
else:
    dll_reader = DLLReader ()
    filename = argument.file_path
    output_file = argument.output
    threshold_to_break = argument.threshold_to_break
    dll_map = None
    if (filename):
        if (os.path.exists (filename)):
            if (argument.single_read):
                debug_process = dll_reader.create_debug_process (filename)
                count_similar = 0
                while (dll_reader.check_process_alive (debug_process)):
                    temp_dll_map = dll_reader.single_dll_reading (debug_process)
                    if (count_similar >= threshold_to_break):
                        continue_program = input ('Your analyzed program did not load any new library for a while. Want to keep recording? [Y/N]').upper ()
                        while (continue_program not in ['Y', 'N']):
                            continue_program = input ('Your analyzed program did not load any new library for a while. Want to keep recording? [Y/N]').upper ()
                        if (continue_program == 'Y'):
                            count_similar = 0
                        else:
                            break
                    if (dll_map is None or (temp_dll_map is not None and len (temp_dll_map) > len (dll_map))):
                        dll_map = temp_dll_map
                        count_similar = 0
                    else:
                        count_similar += 1
                if (output_file):
                    file = open (output_file, 'w')
                    for dll in dll_map:
                        file.write (str (dll.path) + '\n')
                    file.close ()
                else:
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






