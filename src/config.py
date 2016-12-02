'''
Version 4
'''
from os import system

settings = {
    'width'     : 104,
    'height'    : 30
}
system('title Boxhead')
system('mode con: cols=' + str(settings['width'] + 2) + ' lines=' + str(settings['height'] + 1))
