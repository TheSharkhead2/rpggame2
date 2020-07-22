#main file
#information:
#citations in comments (links provided)
#libraries used in "dependencies.txt"
#relying on pygame for visual library

#external library import
import pygame, sys
from pygame.locals import *
from screeninfo import get_monitors #found in: https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python

#file imports from game directory
from player import Player

#Temporary import/import location
currentPlayer = Player()

#template for class from: https://pythonspot.com/game-development-with-pygame/
class Game:

    windowWidth = int(get_monitors()[0].width/2)
    windowHeight = int(get_monitors()[0].height/2)

    def __init__(self):
        self._running = True
        self._display = None

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

    def on_loop(self):
        pass

    def on_render(self):
        self._display.fill((255,255,255))
        #render test (testing rendering and player leveling):
        testFont = pygame.font.SysFont('Times New Roman', 30)
        self._display.blit(testFont.render("Player Level: " + str(currentPlayer.level), True, (0,0,0)), (20, 20))
        self._display.blit(testFont.render("Player XP: " + str(currentPlayer.xp), True, (0,0,0)), (20, 100))

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