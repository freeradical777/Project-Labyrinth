import gridMaker
from gridMaker import *
import random

grid = gridMaker.randomGrid(int(raw_input("Input width: ")), int(raw_input("Input length: ")))


class Maze(object):
    def __init__(self, grid):
        self.grid=grid
        self.n=0
        self.m=0
        for (i,j) in grid.keys():
            if i>self.n: self.n = i
            if j>self.m: self.m = j
        self.n += 1
        self.m += 1
        self.player_pos = (random.randrange(self.n), random.randrange(self.m))
        self.minotaur_pos = (random.randrange(self.n), random.randrange(self.m))
        self.star_pos = ((random.randrange(self.n), random.randrange(self.m)))
    def won(self): return self.player_pos == self.star_pos
    def lost(self): return self.player_pos == self.minotaur_pos
    def move_minotaur(self):
        if self.player_pos != self.minotaur_pos:
            moves=[(self.player_pos)]
            path_found = False

            while not path_found:
                for move in moves: #For every cell in the plotted moves
                    cell = self.grid[move] #The attributes of that cell
                    dir_itr = 0
                    for direction in cell: #For every possible wall location
                        if direction != True: #If there is not a wall
                            new_move=go(move, dir_itr)
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

    def move_player(self, key):
        start = self.grid[self.player_pos]
        if key == 'w': d = up
        elif key == 'a': d = left
        elif key == 's': d = down
        elif key == 'd': d = right
        else: raise ValueError("Not a direction!")
        if start[d] == True: #If there's a wall
            raise ValueError("There's a wall there!")
        else:
            self.player_pos = go(self.player_pos, d)


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
                    elif (i,j) == self.star_pos:
                        rep += '**'
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

m=Maze(grid)
while not m.won() and not m.lost():
    print m
    try:
        m.move_player(raw_input("Direction: "))
    except ValueError as e:
        print e
        continue
    m.move_minotaur()

if m.won():
    print "You won!"
else:
    print "You lost!"
