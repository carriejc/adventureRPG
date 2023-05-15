import pygame
import sys
from pygame.locals import *


class NPC(pygame.sprite.Sprite):

  def __init__(self, height, width):
    super().__init__()  # Always first
    self.image = pygame.Surface([width, height])
    self.NPC = pygame.image.load("NPC.png")
    self.NPC = pygame.transform.scale(self.NPC, (128, 128))
    self.x = 250
    self.y = 100

    # Collision Rectangle
    self.collisionRect = pygame.Rect(self.x, self.y, width, height)

  def move(self, x, y):
    self.x = self.x + x
    self.y = self.y + y
