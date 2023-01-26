'''
Helper functions which are not specific to any one section of the program.
Math functions, string manipulation functions, etc.
'''

def clamp(value,minimum,maximum):
    return (max(minimum,min(value,maximum)))