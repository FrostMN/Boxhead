'''
Version 4
'''
from gui import *

class Menu:
    def __init__(self):
        self.menu_screen = game_menu()
        self.width, self.height = settings['width'], settings['height'] - 1

    def find_cursor(self):
        cursor = '>'
        for i in range(self.height):
            if cursor in self.menu_screen[i]:
                first = i
                second = self.menu_screen[i].index(cursor)
                return first, second
            else:
                continue

    def menu_selector(self, keystroke):
        self.cursor_y, self.cursor_x = self.find_cursor()
        if keystroke == 119:
            if self.menu_screen[15][15] == '>':
                pass
            else:
                self.menu_screen[self.cursor_y - 2][self.cursor_x] = '>'
                self.menu_screen[self.cursor_y][self.cursor_x] = ' '

        elif keystroke == 115:
            if self.menu_screen[19][15] == '>':
                pass
            else:
                self.menu_screen[self.cursor_y + 2][self.cursor_x] = '>'
                self.menu_screen[self.cursor_y][self.cursor_x] = ' '
        else:
            pass

    def get_state(self):
        for i in range(len(self.menu_screen)):
            print(' ', end='')
            for n in range(len(self.menu_screen[i])):
                print(self.menu_screen[i][n], end='')
            print('\n', end='')

    def mainloop(self):
        while True:
            clear_screen()
            self.get_state()
            self.event = ord(getch())
            if self.event == 27:
                break
            elif self.event == 13:
                self.cursor_y, self.cursor_x = self.find_cursor()
                if self.menu_screen[self.cursor_y][self.cursor_x + 2] == 'P':
                    return 'P'
                    break
                elif self.menu_screen[self.cursor_y][self.cursor_x + 2] == 'H':
                    return 'H'
                    break
                elif self.menu_screen[self.cursor_y][self.cursor_x + 2] == 'Q':
                    return 'Q'
                    break
            else:
                self.menu_selector(self.event)
                continue

class Gameplay:
    def __init__(self):
        self.game_screen = game_gui()
        self.width, self.height = settings['width'], settings['height'] - 1

    def find_sprite(self, find):
        sprite = sprites[find]
        for i in range(self.height):
            if sprite in self.game_screen[i]:
                first = i
                second = self.game_screen[i].index(sprite)
                return first, second
            else:
                continue

    def get_state(self):
        for i in range(len(self.game_screen)):
            print(' ', end='')
            for n in range(len(self.game_screen[i])):
                print(self.game_screen[i][n], end='')
            print('\n', end='')

    def player_movement(self, direction):
        self.direction = direction
        self.player_y, self.player_x = self.find_sprite('player')
        player = sprites['player']
        ground = sprites['ground']
        if self.direction == 119:  # w
            next_move = self.game_screen[self.player_y - 1][self.player_x]
            if next_move == ' ':
                self.game_screen[self.player_y - 1][self.player_x] = player
                self.game_screen[self.player_y][self.player_x] = ground
            else:
                pass
        elif self.direction == 97:  # a
            next_move = self.game_screen[self.player_y][self.player_x - 1]
            if next_move == ' ':
                self.game_screen[self.player_y][self.player_x - 1] = player
                self.game_screen[self.player_y][self.player_x] = ground
            else:
                pass
        elif self.direction == 115:  # s
            next_move = self.game_screen[self.player_y + 1][self.player_x]
            if next_move == ' ':
                self.game_screen[self.player_y + 1][self.player_x] = player
                self.game_screen[self.player_y][self.player_x] = ground
            else:
                pass
        elif self.direction == 100:  # d
            next_move = self.game_screen[self.player_y][self.player_x + 1]
            if next_move == ' ':
                self.game_screen[self.player_y][self.player_x + 1] = player
                self.game_screen[self.player_y][self.player_x] = ground
            else:
                pass
        else:
            pass

    def ememy_pathing(self):
        self.enemy_y, self.enemy_x = self.find_sprite('enemy')
        self.player_y, self.player_x = self.find_sprite('player')
        player = sprites['player']
        enemy = sprites['enemy']
        ground = sprites['ground']

        if self.enemy_y == self.player_y:
            if self.enemy_x < self.player_x:
                self.game_screen[self.enemy_y][self.enemy_x + 1] = enemy
                self.game_screen[self.enemy_y][self.enemy_x] = ground
            elif self.enemy_x > self.player_x:
                self.game_screen[self.enemy_y][self.enemy_x - 1] = enemy
                self.game_screen[self.enemy_y][self.enemy_x] = ground
            else:
                pass
        elif self.enemy_x == self.player_x:
            if self.enemy_y < self.player_y:
                self.game_screen[self.enemy_y + 1][self.enemy_x] = enemy
                self.game_screen[self.enemy_y][self.enemy_x] = ground
            elif self.enemy_y > self.player_y:
                self.game_screen[self.enemy_y - 1][self.enemy_x] = enemy
                self.game_screen[self.enemy_y][self.enemy_x] = ground
            else:
                pass
        elif self.enemy_x < self.player_y:
            if self.enemy_y < self.player_y:
                self.game_screen[self.enemy_y + 1][self.enemy_x] = enemy
                self.game_screen[self.enemy_y][self.enemy_x] = ground
            elif self.enemy_y > self.player_y:
                self.game_screen[self.enemy_y - 1][self.enemy_x] = enemy
                self.game_screen[self.enemy_y][self.enemy_x] = ground
            else:
                pass
        else:
            pass

    def mainloop(self):
        while True:
            clear_screen()
            self.get_state()
            self.event = ord(getch())
            if self.event == 27: # force quit
                break
            elif self.event == 112: # potion
                pass
            else:
                self.player_movement(self.event)
                self.ememy_pathing()
                continue