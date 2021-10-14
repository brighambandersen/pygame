import pygame
import os
from pygame.constants import K_SPACE
from pygame.image import load
from pygame.transform import scale
from pygame.transform import flip

# Initialize game

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
X_MIN = -50
X_MAX = 1650
X_START = 100
Y_MIN = 0
Y_MAX = 645

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg_img = load(os.path.join('assets','background.jpg'))
bg_img = scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

mario_img = load(os.path.join('assets', 'mario.png'))
mario_right = scale(mario_img, (100,100))
mario_left = flip(mario_right, True, False)

curr_mario = mario_right
x_pos = X_START
y_pos = Y_MAX

def move_x(distance):
  global x_pos

  x_pos += distance
  if x_pos > X_MAX:  # If mario goes off screen right
    x_pos = X_MIN
  elif x_pos < X_MIN: # If mario goes off screen left
    x_pos = X_MAX

def move_y(distance):
  global y_pos

  y_pos += distance
  if y_pos > Y_MAX: # Don't let mario go below ground
    y_pos = Y_MAX
  elif y_pos < Y_MIN: # Don't let mario leave top of screen
    y_pos = Y_MIN

# Game loop

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit(0)

  screen.blit(bg_img, (0,0))

  screen.blit(curr_mario, (x_pos,y_pos))

  keys = pygame.key.get_pressed()

  distance = 1

  # Go turbo if they are holding space
  if keys[K_SPACE]:
    distance = 4

  # Move right
  if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
    move_x(distance)
    curr_mario = mario_right

  # Move left
  if keys[pygame.K_a] or keys[pygame.K_LEFT]:
    move_x(-1 * distance)
    curr_mario = mario_left

  # Move up
  if keys[pygame.K_w] or keys[pygame.K_UP]:
    move_y(-1 * distance)

  # Move down
  if keys[pygame.K_s] or keys[pygame.K_DOWN]:
    move_y(distance)

  pygame.display.update()
