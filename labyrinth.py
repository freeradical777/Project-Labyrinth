import gridMaker

grid = gridMaker.randomGrid(10,10)

class maze(object):
    def __init__(self, grid):
        self.grid=grid
        self.player_pos = ()
        self.minotaur_pos = ()
