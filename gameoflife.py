import pygame, sys

class Board:
  def __init__(self, n):
    # Initialize empty n x n grid
    self.grid = []
    for x in range(n):
      self.grid.append([])
      for y in range(n):
        self.grid[x].append(False)

    self.n = n
    self.rect = None
    self.height = 0
    self.backgroundColor = (255, 255, 255)
    self.top = 20
    self.left = 0
    self.lineColor = (0, 0, 0)
    self.squareFillColor = (0, 0, 0)
  
  def calculateSize(self, screenSize):
    # Height and width are equal to 75% of window height
    idealHeight = int(0.75 * screenSize[1])
    lineSpacing = int(idealHeight / self.n)
    self.height = lineSpacing * self.n

    self.left = screenSize[0]/2 - self.height/2
    self.rect = pygame.Rect(self.left, self.top, self.height, self.height)
  
  def draw(self, screen):
    pygame.draw.rect(screen.surface, self.backgroundColor, self.rect)
    lineSpacing = self.height / self.n
    for i in range(self.n):
      lineLeft = self.left + (i * lineSpacing)
      # Draw vertical line
      pygame.draw.line(screen.surface, self.lineColor, (lineLeft, self.top), (lineLeft, self.top + self.height))

      lineTop = self.top + (i * lineSpacing)
      # Draw horizontal line,
      pygame.draw.line(screen.surface, self.lineColor, (self.left, lineTop), (self.left + self.height, lineTop))
    
    # Draw horizontal and vertical lines at very end
    pygame.draw.line(screen.surface, self.lineColor, (self.left + self.height, self.top), (self.left + self.height, self.top + self.height))
    pygame.draw.line(screen.surface, self.lineColor, (self.left, self.top + self.height), (self.left + self.height, self.top + self.height))

    # Draw 'alive' cells
    for x in range(self.n):
      for y in range(self.n):
        if(self.grid[x][y]):
          cellRect = pygame.Rect(self.left + (x * lineSpacing), self.top + (y * lineSpacing), lineSpacing, lineSpacing)
          pygame.draw.rect(screen.surface, self.squareFillColor, cellRect)
      
  def handleClick(self, surface, pos):
    # Mark/Unmark the clicked cell on the board
    relativeX = pos[0] - self.left
    relativeY = pos[1] - self.top
    lineSpacing = self.height / self.n
    indexX = int(relativeX / lineSpacing)
    indexY = int(relativeY / lineSpacing)
    self.grid[indexX][indexY] = not self.grid[indexX][indexY]

class Screen:
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
    for obj in self.objects:
      obj.calculateSize(self.surface.get_size())

  def handleClick(self, pos):
    for obj in self.objects:
      if(obj.rect.collidepoint(pos)):
        obj.handleClick(self, pos)


pygame.init()

size = width, height = 320, 240
gridSize = (700, 700)
clock = pygame.time.Clock()
screen = Screen(gridSize)
screen.addObject(Board(25))
while True:
  for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()

      if event.type == pygame.VIDEORESIZE:
        screen.resizeObjects()

      if event.type == pygame.MOUSEBUTTONUP:
        screen.handleClick(event.pos)

  screen.drawBackground()
  screen.drawObjects()
  screen.flip()

  clock.tick(120)