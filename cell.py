import pygame as pg
import sys
import grid as gd

class Cell:
    color = (255, 255, 255)
    state = 0
    cell_type = "sand,"
    def __init__(self, cell_size, color = (255, 255, 255), state = 0):
        self.cell_size = cell_size
        self.state = state
        self.color = color

    def swapColor(self, x1 , y1, x2, y2):
        color1 = self.gridCurrent[y1][x1].getColor()
        color2 = self.gridCurrent[y2][x2].getColor()
        self.gridCurrent[y1][x1].setColor(color2)
        self.gridCurrent[y2][x2].setColor(color1)

    def getColor(self):
        return self.color

    def getState(self):
        return self.state
    
    def getCellType(self):
        return self.cell_type
    
    def setColor(self,cellColor):
        self.color = cellColor

    def setState(self, cellState):
        self.state = cellState

    def setCellType(self, cellType):
        self.cell_type = cellType