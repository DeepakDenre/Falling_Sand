import pygame as pg
import random as rd
import cell as cl

class Grid:
    def __init__(self, col, row, cell_size):
        self.col = col
        self.row = row
        self.cell_size = cell_size
        self.grid = [[cl.Cell(cell_size,color=(rd.randrange(0,255),rd.randrange(0,255),rd.randrange(0,255))) for _ in range(col)] for _ in range(row)]

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
                    if below == 0:
                        self.grid[y][x].setState(0)
                        self.grid[y + 1][x].setState(1)
                    else:
                        pass
    
    def draw(self):
        if pg.mouse.get_pressed()[0]:
            x, y = pg.mouse.get_pos()
            self.grid[y // self.cell_size][x // self.cell_size].setState(1)