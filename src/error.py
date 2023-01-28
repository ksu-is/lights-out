'''
Error helpers which will be shared between many files.
All custom error handling functions will be maintained
inside this file, and then other files will import them
from here. Most of these will essentially be setting
formats for custom print messages for error and exception
handling.
'''

import traceback

ActionLog = []

def causeError(error_type_string,error_desc_string):
    '''
    This function will print out a formatted message describing an error with a given error type and description,
    along with the full traceback of the problem. This makes the usual traceback message much more visible in a terminal.
    This function should be used in combination with try: and except: blocks, where a section of code is included
    in the try: block, and then this function is called in the except: block. This allows for showing clearly
    formatted errors with known names and descriptions, where errors may be expected.\n
    IMPORTANT: This is only meant for making errors easier to understand and find. This does not handle errors
    on its own, or do anything to resolve them.
    '''
    tmp_string = '''
    Error! An expected problem occurred!\n\n
------------------------------------------------------------------------------------------\n
Type: '''+error_type_string+'''\n
------------------------------------------------------------------------------------------\n
Description: '''+error_desc_string+'''\n
------------------------------------------------------------------------------------------\n
Full traceback: '''+traceback.format_exc()+'''\n==========================================================================================\n==========================================================================================\n==========================================================================================
'''

    exitSafely(tmp_string)

def testError():
    '''
    This is a function to be used when testing the implementation of the "try: (code) except: causeError" setup
    in any given file, class, or function. This is not to be included in any final or production version, and should
    be removed once testing is complete.\n
    IMPORTANT: This is for testing purposes only, and should be removed once testing is complete!
    '''
    raise Exception("This is a testing error, thrown by the testError function in error.py. You should be expecting to see this, as part of an error.py output message. If you are not, it means that this was left someplace where it shouldn't be, and it should be removed")

def exitSafely(error_string=""):
    '''
    This is the exit function which should be used for ALL instances of closing the application, for ANY reason.
    \nThe reason is simple enough: by only closing with a specific function, any necessary closing operations can be done every time,
    while also giving the opportunity to print out the action log.
    '''

    log_string = '''\n==========================================================================================\n==========================================================================================\n==========================================================================================\n\n
    Action Log: These are the events logged by the application, before close.\n
    '''

    for j in ActionLog:
        log_string += "\n------------------------------------------------------------------------------------------\n"
        log_string += j
        log_string += "\n------------------------------------------------------------------------------------------"

    log_string += '''\n==========================================================================================\n==========================================================================================\n=========================================================================================='''

    print(log_string)

    print(error_string)

    exit()

def addToActionLog(action_string):
    ActionLog.append(action_string)


def clearActionLog():
    ActionLog = []

