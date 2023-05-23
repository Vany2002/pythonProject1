class Board:
    def __init__(self):
        self.board = {
                "1.1": " ", "1.2": " ", "1.3": " ",
                "2.1": " ", "2.2": " ", "2.3": " ",
                "3.1": " ", "3.2": " ", "3.3": " "}

    def printBoard(self):
        print(self.board["1.1"] + "|" + self.board["1.2"] + "|" + self.board["1.3"])
        print("-+-+-")
        print(self.board["2.1"] + "|" + self.board["2.2"] + "|" + self.board["2.3"])
        print("-+-+-")
        print(self.board["3.1"] + "|" + self.board["3.2"] + "|" + self.board["3.3"])

    def isValidMove(self, position):
        if self.board[position] == " ":
            return True
        return False

    def changeBoard(self, position, type):
        if self.isValidMove(position):
            self.board[position] = type
            return self.board
        return None

    def isWinner(self, player):
        if self.board["1.1"] == player.type and self.board["1.2"] == player.type and self.board["1.3"] == player.type or \
        self.board["2.1"] == player.type and self.board["2.2"] == player.type and self.board["2.3"] == player.type or \
        self.board["3.1"] == player.type and self.board["3.2"] == player.type and self.board["3.3"] == player.type or \
        self.board["1.1"] == player.type and self.board["2.1"] == player.type and self.board["3.1"] == player.type or \
        self.board["1.2"] == player.type and self.board["2.2"] == player.type and self.board["3.2"] == player.type or \
        self.board["1.3"] == player.type and self.board["2.3"] == player.type and self.board["3.3"] == player.type or \
        self.board["1.1"] == player.type and self.board["2.2"] == player.type and self.board["3.3"] == player.type or \
        self.board["3.1"] == player.type and self.board["2.2"] == player.type and self.board["1.3"] == player.type:
            return True
        return False


class Player:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return "Player {}".format(self.type)


class Game:
    def __init__(self):
        self.firstPlayer = Player("X")
        self.secondPlayer = Player("O")
        self.board = Board()

    def printValidEntries(self):
        print("""
            1.1 | 1.2 | 1.3
            2.1 | 2.2 | 2.3 
            3.1 | 3.2 | 3.3 """)

    def printingBoard(self):
        self.board.printBoard()

    def changeTurn(self, player):
        if player == self.firstPlayer:
            return self.secondPlayer
        else:
            return self.firstPlayer

    def wonGame(self, player):
        return self.board.isWinner(player)

    def modifyBoard(self, position, type):
        if self.board.changeBoard(position, type) is not None:
            return self.board.changeBoard(position, type)
        else:
            position = input("Choose another position: ")
            return self.board.changeBoard(position, type)


def play():
    game = Game()
    game.printValidEntries()
    player = game.firstPlayer
    number = 9
    while number > 0:
        number -= 1
        game.printingBoard()
        position = input("{} next move: ".format(player))
        game.modifyBoard(position, player.type)
        if game.wonGame(player):
            print("{} winner!".format(player))
            break
        else:
            player = game.changeTurn(player)
    if number == 0:
        print("Game over!")

play()
