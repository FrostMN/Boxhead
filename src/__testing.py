import pickle
sprites = {
    'wall': '#',
    'ground': ' ',
    'player': '■',
    'enemy': '¥',
    'gold': '*',
    'down': '»'
}
choice = {
            'black': '\033[0;30m',
            'dark_grey': '\033[1;30m',
            'red': '\033[0;31m',
            'light_red': '\033[1;31m',
            'green': '\033[0;32m',
            'light_green': '\033[1;32m',
            'brown': '\033[0;33m',
            'light_brown': '\033[1;33m',
            'blue': '\033[0;34m',
            'light_blue': '\033[1;34m',
            'purple': '\033[0;35m',
            'light_purple': '\033[1;35m',
            'cyan': '\033[0;36m',
            'light_cyan': '\033[1;36m',
            'light_grey': '\033[0;37m',
            'white': '\033[1;37m',
            'end': '\033[0m'
        }
pickle.dump(choice, open('color.dat', 'wb'))
pickle.dump(sprites, open('sprites.dat', 'wb'))
# sprites = pickle.load(open('sprites.dat', 'rb'))

# print(sprites)
import os

os.system('mode con: cols=52 lines=15')
input("Press any key to continue...")