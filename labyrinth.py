import gridMaker

grid = gridMaker.newFullGrid(10,10)

class maze(object):
    def __init__(self, grid):
        self.grid=grid
        self.player_pos = (0,0)
        self.minotaur_pos = (9,9)
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

m=maze(grid)
m.move_minotaur()
