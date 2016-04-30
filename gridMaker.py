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

def asciiGrid(g,n,m):
    c = ""
    for i in xrange(n):
        for j in xrange(m):
            if g[(i,j)][down]:
                c += '_'
            else:
                c += ' '
            if g[(i,j)][right]:
                c += '|'
            else:
                c += ' '
        c += '\n'
    return c

def randomGrid(n,m):
    return newFullGrid(n,m)
