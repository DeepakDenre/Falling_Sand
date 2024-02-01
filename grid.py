import pygame as pg
import random as rd
import cell as cl
from setting import *

colorSet = [red, green, blue, yellow]

class Grid:
    def __init__(self, col, row, cell_size):
        self.col = col
        self.row = row
        self.cell_size = cell_size
        self.grid = [[cl.Cell(cell_size,color=colorSet[rd.randrange(0,len(colorSet))]) for _ in range(col)] for _ in range(row)]

    def render(self, screen,color = (255, 255, 255)):
        for y in range(self.row):
            for x in range(self.col):
                if self.grid[y][x].getState() == 1:
                    pg.draw.rect(screen, self.grid[y][x].getcolor(), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                else:
                    pass

    def update(self):
        for y in range(self.row):
            for x in range(self.col):
                state = self.grid[y][x].getState()
                if state == 1 and y < self.row - 1:
                    below = self.grid[y + 1][x].getState()
                    if below == 0 :
                        self.grid[y][x].setState(0)
                        self.grid[y + 1][x].setState(1)
                    elif below == 1 and x > 0 and x < self.col - 1:
                        right = self.grid[y+1][x + 1].getState()
                        left = self.grid[y+1][x - 1].getState()
                        if right == 0 and left == 0:
                            self.grid[y][x].setState(0)
                            self.grid[y + 1][x + rd.randrange(-1,1,2)].setState(1)
                        elif right == 0:
                            self.grid[y][x].setState(0)
                            self.grid[y + 1][x + 1].setState(1)
                        elif left == 0:
                            self.grid[y][x].setState(0)
                            self.grid[y + 1][x - 1].setState(1)
    