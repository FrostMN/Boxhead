'''
Version 4
'''
from utilities import *
from movement import *

def __testing(border):
    for i in range(len(border)):
        print(' ', end='')
        for n in range(len(border[i])):
            print(border[i][n], end='')
        print('\n', end='')

def main():
    menu = Menu()
    menu_selection = menu.mainloop()
    if menu_selection == 'P':
        game = Gameplay()
        game.mainloop()
    elif menu_selection == 'H':
        score = game_score()
        __testing(score)
    elif menu_selection == 'Q':
        pass


main()