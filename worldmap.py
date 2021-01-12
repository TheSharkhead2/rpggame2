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

    #define asset variables
    baseFloorImg = pygame.image.load("assets/tiles/basefloor.png")
    baseWallImg = pygame.image.load("assets/tiles/basewall.png")

    #define movement variables
    movingUp = False
    movingDown = False
    movingLeft = False
    movingRight = False

    def __init__(self):
        self.current_map = self.testMap
        self.player_location = self.current_map['pStart']
        self.player_location_exact = (int(self.current_map['pStart'][0]*self.tileSize+self.tileSize/2), int(self.current_map['pStart'][1]*self.tileSize+self.tileSize/2)) #get "exact" location for player at start (center of starting square)
        self.player_location_start_exact = self.player_location_exact #get exact starting location (variable is constant)
    
    def _playerLocationOffset(self): #returns tuple for how far in x and y player is from center square's top left corner (default render location)
        theoreticalPos = (int(self.player_location[0]*self.tileSize+self.tileSize/2), int(self.player_location[1]*self.tileSize+self.tileSize/2)) #takes square player is in and calculates center of square
        return ((self.player_location_exact[0] - theoreticalPos[0], self.player_location_exact[1] - theoreticalPos[1])) #find difference between "expected" location and actual location

    def _centerScreen(self, windowWidth, windowHeight):
        return((int(math.floor(windowWidth/2)), int(math.floor(windowHeight/2))))

    def _endPointsTile(self, x, y): #get all corners of tile based on top left corner (render location)
        return([(x, y), (x+self.tileSize, y), (x, y+self.tileSize), (x+self.tileSize, y+self.tileSize)])

    def _processUserInput(self, inputs):
        for userInput in inputs:
            #process start movement commands
            if userInput == 'up':
                self.movingUp = True
            elif userInput == 'down':
                self.movingDown = True
            elif userInput == 'left':
                self.movingLeft = True
            elif userInput == 'right':
                self.movingRight = True
            #process end movement commands
            elif userInput == 'upstop':
                self.movingUp = False
            elif userInput == 'downstop':
                self.movingDown = False
            elif userInput == 'leftstop':
                self.movingLeft = False
            elif userInput == 'rightstop':
                self.movingRight = False

    def _movePlayer(self):
        #move player
        if self.movingUp:
            self.player_location_exact = (self.player_location_exact[0], self.player_location_exact[1]-0.1)
            print(self.player_location_exact)
            print("moving up")
        if self.movingDown:
            self.player_location_exact = (self.player_location_exact[0], self.player_location_exact[1]+0.1)
            print(self.player_location_exact)
            print("moving down")
        if self.movingLeft:
            self.player_location_exact = (self.player_location_exact[0]-0.1, self.player_location_exact[1])
            print(self.player_location_exact)
            print("moving left")
        if self.movingRight:
            self.player_location_exact = (self.player_location_exact[0]+0.1, self.player_location_exact[1])
            print(self.player_location_exact)
            print("moving right")

        if self.player_location_exact[0] > self.tileSize * (self.player_location[0] + 1):
            self.player_location = (self.player_location[0] + 1, self.player_location[1]) 
        if self.player_location_exact[0] < self.tileSize * (self.player_location[0] - 1):
            self.player_location = (self.player_location[0] - 1, self.player_location[1])
            
        if self.player_location_exact[1] > self.tileSize * (self.player_location[1] + 1):
            self.player_location = (self.player_location[0], self.player_location[1] + 1) 
        if self.player_location_exact[1] < self.tileSize * (self.player_location[1] - 1):
            self.player_location = (self.player_location[0], self.player_location[1] - 1)



    def renderMap(self, _display, font, inputs, windowWidth, windowHeight):
        self._processUserInput(inputs) #set enviroment variables for inputs
        self._movePlayer() #run player movement 

        _display.fill((0,0,0)) #make screen black
        _display.blit(font.render(str(self.player_location), True, (255,255,255)), (20,20))
        _display.blit(font.render(str(self.player_location_exact), True, (255,255,255)), (20,50))
        center_square_render = (int(self._centerScreen(windowWidth, windowHeight)[0] - self.tileSize/2), int(self._centerScreen(windowWidth, windowHeight)[1] - self.tileSize/2)) #location of top left corner for gridsize

        renderOffset = self._playerLocationOffset() #grab value for offset from rendering with player in center of middle tile (when player not in center)

        endpoints = [] #list to record all endpoints for walls
        for offsetx in range(-4,5):
            for offsety in range(-4, 5):
                currentlyRendering = (self.player_location[1] + offsety, self.player_location[0] + offsetx)
                if currentlyRendering[0] < 0 or currentlyRendering[1] < 0 or currentlyRendering[0] > len(self.current_map['map'][0]) or currentlyRendering[1] > len(self.current_map['map']): #don't render a tile with nothing
                    pass
                elif currentlyRendering[0] > len(self.current_map['map']) - 1 or currentlyRendering[1] > len(self.current_map['map'][0]) - 1: #don't render out of map
                    pass
                else:
                    renderPosBase = (center_square_render[0] + self.tileSize*offsetx, center_square_render[1] + self.tileSize*offsety) #render position if player in center of square 
                    renderPos = (renderPosBase[0] - renderOffset[0], renderPosBase[1] - renderOffset[1])
                    if self.current_map['map'][currentlyRendering[0]][currentlyRendering[1]] == 0:
                        _display.blit(self.baseFloorImg, renderPos)
                    elif self.current_map['map'][currentlyRendering[0]][currentlyRendering[1]] == 1:
                        _display.blit(self.baseWallImg, renderPos)
                        for endpoint in self._endPointsTile(currentlyRendering[0], currentlyRendering[1]):
                            endpoints.append(endpoint)

        pygame.draw.circle(_display, (255,0,0), self._centerScreen(windowWidth, windowHeight), 10)