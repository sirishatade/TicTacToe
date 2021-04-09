import string as str


class TicTacToe:

    def __init__(self):
        """ Initializes empty board, with index for every space on board as the keys """
        self.board = {1: " ", 2: " ", 3: " ",
                      4: " ", 5: " ", 6: " ",
                      7: " ", 8: " ", 9: " "}

    def print_board(self):
        """ Prints the game board at its most recent state. The board will print after every new move """
        top_row = self.board.get(1) + " | " + self.board.get(2) + " | " + self.board.get(3)
        middle_row = self.board.get(4) + " | " + self.board.get(5) + " | " + self.board.get(6)
        bottom_row = self.board.get(7) + " | " + self.board.get(8) + " | " + self.board.get(9)

        print(top_row)
        print("---------")
        print(middle_row)
        print("---------")
        print(bottom_row)

    def start_game(self):
        """ This is the driver function of the game. Sets up the initial display and plays the game until someone wins
        or there is a tie """
        input("Welcome to TicTacToe! This game requires 2 players. Enter any button to continue:")
        print("Here is the board with the position numbers. When it is your turn, select the position you want:")
        print("""
                1 | 2 | 3
                ---------
                4 | 5 | 6
                ---------
                7 | 8 | 9""")

        while not self.game_over():
            self.play_game("X")
            if self.game_over():
                break
            self.play_game("O")

        print("Game over!")

    def play_game(self, player):
        """ Checks for valid input from player and fills the board based on player's desired positions, then prints
        the board """
        pos = input(f"Player {player}, please enter your desired position: ").strip()
        while not self.is_valid_input(pos):
            pos = input("Please enter a valid position: ").strip()
        self.board[int(pos)] = player
        self.print_board()

    def is_valid_input(self, pos):
        """ User input sanity check """
        if pos not in str.digits:
            return False
        elif int(pos) > 9 or int(pos) < 1:
            return False
        elif self.board.get(int(pos)) != " ":
            print("That position is already taken!!")
            return False
        return True

    def game_over(self):
        """ Enumerates all conditions in which someone wins or there is a tie, and returns True if the game is over
        and False if not """

        if self.board[1] == self.board[4] == self.board[7] != " ":
            print(f"{self.board[1]} WINS!")
            return True
        elif self.board[2] == self.board[5] == self.board[8] != " ":
            print(f"{self.board[2]} WINS!")
            return True
        elif self.board[3] == self.board[6] == self.board[9] != " ":
            print(f"{self.board[3]} WINS!")
            return True
        elif self.board[1] == self.board[2] == self.board[3] != " ":
            print(f"{self.board[1]} WINS!")
            return True
        elif self.board[4] == self.board[5] == self.board[6] != " ":
            print(f"{self.board[4]} WINS!")
            return True
        elif self.board[7] == self.board[8] == self.board[9] != " ":
            print(f"{self.board[7]} WINS!")
            return True
        elif self.board[1] == self.board[5] == self.board[9] != " ":
            print(f"{self.board[1]} WINS!")
            return True
        elif self.board[3] == self.board[5] == self.board[7] != " ":
            print(f"{self.board[3]} WINS!")
            return True
        elif all(value != " " for value in self.board.values()):
            print("It's a tie!")
            return True
        return False


t = TicTacToe()
t.start_game()
