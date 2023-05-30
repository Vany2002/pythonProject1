from Practika2.Pr_13.Pr13_Task_3 import Board

b = Board()
b.startGame()
b.drowBoard()
player = ["X", "0"]
i = 0
while b.checkWinners(player[i % 2]):
    b.turn(player[i % 2])
    if b.checkWinners(player[i % 2]):
        b.drowBoard()
        i += 1
    else:
        b.drowBoard()
        break