from pygame.locals import *

class Map:

    testMap = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    def __init__(self):
        pass
    
    def renderMap(self, _display, pygame, font, inputs):
        _display.blit(font.render("You in map, yes?", True, (0,0,0)), (20, 100))