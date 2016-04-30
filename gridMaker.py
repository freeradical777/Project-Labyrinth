#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

up = 0
left = 1
down = 2
right = 3
dirs = [up,left,down,right]

def neg(d):
    if   d == up:
        return down
    elif d == left:
        return right
    elif d == down:
        return up
    elif d == right:
        return left
    else:
        raise(ValueError, d ++ " is not a direction")
        return do

def go((i,j),d):
    if   d == up:
        return (i,j-1)
    elif d == left:
        return (i-1,j)
    elif d == down:
        return (i,j+1)
    elif d == right:
        return (i+1,j)
    else:
        raise(ValueError, d ++ " is not a direction")


def newFullGrid(n,m):
    d = {}
    for i in xrange(n):
        for j in xrange(m):
            d[(i,j)] = [True,True,True,True]
    return d

def asciiGrid(g,n,m):
    c = ""
    for j in xrange(m):
        for i in xrange(n):
            if g[(i,j)][up]:
                c += '.|.'
            else:
                c += '...'
        c += '\n'
        for i in xrange(n):
            if g[(i,j)][left]:
                c += '-'
            else:
                c += '.'
            c += '+'
            if g[(i,j)][right]:
                c += '-'
            else:
                c += '.'
        c += '\n'
        for i in xrange(n):
            if g[(i,j)][up]:
                c += '.|.'
            else:
                c += '...'
        c += '\n'
    return c

def randomGrid(n,m):
    #From http://weblog.jamisbuck.org/2011/1/27/maze-generation-growing-tree-algorithm
    g = newFullGrid(n,m)
    c = [random.choice(g.keys())]
    visited = c[:]
    while c:
        #print asciiGrid(g,n,m)
        node = pickNode(c)
        neighbors = []
        for d in dirs:
            neighbor = go(node,d)
            if neighbor not in visited and neighbor in g:
                neighbors.append((d,neighbor))
        if not neighbors:
            c.remove(node)
            continue
        (d,neighbor) = pickNeighbor(neighbors)
        g[node][d] = False
        g[neighbor][neg(d)] = False
        c.append(neighbor)
        visited.append(neighbor)
    return g

pickNode = random.choice
pickNeighbor = random.choice


print asciiGrid(randomGrid(4,3),4,3)
