import psutil
import subprocess

def single_read (path_to_executable_file):
    process =  psutil.Popen([path_to_executable_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    process.suspend ()
    memory_maps = None
    while (process.poll () is None):
        memory_maps = process.memory_maps ()
        process.suspend ()
        process.resume ()
    return memory_maps

def iterative_read (path_to_executable_file, num_iteration):
    memory_maps = None
    for iteration in range (num_iteration):
        temp_maps = single_read (path_to_executable_file)
        if (memory_maps == None or (temp_maps != None and len (temp_maps) > len (memory_maps))):
            memory_maps = temp_maps
    return memory_maps
    
a = iterative_read ('./temp', 10) # please replace it with your program here
for dll in a:
    print (dll.path)

