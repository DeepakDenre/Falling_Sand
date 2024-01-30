import pygame as pg
import sys
import grid as gd
from setting import *

grid = gd.Grid(col, row, cell_size)

if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('Falling Sand Simulation')
    clock = pg.time.Clock()
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
        # Draw the sand
        grid.draw()
            
        screen.fill((0 ,0 ,0))

        # Update the grid
        grid.update()

        # Draw the grid
        grid.render(screen,(255, 255, 255))

        pg.display.update()
        clock.tick(60)

    pg.quit()