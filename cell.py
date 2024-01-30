import pygame as pg
import sys
import grid as gd

class Cell:
    def __init__(self, cell_size, color = (255, 255, 255), state = 0):
        self.cell_size = cell_size
        self.state = state
        self.color = color

    def getcolor(self):
        return self.color

    def getState(self):
        return self.state
    
    def setcolor(self,cellColor):
        self.color = cellColor

    def setState(self, cellState):
        self.state = cellState