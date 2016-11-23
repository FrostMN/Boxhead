from sys import platform as _platform
from os import system
from time import sleep

class Setup:
    def __init__(self):
        pass

    def floor_size(self, size):
        sizes = {
            'Small': [53, 15],
            'Medium': [70, 20],
            'Large' : [105, 40]
        }
        return sizes[size]

    def floor_difficulty(self, challenge):
        level = {
            'Easy'  : [2, 3],
            'Medium': [3, 3],
            'Hard'  : [4, 3]
        }
        return level[challenge]

    def clear_screen(self):
        if _platform == 'linux' or _platform == 'linux2':
            # linux
            pass
        elif _platform == 'darwin':
            # MAC OS X
            system('clear')
        elif _platform == 'win32':
            # Windows
            system('cls')

    def settings(self):
        system('mode con: cols=54 lines=20')
        # self.clear_screen()
        # print('BoxHead')
        # size_input = input('Size: ')
        # self.size =  self.floor_size(size_input)
        # difficulty_input = input('Difficulty: ')
        # self.difficulty = self.floor_difficulty(difficulty_input)
        # return self.size, self.difficulty
        return self.floor_size('Small'), self.floor_difficulty('Easy')