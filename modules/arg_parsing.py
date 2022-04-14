"""
Version 1.0 log
Apr 13th
++  Bascial functions to the program:
+       function to read user input string from CMD (to store applicaiton path)
+       function to store user input numerical value from CMD
+       function to switch user input boolean value from CMD
+       funciton to append user input item from CMD to a list 
+       function to check program version from CMD
+       function to write to a txt file

++  Testing
+       tested two input functions
+       tested two boolean switches
+       tested append function
+       tested output function
+       tested version check
"""

import argparse
# from ConfigParser import ConfigParser
# import shlex

parser = argparse.ArgumentParser()

# Store the location of the file
parser.add_argument('-file', action='store', dest='file_path',
                    help='Store a file location')

# Store numerical value
parser.add_argument('-c', action='store_const', dest='constant_value',
                    const='value-to-store',
                    help='Store a constant value')

# Switch boolean
parser.add_argument('-true', action='store_true', default=False,
                    dest='boolean_switch',
                    help='Set a switch to true')
parser.add_argument('-false', action='store_false', default=False,
                    dest='boolean_switch',
                    help='Set a switch to false')

# Append item into list
parser.add_argument('-append', action='append', dest='collection',
                    default=[],
                    help='Add repeated values to a list',
                    )

# Check version (just for fun)
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

# Load and write to txt files
# parser.add_argument('-inputFile', metavar='in-file', type=argparse.FileType('rt'),
#                     help = 'Load content from a txt file')
parser.add_argument('-output', metavar='out-file', type=argparse.FileType('wt'),
                    help = 'Write output to a txt file')

# debug
# parser.add_argument('-A', action='append_const', dest='const_collection',
#                     const='value-1-to-append',
#                     default=[],
#                     help='Add different values to list')
# parser.add_argument('-B', action='append_const', dest='const_collection',
#                     const='value-2-to-append',
#                     help='Add different values to list')

results = parser.parse_args()
print ('File_path     =', results.file_path)
print ('constant_value   =', results.constant_value)
print ('boolean_switch   =', results.boolean_switch)
print ('collection       =', results.collection)
# print ('const_collection =', results.const_collection)

try:
    results = parser.parse_args()
    #print ('Input file:', results.i)
    print ('Output file:', results.output)
except IOError as msg:
    parser.error(str(msg))