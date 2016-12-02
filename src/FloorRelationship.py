from FloorGeneration import Floor

class Relationships:
    def __init__(self, size, difficulty):
        self.__size = size
        self.__difficulty = difficulty
        self.world = []

    def create_world(self):
        for levels in range(10):
            level = Floor(self.__size, self.__difficulty)
            level_generated = level.make_floor()
            self.world.append(level_generated)

        return self.world