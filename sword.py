import pygame
import sys
from pygame.locals import *


class Sword(pygame.sprite.Sprite):
  def __init__(self,height,width):
    super().__init__() # Always first 
    self.image = pygame.Surface([width,height])
    self.sword = pygame.image.load("Psword.png")
    self.sword = pygame.transform.scale(self.sword, (64, 64))
    self.x = 20;
    self.y = 0;
  
  def move(self, x, y):
    self.x = self.x + x;
    self.y = self.y + y;


