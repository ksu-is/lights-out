'''
Error helpers which will be shared between many files.
All custom error handling functions will be maintained
inside this file, and then other files will import them
from here. Most of these will essentially be setting
formats for custom print messages for error and exception
handling.
'''

import traceback

def causeError(error_type_string,error_desc_string):
    tmp_string = '''
    ====================================================\n\n
    Error! An expected problem occurred!\n\n
    ----------------------------------------------------\n
    Type: '''+error_type_string+'''\n
    ----------------------------------------------------\n
    Description: '''+error_desc_string+'''\n
    ----------------------------------------------------\n
    Full traceback: '''+traceback.format_exc()+'''\n
    ====================================================
    '''
    print(tmp_string)

    exit()
    