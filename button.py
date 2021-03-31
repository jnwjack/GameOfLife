import pygame
from screen_object import ScreenObject

BUTTON_SIZE = 75

class Button(ScreenObject):
  """
  Generic object for button at the bottom of the screen. Also handles the drawing of the button
  onto the screen.
  """
  def __init__(self, imageFilename, callback, callbackArguments, relativeLeft, relativeTop):
    self.callback = callback
    # Arguments to pass for callback function
    self.callbackArguments = [self] + callbackArguments 
    self.image = None
    self.loadImage(imageFilename)
    self.rect = self.image.get_rect()

    # Percentage of width, height of at which the top left corner should be placed
    self.relativeLeft = relativeLeft
    self.relativeTop = relativeTop

  def calculateSize(self, screenSize):
    destinationLeft = screenSize[0] * self.relativeLeft
    destinationTop = screenSize[1] * self.relativeTop
    
    self.rect.move_ip((destinationLeft - self.rect.x -BUTTON_SIZE / 2 , destinationTop - self.rect.y - BUTTON_SIZE / 2))

  def draw(self, screen):
    screen.surface.blit(self.image, self.rect)

  def handleClick(self, pos):
    self.callback(self.callbackArguments)

  # Do nothing for buttons
  def handleMouseWheel(self, pos, direction):
    pass

  def loadImage(self, filename):
    self.image = pygame.image.load(filename).convert()
    self.image = pygame.transform.scale(self.image, (BUTTON_SIZE, BUTTON_SIZE))
