import pygame as pg
import random as rd

class brush:
    def __init__(self, grid, brushSize):
        self.grid = grid
        self.brushSize = brushSize
        brushGrid = [[0 for _ in range(brushSize)] for _ in range(brushSize)]

    def draw(self):
        if pg.mouse.get_pressed()[0]:
            x, y = pg.mouse.get_pos()
            for i in range(self.brushSize):
                for j in range(self.brushSize):
                    if i + y // self.grid.cell_size < self.grid.row and j + x // self.grid.cell_size < self.grid.col:
                        self.grid.grid[i + y // self.grid.cell_size][j + x // self.grid.cell_size].setState(1)
        elif pg.mouse.get_pressed()[2]:
            x, y = pg.mouse.get_pos()
            for i in range(self.brushSize):
                for j in range(self.brushSize):
                    if i + y // self.grid.cell_size < self.grid.row and j + x // self.grid.cell_size < self.grid.col:
                        self.grid.grid[i + y // self.grid.cell_size][j + x // self.grid.cell_size].setState(0)