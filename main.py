#external library import
import pygame, sys
from pygame.locals import *
from screeninfo import get_monitors #found in: https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python

#file imports from game directory
from player import Player
from worldmap import Map

#Temporary import/import location
currentPlayer = Player()

#template for class from: https://pythonspot.com/game-development-with-pygame/
class Game:

    windowWidth = int(get_monitors()[0].width/2)
    windowHeight = int(get_monitors()[0].height/2)

    def __init__(self):
        self._running = True
        self._display = None
        self._rendering = "map"
        self.map = Map()
        self.map_inputs = [] #backlog play inputs to send to map class

    def on_init(self):
        pygame.init()
        self._display = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption("Text-Based RPG Game (No Name)")

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

        #player test
        if event.type == KEYDOWN: #Key labeling in pygame: https://www.pygame.org/docs/ref/key.html
            if event.key == K_0: #This is temp, testing for player leveling and key input
                currentPlayer.xp_gain(10) 
            if event.key == K_ESCAPE:
                self._rendering = "title"
            #detect movement begin commands
            if event.key == K_w or event.key == K_UP and self._rendering == "map": 
                self.map_inputs.append("up")
            if event.key == K_s or event.key == K_DOWN and self._rendering == "map":
                self.map_inputs.append("down")
            if event.key == K_a or event.key == K_LEFT and self._rendering == "map": 
                self.map_inputs.append("left")
            if event.key == K_d or event.key == K_RIGHT and self._rendering == "map":  
                self.map_inputs.append("right")
        elif event.type == KEYUP:
            #detect movement end commands
            if event.key == K_w or event.key == K_UP and self._rendering == "map": 
                self.map_inputs.append("upstop")
            if event.key == K_s or event.key == K_DOWN and self._rendering == "map":  
                self.map_inputs.append("downstop")
            if event.key == K_a or event.key == K_LEFT and self._rendering == "map":  
                self.map_inputs.append("leftstop")
            if event.key == K_d or event.key == K_RIGHT and self._rendering == "map":  
                self.map_inputs.append("rightstop")

    def on_loop(self):
        pass

    def on_render(self):
        #render test (testing rendering and player leveling):
        testFont = pygame.font.SysFont('Times New Roman', 30)
        if self._rendering == "title":
            self._display.fill((255,255,255))
            self._display.blit(testFont.render("Player Level: " + str(currentPlayer.level), True, (0,0,0)), (20, 20))
            self._display.blit(testFont.render("Player XP: " + str(currentPlayer.xp), True, (0,0,0)), (20, 100))
        elif self._rendering == "map":
            self.map.renderMap(self._display, testFont, self.map_inputs, self.windowWidth, self.windowHeight)
            self.map_inputs = []

    def on_quit(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        pygame.display.flip()
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            pygame.display.update()
        self.on_quit()


Game().on_execute()