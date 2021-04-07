import pygame
from screen_object import ScreenObject

MIN_N = 1
MAX_N = 100

class Board(ScreenObject):
  """
  Object that holds state of the grid as a 2D array. Also handles the drawing of the
  grid onto the screen.
  """
  def __init__(self, n):
    self.n = n
    self.rect = None
    self.grid = []
    self.height = 0
    self.backgroundColor = (255, 255, 255)
    self.top = 20
    self.left = 0
    self.lineColor = (0, 0, 0)
    self.squareFillColor = (0, 0, 0)

    self.autoPlay = False

    self.delay = 25
    self.tick = 0

    # Store 'alive' indexes in set
    self.aliveCellCoords = set()
    self.origin = (0, 0)
    self.offset = int(self.n / 2)

  
  def initializeGrid(self):
    # Create n x n grid
    self.aliveCellCoords = set()

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

    # Draw 'alive' cells that are within the viewing window
    for (cartesianX, cartesianY) in self.aliveCellCoords:
      (indexX, indexY) = self.cartesianToBoardIndex((cartesianX, cartesianY))
      # If cell is outside viewing window, skip drawing it
      if(indexX < 0 or indexX >= self.n or indexY < 0 or indexY >= self.n):
        continue
      cellRect = pygame.Rect(self.left + (indexX * lineSpacing), self.top + (indexY * lineSpacing), lineSpacing, lineSpacing)
      pygame.draw.rect(screen.surface, self.squareFillColor, cellRect)
      
  def handleClick(self, pos):
    # Mark/Unmark the clicked cell on the board
    relativeX = pos[0] - self.left
    relativeY = pos[1] - self.top
    lineSpacing = self.height / self.n
    indexX = int(relativeX / lineSpacing)
    indexY = int(relativeY / lineSpacing)

    (cartesianX, cartesianY) = self.boardIndexToCartesian((indexX, indexY))
    if((cartesianX, cartesianY) in self.aliveCellCoords):
      self.aliveCellCoords.remove((cartesianX, cartesianY))
    else:
      self.aliveCellCoords.add((cartesianX, cartesianY))

  def handleMouseWheel(self, pos, direction):
    # Zoom in/out by 10 cells, set offset to match
    lineSpacing = self.height / self.n
    newN = self.n + direction
    if(newN <= MAX_N and newN >= MIN_N):
      self.n += 10 * direction
      self.offset = int(self.n / 2)
  
  def cycle(self):
    if(self.autoPlay):
      self.tick += 1
      if(self.tick == self.delay):
        self.advanceState()
        self.tick = 0

  def boardIndexToCartesian(self, pos):
    x = pos[0] - self.offset + self.origin[0]
    y = pos[1] - self.offset + self.origin[1]
    return (x, y)
  
  def cartesianToBoardIndex(self, pos):
    x = pos[0] + self.offset - self.origin[0]
    y = pos[1] + self.offset - self.origin[1]
    return (x, y)

  def getPositionAfterWrap(self, point):
    upperBound = int(MAX_N / 2)
    lowerBound = upperBound * -1
    if(point > upperBound):
      return lowerBound
    if(point < lowerBound):
      return upperBound
    return point

  def getNeighbors(self, coords):
    neighborOffsets = [
      (offsetX, offsetY)
      for offsetX in range(-1, 2)
      for offsetY in range(-1, 2)
    ]
    neighborOffsets.remove((0,0))
    neighbors = [(self.getPositionAfterWrap(coords[0] + x), self.getPositionAfterWrap(coords[1] + y)) for (x, y) in neighborOffsets]

    return neighbors


  def advanceState(self):
    # TODO: Implement the logic for Game of Life
    nextState = set()

    neighborEncounters = dict()
    for coord in self.aliveCellCoords:
      neighbors = self.getNeighbors(coord)

      for neighbor in neighbors:
        if not neighbor in neighborEncounters:
          neighborEncounters[neighbor] = 1
        else:
          neighborEncounters[neighbor] += 1

      aliveNeighbors = len([
        neighbor
        for neighbor in neighbors
        if neighbor in self.aliveCellCoords
      ])

      if(aliveNeighbors in set([2,3])):
        nextState.add(coord)
    
    for neighbor in neighborEncounters:
      if(neighborEncounters[neighbor] == 3):
        nextState.add(neighbor)
      
    self.aliveCellCoords = nextState
    


      


    

    