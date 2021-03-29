def playCallback(args):
  button = args[0]
  board = args[1]

  # If board is playing, change button image to 'play' and pause board
  if(board.autoPlay):
    board.autoPlay = False
    button.loadImage("img/play.png")

  # Otherwise, change button image to 'pause' and start autoplay
  else:
    board.autoPlay = True
    button.loadImage("img/pause.png")

def nextCallback(args):
  board = args[1]
  board.advanceState()

def resetCallback(args):
  board = args[1]
  board.initializeGrid()