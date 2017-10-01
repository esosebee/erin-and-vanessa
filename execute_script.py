import os, subprocess, sys

# Default file names and paths if no arguments given
path = os.getcwd()
data_path = os.path.join(path, 'Data')
default_training_path = os.path.join(data_path, 'training.csv')
default_testing_path = os.path.join(data_path, 'testing.csv')

def install_libraries():
    '''
    Install libraries that are not part of Python's standard library.
    '''
    subprocess.call(['pip', 'install', 'scipy'])

def parse_args(args):
    '''
    If command line input is valid, then parses the args and 
    gets the necessary information from them. Otherwise, displays
    a usage statement and exits the program.
    '''
    if '-train' in args and '-test' in args:
        training_filename = args['-train']
        testing_filename = args['-test']
        return training_filename, testing_filename
    else:
        print_usage()
        sys.exit(0)

def build_call_string(argv):
    if len(argv) < 1:
        print 'use defaults'
# Install libraries that are not part of Python's standard library
install_libraries()

# Build string to call main script with
call_string = build_call_string(sys.argv[1:])

# def get_args(argv):
#     '''
#     Get options from command line input.
#     '''
#     opts = {}
#     while argv:
#         if argv[0][0] == '-':
#             opts[argv[0]] = argv[1]
#         argv = argv[1:]
#     return opts


# def build_call_string():
#     if len(sys.argv) == 1:
#         return 'python src/main.py -train ' + default_training + ' -test ' + default_testing
#     # myargs = get_args(sys.argv[1:])

# print call_string

# Call 