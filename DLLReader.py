import psutil
import subprocess

class DLLReader:
    def check_process_alive (self, process):
        return process.poll () is None
        
    def create_debug_process (self, path_to_executable_file):
        process =  psutil.Popen([path_to_executable_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        process.suspend ()
        return process
    def single_dll_reading (self, process):
        if (self.check_process_alive (process)):
            dll_maps = process.memory_maps ()
            process.resume ()
            process.suspend ()
            return dll_maps
        return None
    
    def iterative_dll_reading (self, path_to_executable_file):
        # repeat single reading for 10 times
        num_iteration = 10
        final_dll_map = None
        for iter in range (num_iteration):
            process = self.create_debug_process (path_to_executable_file)
            while (self.check_process_alive (process)):
                temp_dll_map = self.single_dll_reading (process)
                if (final_dll_map is None or (temp_dll_map is not None and len (temp_dll_map) > len (final_dll_map))):
                    final_dll_map = temp_dll_map
        return final_dll_map
            


        

