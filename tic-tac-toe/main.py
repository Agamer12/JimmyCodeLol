from lib import *
import random

def main():
  boardState = [0,0,0,0,0,0,0,0,0]

  while True:
    while True:
      playerInput = input("Your Move: (1-9)")

      if boardState[playerInput] == 0:
        boardState[playerInput] = 1
        break
      else:
        print("Invalid Move!")

    printBoard(boardState)
    if checkWin(boardState):
      print("You Win!")
      break

    while True:
      cpuInput = random(1, 9)

      if boardState[cpuInput] == 0:
        boardState[cpuInput] = 2
        break

    printBoard(boardState)
    if checkWin(boardState):
      print("You Lose...")
      break
    

if __name__ == "__main__":
    main()

