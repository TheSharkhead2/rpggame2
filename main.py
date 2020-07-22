#main file
#information:
#citations in comments (links provided)
#libraries used in "dependencies.txt"
#relying on pygame for visual library

import pygame, sys
from pygame.locals import *
from screeninfo import get_monitors #found in: https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python

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

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display.fill((255,255,255))
        #render test:
        testFont = pygame.font.SysFont('Times New Roman', 30)
        self._display.blit(testFont.render("Hello World", True, (0,0,0)), testFont.render("Hello World", True, (0,0,0)).get_rect())

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
        self.on_quit()


Game().on_execute()