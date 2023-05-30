class Board:
    def __init__(self):
        self.cells = []

    def startGame(self):
        print("Welcome to game!")
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def checkWinners(self, player):
        if (self.cells[0] == self.cells[1] == self.cells[2] and self.cells[0] == player) or (self.cells[0] == self.cells[3] == self.cells[6] and self.cells[0] == player) or (self.cells[0] == self.cells[4] == self.cells[8] and self.cells[0] == player) or (self.cells[2] == self.cells[5] == self.cells[8] and self.cells[2] == player) or (self.cells[2] == self.cells[4] == self.cells[6] and self.cells[2] == player) or (self.cells[6] == self.cells[7] == self.cells[8] and self.cells[6] == player):
            print(f"{player} has won the game! \n", "Thanks for playing")
            return False
        else:
            if self.cells.count(" ") == 0:
                print("No winners! You both losers!")
            return True

    def turn(self, player):
        print(f"What is {player}'s move? (1-9)\n")
        n = int(input())
        if 10 > n > 0:
            cel = self.cells[n-1]
            if cel != " ":
                print("That cell is engaged!")
                return False
            else:
                self.cells[n-1] = player
                return True
        else:
            print("Wrong cell's number!")
            return False

    def drowBoard(self):
        board = [
            [self.cells[0], "|", self.cells[1], "|", self.cells[2]],
            ["-", "+", "-", "+", "-"],
            [self.cells[3], "|", self.cells[4], "|", self.cells[5]],
            ["-", "+", "-", "+", "-"],
            [self.cells[6], "|", self.cells[7], "|", self.cells[8]],
        ]
        for i in board:
            print(i[0], i[1], i[2], i[3], i[4], sep="")
