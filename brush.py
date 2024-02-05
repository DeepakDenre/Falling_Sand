import pygame as pg
import random as rd

class brush:
    def __init__(self, grid, brushSize):
        self.grid = grid
        self.brushSize = brushSize
        self.brushgrid = [[1 for _ in range(brushSize)] for _ in range(brushSize)]
        
    def Cursor(self):
        y,x = pg.mouse.get_pos()
        if pg.mouse.get_pressed()[0]:
            for i in range(self.brushSize):
                for j in range(self.brushSize):
                    try:
                        self.grid.gridNext[int((x+i)/self.grid.cell_size)][int((y+j)/self.grid.cell_size)].setState(1)
                    except:
                        pass