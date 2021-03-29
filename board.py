import pygame

class Board:
  """
  Object that holds state of the grid as a 2D array. Also handles the drawing of the
  grid onto the screen.
  """
  def __init__(self, n):
    self.n = n
    self.rect = None
    self.height = 0
    self.backgroundColor = (255, 255, 255)
    self.top = 20
    self.left = 0
    self.lineColor = (0, 0, 0)
    self.squareFillColor = (0, 0, 0)

    self.autoPlay = False

    self.delay = 50
    self.tick = 0

    self.initializeGrid()
  
  def initializeGrid(self):
    # Create n x n grid
    self.grid = []
    for x in range(self.n):
      self.grid.append([])
      for y in range(self.n):
        self.grid[x].append(False)

  
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
  
  def cycle(self):
    if(self.autoPlay):
      self.tick += 1
      if(self.tick == self.delay):
        self.advanceState()
        self.tick = 0

  def advanceState(self):
    # TODO: Implement the logic for Game of Life

    pass

    

    