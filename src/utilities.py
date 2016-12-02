'''
Version 4
'''
from sys import platform as _platform
from os import system

def clear_screen():
    if _platform == 'linux' or _platform == 'linux2':
        # linux
        pass
    elif _platform == 'darwin':
        # MAC OS X
        system('clear')
    elif _platform == 'win32':
        # Windows
        system('cls')