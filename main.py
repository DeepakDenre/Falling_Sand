import pygame as pg
import grid as gd
import brush as br
from setting import *

class main:
    def __init__(self,):
        pg.init()
        pg.display.set_caption(TITLE)
        self.grid = gd.Grid(col, row, cell_size)
        self.brush = br.brush(self.grid, brushSize)
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.running = True

    def gameEvent(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and (event.key == pg.K_ESCAPE or event.key == pg.K_x)):
                # close the game
                self.running = False
        if pg.mouse.get_pressed()[0]: #left click set cell state to 1
            self.brush.Cursor()

    def gameLogicUpdate(self):
        self.grid.update()

    def gameRender(self):
        self.screen.fill(SCREEN_COLOR)
        self.grid.render(self.screen)
        pg.display.update()

    def run(self):
        while self.running:
            self.gameEvent()
            self.gameLogicUpdate()
            self.gameRender()
            self.clock.tick(FPS)
        pg.quit()

main().run()