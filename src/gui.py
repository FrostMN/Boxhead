'''
Version 4
'''
from msvcrt import getch
from config import *
from assets import *
from utilities import *

def game_menu():
    width, height = settings['width'], settings['height'] - 1
    master_border = []

    # initial boarder
    for i in range(height):
        index = height - 1
        if i == 0:
            master_border.append([sprites['top_border']] * width)
        elif i != index:
            middle = [' '] * (width - 2)
            master_border.append([sprites['y_border']] + middle + [sprites['y_border']])
        elif i == index:
            master_border.append([sprites['bottom_border']] * width)

    # title
    title = menu_title()
    for i in range(height):
        if i < 3:
            pass
        else:
            try:
                title_index = title[i - 3]
            except IndexError:
                pass
            else:
                for n in range(len(title_index)):
                    master_border[i][n + 5] = title_index[n]
    for i in range(height):
        for n in range(width):
            if '█' in master_border[i][n]:
                master_border[i][n] = color_sprites(sprites['y_border'], 'cyan')

    # menu
    for i in range(height):
        if i == 12:
            for n in range(width):
                if n < 9 :
                    pass
                elif n > width - 39:
                    pass
                else:
                    master_border[i][n] = sprites['top_border']

    # options
    play = list('> Play')
    for i in range(len(play)):
        master_border[15][i + 15] = play[i]

    # high score
    score = list('  High Score  ')
    for i in range(len(score)):
        master_border[17][i + 15] = score[i]

    # quit
        quit = list('  Quit')
    for i in range(len(quit)):
        master_border[19][i + 15] = quit[i]

    return master_border

def game_gui():
    width, height = settings['width'], settings['height'] - 1
    master_border = []
    # # GUI
    # initial boarder
    for i in range(height):
        index = height - 1
        if i == 0:
            master_border.append([sprites['top_border']] * width)
        elif i != index:
            middle = [' '] * (width - 2)
            master_border.append([sprites['y_border']] + middle + [sprites['y_border']])
        elif i == index:
            master_border.append([sprites['bottom_border']] * width)

    # stats
    for i in range(width):
        if i == 0:
            pass
        elif i == width - 1:
            pass
        else:
            master_border[2][i] = sprites['bottom_border']

    # title
    title = list('Boxhead')
    for i in range(len(title)):
        master_border[1][i+3] = title[i]

    # title border
    master_border[1][12] = sprites['y_border']

    # wave
    wave = list('Wave: 01')
    for i in range(len(wave)):
        master_border[1][i + 15] = wave[i]

    # title border
    master_border[1][26] = sprites['y_border']

    # score
    score = list('Score: 00000')
    for i in range(len(score)):
        master_border[1][i + 29] = score[i]

    # title border
    master_border[1][44] = sprites['y_border']

    # kills
    kills = list('Kills: 00')
    for i in range(len(kills)):
        master_border[1][i + 47] = kills[i]

    # title border
    master_border[1][58] = sprites['y_border']

    # health
    health = list('Health: 20/20')
    for i in range(len(health)):
        master_border[1][i + 61] = health[i]

    # title border
    master_border[1][76] = sprites['y_border']

    # potions
    potions = list('(P)otions: [x] [x] [x]')
    for i in range(len(potions)):
        master_border[1][i + 79] = potions[i]

    # # sprites

    # player
    master_border[(height//2)][(width//2)] = sprites['player']

    # door north
    master_border[3][(width//2)] = sprites['door']
    # door south
    master_border[(height-2)][(width//2)] = sprites['door']
    # door east
    master_border[(height//2)][(width-3)] = sprites['door']
    # door west
    master_border[(height//2)][1] = sprites['door']
    # door west enemy
    master_border[(height//2)][2] = sprites['enemy']

    return master_border

def game_score():
    width, height = settings['width'], settings['height'] - 1
    master_border = []

    # initial boarder
    for i in range(height):
        index = height - 1
        if i == 0:
            master_border.append([sprites['top_border']] * width)
        elif i != index:
            middle = [' '] * (width - 2)
            master_border.append([sprites['y_border']] + middle + [sprites['y_border']])
        elif i == index:
            master_border.append([sprites['bottom_border']] * width)

    for i in range(width):
        if i == 0:
            pass
        elif i == width - 1:
            pass
        else:
            master_border[2][i] = sprites['bottom_border']

    # title
    title = list('High Scores')
    for i in range(len(title)):
        master_border[1][i + 3] = title[i]

    return master_border

