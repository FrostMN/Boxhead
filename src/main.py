from GameSetup import Setup
from FloorRelationship import Relationships
from GamePlay import Boxhead

def main():
    size, difficulty = Setup().settings()
    levels_init = Relationships(size, difficulty)
    world = levels_init.create_world()
    boxhead = Boxhead(world)
    boxhead.mainloop()
    # boxhead.test_world()

main()