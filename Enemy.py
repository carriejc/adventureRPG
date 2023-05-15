import pygame
import sys
from pygame.locals import *
import random
from Constants import Constants

class Enemies(pygame.sprite.Sprite):
  def __init__(self, height, width):
    super().__init__()  # Always first
    self.image = pygame.Surface([width, height])
    self.Enemy = pygame.image.load("Enemy.png")
    self.Enemy = pygame.transform.scale(self.Enemy, (128, 128))
    self.x = random.randint(0, Constants.WIDTH - width)
    self.y = random.randint(0, Constants.HEIGHT - height)

  # random movement
  def move(self, x, y):
    self.x = self.x + x
    self.y = self.y + y
