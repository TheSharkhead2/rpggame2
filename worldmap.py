from pygame.locals import *
import math
import pygame, sys

class Map:

    tileSize = 30
    testMap = {'map' : [
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
    ],
    'pStart' : (2,2)
    }
    baseFloorImg = pygame.image.load("assets/tiles/basefloor.png")
    baseWallImg = pygame.image.load("assets/tiles/basewall.png")

    def __init__(self):
        self.current_map = self.testMap
        self.player_location = self.current_map['pStart']
    
    def _centerScreen(self, windowWidth, windowHeight):
        return((int(math.floor(windowWidth/2)), int(math.floor(windowHeight/2))))

    def renderMap(self, _display, font, inputs, windowWidth, windowHeight):
        _display.fill((0,0,0))
        _display.blit(font.render("You in map, yes?", True, (0,0,0)), (20, 100))
        center_square_render = (int(self._centerScreen(windowWidth, windowHeight)[0] - self.tileSize/2), int(self._centerScreen(windowWidth, windowHeight)[1] - self.tileSize/2)) #location of top left corner for gridsize

        for offsetx in range(-2,3):
            for offsety in range(-2, 3):
                currentlyRendering = (self.player_location[0] + offsety, self.player_location[1] + offsetx)
                if currentlyRendering[0] < 0 or currentlyRendering[1] < 0 or currentlyRendering[0] > len(self.current_map['map'][0]) or currentlyRendering[1] > len(self.current_map['map']): #don't render a tile with nothing
                    pass
                else:
                    renderPos = (center_square_render[0] + self.tileSize*offsetx, center_square_render[1] + self.tileSize*offsety)
                    if self.current_map['map'][currentlyRendering[0]][currentlyRendering[1]] == 0:
                        _display.blit(self.baseFloorImg, renderPos)
                    elif self.current_map['map'][currentlyRendering[0]][currentlyRendering[1]] == 1:
                        _display.blit(self.baseWallImg, renderPos)
