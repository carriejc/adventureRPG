import pygame
import sys
from pygame.locals import *

# object imports
from Enemy import Enemies
from sword import Sword
from NPC import NPC
from Player import Player
from Constants import Constants

# Setting up the window
WINDOW = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
pygame.display.set_caption('Adventure RPG :)')

pygame.init()

font = pygame.font.Font("pixelizedFont.ttf", 16)
fpsClock = pygame.time.Clock()  # clock
looping = True  # Game Loop

playerObject = Player(128, 128)
enemyObject = Enemies(128, 128)
swordObject = Sword(64, 64)
npcObject = NPC(128, 128)
text = font.render("Welcome to our game", True, (0, 0, 0))

# makes it center aligned and not left aligned
textRect = text.get_rect()
textRect.center = (Constants.WIDTH // 2, 20 // 2)


def update():
  WINDOW.fill(Constants.BACKGROUND_COLOR)
  fpsClock.tick(Constants.FPS)
  WINDOW.blit(playerObject.MC, (playerObject.x, playerObject.y))
  WINDOW.blit(swordObject.sword, (playerObject.x + 70, playerObject.y + 40))
  WINDOW.blit(enemyObject.Enemy, (enemyObject.x, enemyObject.y))
  WINDOW.blit(npcObject.NPC, (npcObject.x, npcObject.y))
  WINDOW.blit(text, textRect)


def checkCollision():
  collidingWithNPC = playerObject.collisionRect.colliderect(
    npcObject.collisionRect)


while looping:
  # Getting Inputs
  # Add events for W,A,S,D or arrow keys (movement)
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:  # if any key is pressed down
      # Movement Keys
      # check if the key pressed is the up key
      if event.key == pygame.K_UP or event.key == pygame.K_w:
        playerObject.move(0, -Constants.STEPS)
      if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        playerObject.move(0, Constants.STEPS)
      if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        playerObject.move(Constants.STEPS, 0)
      if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        playerObject.move(-Constants.STEPS, 0)
        # Interacting Key
      if event.key == pygame.K_e:
        print("interact")

    # for stopping
    if event.type == pygame.KEYUP:  # if any key is pressed down
      # Movement Keys
      # check if the key pressed is the up key
      if event.key == pygame.K_UP or event.key == pygame.K_w:
        playerObject.move(0, -Constants.STEPS)

      if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        playerObject.move(0, Constants.STEPS)

      if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        playerObject.move(Constants.STEPS, 0)
      if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        playerObject.move(-Constants.STEPS, 0)

  update()
  checkCollision()
  pygame.display.update()

#canvas.bind_all('<KeyPress-Left>',self.move_left)
