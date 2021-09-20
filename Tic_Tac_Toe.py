#board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |  |')
    print(' ' + board[1] + ' |' + board[2] + ' |' + board[3])
    print('   |  |')
    print('----------')
    print('   |  |')
    print(' ' + board[4] + ' |' + board[5] + ' |' +board[6])
    print('   |  |')
    print('----------')
    print('   |  |')
    print(' ' + board[7] + ' |' +board[8] + ' |' + board[9])
    print('   |  |')

def isWinner(bo, le):
    # reture True or False, bo=board,le=letter 
    return ((board[1] == le and board[2] == le and board[3] == le) or
           (board[4] == le and board[5] == le and board[6] == le) or
           (board[7] == le and board[8] == le and board[9] == le) or
           (board[1] == le and board[5] == le and board[9] == le) or
           (board[3] == le and board[5] == le and board[7] == le) or
           (board[1] == le and board[4] == le and board[7] == le) or 
           (board[2] == le and board[5] == le and board[8] == le) or
           (board[3] == le and board[6] == le and board[9] == le))
           
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def playMove():
    run = True
    while run:
      move = input('please select a postion to place \'X\' (1-9): ')
      try:
        move = int(move)
        if move > 0 and move < 10:
          if spaceIsFree(move):
            run = False
            insertLetter('X', move)
          else:
            print('This postion is already occupied!')
        else:
            print('Please type a number within the range!')
      except:
        print('Please type a number!')     

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def compMove():    
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornerOpen = []
    for i in possibleMoves:
      if i in [1,3,7,9]:
         cornerOpen.append(i)
    if len(cornerOpen) > 0:
       move = selectRandom(cornerOpen)
       return move

    if 5 in possibleMoves:
       move = 5
       return move

    edgesOpen = []
    for i in possibleMoves:
      if i in [2,4,6,8]:
         edgesOpen.append(i)

    if len(edgesOpen) > 0:
       move = selectRandom(edgesOpen)
    return move

def main():
    printBoard(board)

    while not(isBoardFull(board)):    
        if not(isWinner(board, 'O')):
          playMove()
          printBoard(board)
        else:
          print('O\'s win this time...')
          break

        if not(isWinner(board, 'X')):
           move = compMove()        
           if move == 0:
              print('Game is a Tie! No more spaces left to move.')
           else:
              insertLetter('O', move)  
              print('Computer placed an \'O\' in position', move, ':')
              printBoard(board)
        else:
           print('X\'s win, good job!')
           break

    if isBoardFull(board):
      print('Game is a tie! No more spaces left to move.')             

while True:
   answer = input('do you want to play game? (Y/N)')
   if answer.lower() == 'y' or answer.lower() == 'yes':
      board = [' ' for x in range(10)]
      print('------------------------------------------')
      main()
   else:
      break