from random import randint
from random import choice
from pickle import load

class Floor:
    def __init__(self, size, difficulty):
        self.__size = size
        self.__difficulty = difficulty
        self.sprites = load(open('sprites.dat', 'rb'))
        self.color = load(open('color.dat', 'rb'))

    def colorize(self, string, clr):
        return '{0}{1}{2}'.format(self.color[clr], string, self.color['end'])

    def make_floor(self):
        sprites = self.sprites
        floor = []
        width, height = self.__size
        enemy_count, gold_count = self.__difficulty
        wall = self.colorize(sprites['wall'], 'light_cyan')
        ground = sprites['ground']
        player = sprites['player']
        enemy = self.colorize(sprites['enemy'], 'red')
        gold = self.colorize(sprites['gold'], 'brown')
        down = sprites['down']

        # generate boarder
        for i in range(height):
            index = height - 1
            if i == 0:
                floor.append([wall] * width)
            elif i != index:
                middle = [ground] * (width - 2)
                floor.append([wall] + middle + [wall])
            elif i == index:
                floor.append([wall] * width)

        # generate walls
        build = choice([1, 2, 3, 4, 5, 6, 7])

        if build == 1:
            for i in range(height):
                for n in range(width):
                    if i == 0:
                        pass
                    elif i == height - 1:
                        pass
                    elif i < round(height * .4):
                        floor[i][n] = wall
                    elif i > round(height * .5):
                        floor[i][n] = wall

        elif build == 2:
            for i in range(height):
                for n in range(width):
                    if n == 0:
                        pass
                    elif n == width - 1:
                        pass
                    elif n < round(width * .4):
                        floor[i][n] = wall
                    elif n > round(width * .6):
                        floor[i][n] = wall

        elif build == 3:
            for i in range(height):
                for n in range(width):
                    if i == 0:
                        pass
                    elif i == height - 1:
                        pass
                    elif i < round(height * .2):
                        floor[i][n] = wall
                    elif i > round(height * .6):
                        floor[i][n] = wall

            for i in range(height):
                for n in range(width):
                    if n == 0:
                        pass
                    elif n == width - 1:
                        pass
                    elif n < round(width * .4):
                        floor[i][n] = wall
                    elif n > round(width * .6):
                        floor[i][n] = wall

        elif build == 4:
            for i in range(height):
                for n in range(width):
                    if i == 0:
                        pass
                    elif i == height - 1:
                        pass
                    elif i < round(height * .2):
                        floor[i][n] = wall
                    elif i > round(height * .5):
                        floor[i][n] = wall

            for i in range(height):
                for n in range(width):
                    if n == 0:
                        pass
                    elif n == width - 1:
                        pass
                    elif n < round(width * .2):
                        floor[i][n] = wall
                    elif n > round(width * .6):
                        floor[i][n] = wall

        elif build == 5:
            for i in range(height):
                for n in range(width):
                    if i == 0:
                        pass
                    elif i == height - 1:
                        pass
                    elif i < round(height * .5):
                        floor[i][n] = wall
                    elif i > round(height * .9):
                        floor[i][n] = wall

            for i in range(height):
                for n in range(width):
                    if n == 0:
                        pass
                    elif n == width - 1:
                        pass
                    elif n < round(width * .6):
                        floor[i][n] = wall
                    elif n > round(width * .8):
                        floor[i][n] = wall

        elif build == 6:
            for i in range(height):
                for n in range(width):
                    if i == 0:
                        pass
                    elif i == height - 1:
                        pass
                    elif i < round(height * .5):
                        floor[i][n // i] = wall
                    elif i > round(height * .9):
                        floor[i][n] = wall

        elif build == 7:
            for i in range(height):
                for n in range(width):
                    if i == 0:
                        pass
                    elif i == height - 1:
                        pass
                    elif i > round(height ** .5):
                        floor[i][n // i] = wall
                    elif n < round(height ** .9):
                        try:
                            floor[i ** 2][round(n ** .9)] = wall
                        except IndexError:
                            pass
                        else:
                            pass

            for i in range(height):
                for n in range(width):
                    if n == 0:
                        pass
                    elif n == height - 1:
                        pass
                    elif i > (randint(0, height)):
                        floor[i][height // n] = wall
        else:
            pass

        # generate exit
        count = 0
        while count != 1:
            y = randint(0, height)
            x = randint(0, width)
            try:
                floor[y][x]
            except IndexError:
                continue
            else:
                if floor[y][x] == wall:
                    continue
                else:
                    floor[y][x] = down
                    count += 1

        # generate enemies
        count = 0
        while count != enemy_count:
            y = randint(0, height)
            x = randint(0, width)
            try:
                floor[y][x]
            except IndexError:
                continue
            else:
                if floor[y][x] == wall:
                    continue
                elif floor[y][x] == down:
                    continue
                else:
                    floor[y][x] = enemy
                    count += 1

        # generate gold
        count = 0
        while count != gold_count:
            y = randint(0, height)
            x = randint(0, width)
            try:
                floor[y][x]
            except IndexError:
                continue
            else:
                if floor[y][x] == wall:
                    continue
                elif floor[y][x] == enemy:
                    continue
                elif floor[y][x] == down:
                    continue
                else:
                    floor[y][x] = gold
                    count += 1

        # generate player
        count = 0
        while count != 1:
            y = randint(0, height)
            x = randint(0, width)
            try:
                floor[y][x]
            except IndexError:
                continue
            else:
                if floor[y][x] == wall:
                    continue
                elif floor[y][x] == enemy:
                    continue
                elif floor[y][x] == gold:
                    continue
                elif floor[y][x] == down:
                    continue
                else:
                    floor[y][x] = player
                    count += 1

        return floor