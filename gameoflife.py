import pygame, sys
from board import Board
from button import Button
from screen import Screen
from callbacks import playCallback, nextCallback, resetCallback

pygame.init()

size = width, height = 320, 240
gridSize = (700, 700)
clock = pygame.time.Clock()
screen = Screen(gridSize)
board = Board(50)
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

    if event.type == pygame.MOUSEBUTTONUP:
      screen.handleClick(event.pos)

  board.cycle()
  screen.drawBackground()
  screen.drawObjects()
  screen.flip()
  
  clock.tick(120)