import random

up = 0
left = 1
down = 2
right = 3

def newFullGrid(n,m):
    d = {}
    for i in xrange(n):
        for j in xrange(m):
            d[(i,j)] = [True,True,True,True]
    return d
