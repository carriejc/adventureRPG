import pygame
import sys
from pygame.locals import *


class Player(pygame.sprite.Sprite):

  def __init__(self, height, width):
    super().__init__()  # Always first
    self.image = pygame.Surface([width, height])
    self.MC = pygame.image.load("MC.png")
    self.MC = pygame.transform.scale(self.MC, (128, 128))
    self.x = 0
    self.y = 0

    # Collision Rectangle
    self.collisionRect = pygame.Rect(self.x, self.y, width, height)

  def move(self, x, y):
    self.x = self.x + x
    self.y = self.y + y
