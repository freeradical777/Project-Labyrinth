import gridMaker
from gridMaker import *

grid = gridMaker.newFullGrid(10,10)

class Maze(object):
    def __init__(self, grid, n, m):
        self.grid=grid
        self.player_pos = (0,0)
        self.minotaur_pos = (9,9)
        self.n = n
        self.m = m
    def move_minotaur(self):
        moves=[(self.player_pos)]
        path_found = False

        while not path_found:
            for move in moves: #For every cell in the plotted moves
                cell = self.grid[move] #The attributes of that cell
                dir_itr = 0
                for direction in cell: #For every possible wall location

                    if direction != True: #If there is not a wall

                        new_move=gridMaker.go(move, dir_itr)

                        if new_move not in moves:
                            moves.append(new_move) #Append the adjacent cell 
                            if new_move == self.minotaur_pos: #If the new move reaches the minotaur, stop
                                path_found=True
                                self.minotaur_pos=move
                                break
                    dir_itr += 1
                    if path_found == True:
                        break
                if path_found == True:
                    break

    def __repr__(self):
        rep = ""
        for j in xrange(self.m):
            for i in xrange(self.n):
                if self.grid[(i,j)][up]:
                    rep += '+--+'
                else:
                    rep += '+  +'
            rep += '\n'
            for _ in xrange(2):
                for i in xrange(self.n):
                    if self.grid[(i,j)][left]:
                        rep += '|'
                    else:
                        rep += ' '
                    if (i,j) == self.minotaur_pos:
                        rep += 'MM'
                    elif (i,j) == self.player_pos:
                        rep += 'pp'
                    else:
                        rep += '  '
                    if self.grid[(i,j)][right]:
                        rep += '|'
                    else:
                        rep += ' '
                rep += '\n'
            for i in xrange(self.n):
                if self.grid[(i,j)][down]:
                    rep += '+--+'
                else:
                    rep += '+  +'
            rep += '\n'
        return rep

m=Maze(grid, 10, 10)
m.move_minotaur()
