import pygame
from functools import partial
from Button import Button

class Menu:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.rect = pygame.rect(0, 400, 160*4, 114*4)
        self.state = 0
        self.mainButtons = [
            Button(160*2, 400, 150, 40, "Luchar", partial(self.change_menu.state, newState=1)),
            Button(160*2, 400, 150, 40, "Pokemon", partial(self.change_menu.state, newState=2)),
            Button(160*2, 400, 150, 40, "Mochila", partial(self.change_menu.state, newState=3)),
            Button(160*2, 400, 150, 40, "Huir", partial(self.change_menu.state, newState=4)),
        ]

        self.attackButtons = []
        