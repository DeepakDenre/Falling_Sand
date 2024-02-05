import pygame as pg
import random as rd
import cell as cl
from setting import *


class Grid:
    def __init__(self, col, row, cell_size):
        self.col = col
        self.row = row
        self.cell_size = cell_size
        self.gridCurrent = [[cl.Cell(cell_size,color=sandColorSet[rd.randrange(0,len(sandColorSet))]) for _ in range(col)] for _ in range(row)]
        self.gridNext = self.gridCurrent
        self.gridEmpty = self.gridCurrent
    def render(self, screen,color = (255, 255, 255)):
        for x in range(self.col):
            for y in range(self.row):
                if self.gridCurrent[y][x].getState() == 1:
                    pg.draw.rect(screen, self.gridCurrent[y][x].getColor(), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                else:
                    pass

    def update(self):
        for x in range(0,self.col):
            for y in range(0,self.row):
                try:
                    state = self.gridCurrent[y][x].getState()
                    down = self.gridCurrent[y+1][x].getState()
                    downRight = self.gridCurrent[y+1][x+1].getState()
                    downLeft = self.gridCurrent[y+1][x-1].getState()
                    if state == 1:
                        if down == 0:
                            self.gridNext[y][x].setState(0)
                            self.gridNext[y+1][x].setState(1)
                            cl.Cell.swapColor(self, x, y, x, y+1)
                        elif downRight == 0 and downLeft ==0:
                            ran = rd.randrange(-1,2,2)
                            self.gridNext[y][x].setState(0)
                            self.gridNext[y+1][x+ ran].setState(1)
                            cl.Cell.swapColor(self, x, y, x+ran, y+1)
                        elif downRight == 0 and downLeft == 1:
                            self.gridNext[y][x].setState(0)
                            self.gridNext[y+1][x+1].setState(1)
                            cl.Cell.swapColor(self, x, y, x+1, y+1)
                        elif downLeft == 0 and downRight == 1:
                            self.gridNext[y][x].setState(0)
                            self.gridNext[y+1][x-1].setState(1)
                            cl.Cell.swapColor(self, x, y, x-1, y+1)
                    else:
                        self.gridNext[y][x].setState(0)
                except:
                    pass
        self.gridCurrent, self.gridNext = self.gridNext, self.gridEmpty