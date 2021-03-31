import pygame, sys
from board import Board
from button import Button
from screen import Screen
from callbacks import playCallback, nextCallback, resetCallback

pygame.init()

# Set window structures
screenSize = (700, 700)
clock = pygame.time.Clock()
screen = Screen(screenSize)
board = Board(51)
screen.addObject(board)


screen.addObject(Button("img/play.png", playCallback, [board], 0.2, 0.85))
screen.addObject(Button("img/next.png", nextCallback, [board], 0.5, 0.85))
screen.addObject(Button("img/reset.png", resetCallback, [board], 0.8, 0.85))

# Main event loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.VIDEORESIZE:
      screen.resizeObjects()

    if event.type == pygame.MOUSEWHEEL:
      screen.handleMouseWheel(pygame.mouse.get_pos(), event.y)

    # pygame.mouse.get_pressed returns array of bools for all mouse buttons, true means button is clicked
    if event.type == pygame.MOUSEBUTTONDOWN and True in pygame.mouse.get_pressed():
      screen.handleClick(event.pos)

  board.cycle()
  screen.drawBackground()
  screen.drawObjects()
  screen.flip()
  
  clock.tick(120)