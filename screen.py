import pygame

class Screen:
  """
  Object that holds the base Surface object onto which everything is drawn
  """
  def __init__(self, size):
    self.size = size
    self.surface = pygame.display.set_mode(size, pygame.RESIZABLE)
    self.fillColor = (150, 150, 150)
    self.objects = []
  
  def drawBackground(self):
    self.surface.fill(self.fillColor)

  def flip(self):
    pygame.display.flip()

  def drawObjects(self):
    for obj in self.objects:
      obj.draw(self)
  
  def addObject(self, obj):
    self.objects.append(obj)
    obj.calculateSize(self.surface.get_size())
  
  def resizeObjects(self):
    # Resize objects on screen
    for obj in self.objects:
      obj.calculateSize(self.surface.get_size())

  def handleClick(self, pos):
    for obj in self.objects:
      if(obj.rect.collidepoint(pos)):
        obj.handleClick(pos)

  def handleMouseWheel(self, pos, direction):
    for obj in self.objects:
      if(obj.rect.collidepoint(pos)):
        obj.handleMouseWheel(pos, direction)
        obj.calculateSize(self.surface.get_size())