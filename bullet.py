import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    #************************************************************************#
    #                     __init__(self, ai_game)                            #
    #************************************************************************#
    def __init__(self, ai_game):

        super().__init__()
        self.screen   = ai_game.screen
        self.settings = ai_game.settings
        self.color    = self.settings.bullet_color

        # The bullet is fired from the ship
        self.rect        = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)


    #************************************************************************#
    #                     update(self)                                       #
    #************************************************************************#
    def update (self):

        self.y     -= self.settings.bullet_speed
        self.rect.y = self.y


    #************************************************************************#
    #                     draw_bullet(self)                                  #
    #************************************************************************#
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)