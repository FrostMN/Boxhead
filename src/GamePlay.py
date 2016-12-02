from sys import platform as _platform
from tabulate import tabulate
from msvcrt import getch
from pickle import load
from os import system

class Boxhead:
    def __init__(self, world):
        self.world = world
        self.width, self.height = len(self.world[0][0]), len(self.world[0])
        self.sprites = load(open('sprites.dat', 'rb'))
        self.color = load(open('color.dat', 'rb'))
        self.wall = self.colorize(self.sprites['wall'], 'light_cyan')
        self.ground = self.sprites['ground']
        self.player = self.sprites['player']
        self.enemy = self.colorize(self.sprites['enemy'], 'red')
        self.gold = self.colorize(self.sprites['gold'], 'brown')
        self.down = self.sprites['down']

        self.money = 0
        self.floor = 1
        self.hp = 6
        self.max_hp = 6

    def colorize(self, string, clr):
        return '{0}{1}{2}'.format(self.color[clr], string, self.color['end'])

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

    def find_player(self):
        player = self.sprites['player']
        for i in range(self.height):
            if player in self.level[i]:
                first = i
                second = self.level[i].index(player)
                return first, second
            else:
                continue

    def movement(self, direction):
        self.direction = direction
        self.player_y, self.player_x = self.find_player()
        if self.direction == 119:  # w
            next_move = self.level[self.player_y - 1][self.player_x]
            if next_move == self.wall:
                pass
            elif next_move == self.gold:
                self.level[self.player_y - 1][self.player_x] = self.player
                self.level[self.player_y][self.player_x] = self.ground
                self.money += 1
            elif next_move == self.down:
                self.floor += 1
                return 'next_level'
            elif next_move == self.enemy:
                self.level[self.player_y - 1][self.player_x] = self.player
                self.level[self.player_y][self.player_x] = self.ground

            else:
                self.level[self.player_y - 1][self.player_x] = self.player
                self.level[self.player_y][self.player_x] = self.ground
        elif self.direction == 97:  # a
            next_move = self.level[self.player_y][self.player_x - 1]
            if next_move == self.wall:
                pass
            elif next_move == self.gold:
                self.level[self.player_y][self.player_x - 1] = self.player
                self.level[self.player_y][self.player_x] = self.ground
                self.money += 1
            elif next_move == self.down:
                self.floor += 1
                return 'next_level'
            elif next_move == self.enemy:
                self.level[self.player_y][self.player_x - 1] = self.player
                self.level[self.player_y][self.player_x] = self.ground

            else:
                self.level[self.player_y][self.player_x - 1] = self.player
                self.level[self.player_y][self.player_x] = self.ground
        elif self.direction == 115:  # s
            next_move = self.level[self.player_y + 1][self.player_x]
            if next_move == self.wall:
                pass
            elif next_move == self.gold:
                self.level[self.player_y + 1][self.player_x] = self.player
                self.level[self.player_y][self.player_x] = self.ground
                self.money += 1
            elif next_move == self.down:
                self.floor += 1
                return 'next_level'
            elif next_move == self.enemy:
                self.level[self.player_y + 1][self.player_x] = self.player
                self.level[self.player_y][self.player_x] = self.ground

            else:
                self.level[self.player_y + 1][self.player_x] = self.player
                self.level[self.player_y][self.player_x] = self.ground
        elif self.direction == 100:  # d
            next_move = self.level[self.player_y][self.player_x + 1]
            if next_move == self.wall:
                pass
            elif next_move == self.gold:
                self.level[self.player_y][self.player_x + 1] = self.player
                self.level[self.player_y][self.player_x] = self.ground
                self.money += 1
            elif next_move == self.down:
                self.floor += 1
                return 'next_level'
            elif next_move == self.enemy:
                self.level[self.player_y][self.player_x + 1] = self.player
                self.level[self.player_y][self.player_x] = self.ground

            else:
                self.level[self.player_y][self.player_x + 1] = self.player
                self.level[self.player_y][self.player_x] = self.ground
        else:
            pass

    def get_world(self, level):
        for i in range(len(level)):
            for n in range(len(level[i])):
                print(level[i][n], end='')
            print('\n', end='')

    def test_world(self):
        for level in range(len(self.world)):
            for i in range(len(self.world[level])):
                for n in range(len(self.world[level][i])):
                    print(self.world[level][i][n], end='')
                print('\n', end='')

    def mainloop(self):
        for level in range(len(self.world)):
            self.level = self.world[level]
            while True:
                self.clear_screen()
                print(tabulate([['BOXHEAD','Floor: {0}'.format(self.floor), 'Health: {0}/{1}'.format(self.hp, self.max_hp), 'Gold: {0}'.format(self.money)]],tablefmt='grid'))
                self.get_world(self.level)
                self.user_input = ord(getch())
                if self.user_input == 27:
                    break
                else:
                    catch = self.movement(self.user_input)
                    if catch == 'next_level':
                        break
                    else:
                        continue
