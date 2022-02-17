from Chesspiece import Rook, Queen, Knight, King, Pawn, Bishop
from utilities import complex_number_2_chess_notation


class Chess:
    def __init__(self):
        self.chess_board = {
            complex(k, v): None for k in range(1, 9) for v in range(1, 9)
        }
        for i in range(1, 9):
            self.chess_board[complex(i, 2)] = Pawn(True)
            self.chess_board[complex(i, 7)] = Pawn(False)

        self.chess_board[1 + 1j] = Rook(True)
        self.chess_board[2 + 1j] = Knight(True)
        self.chess_board[3 + 1j] = Bishop(True)
        self.chess_board[4 + 1j] = Queen(True)
        self.chess_board[5 + 1j] = King(True)
        self.chess_board[6 + 1j] = Bishop(True)
        self.chess_board[7 + 1j] = Knight(True)
        self.chess_board[8 + 1j] = Rook(True)

        self.chess_board[1 + 8j] = Rook(False)
        self.chess_board[2 + 8j] = Knight(False)
        self.chess_board[3 + 8j] = Bishop(False)
        self.chess_board[4 + 8j] = Queen(False)
        self.chess_board[5 + 8j] = King(False)
        self.chess_board[6 + 8j] = Bishop(False)
        self.chess_board[7 + 8j] = Knight(False)
        self.chess_board[8 + 8j] = Rook(False)

    def restart(self):
        self.__init__()

    def render_chessboard(self):
        print('  ', end=" ")
        for k in range(1, 9):
            print(complex_number_2_chess_notation(complex(k, 0)) + "", end=" ")
        print(" ")
        for i in range(8, 0, -1):
            print(i, end="  ")
            for k in range(1, 9):
                if self.chess_board[complex(k, i)]:
                    print(self.chess_board[complex(k, i)], end=" ")
                else:
                    print(".", end=" ")
            print(" " + str(i))
        print('  ', end=" ")
        for k in range(1, 9):
            print(complex_number_2_chess_notation(complex(k, 0)), end=" ")


if __name__ == "__main__":
    cb = Chess()
    cb.render_chessboard()
