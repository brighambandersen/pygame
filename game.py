import pygame
import os
from pygame.image import load
from pygame.transform import scale

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg_img = load(os.path.join('assets','background.jpg'))
bg_img = scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

mario = load(os.path.join('assets', 'mario.png'))
mario = scale(mario, (100,100))

mario_x_pos = 100

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit(0)

  screen.blit(bg_img, (0,0))

  screen.blit(mario, (mario_x_pos,645))

  keys = pygame.key.get_pressed()

  if keys[pygame.K_d]:
    mario_x_pos += 1

  if keys[pygame.K_a]:
    mario_x_pos -= 1

  if mario_x_pos >= 1650:
    mario_x_pos = -30
  if mario_x_pos <= -50:
    mario_x_pos = 1650

  pygame.display.update()