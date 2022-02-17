from Chessboard import Chessboard
from utilities import complex_number_2_chess_notation, chess_notation_2_complex_number
import os

class Cli:
    def __init__(self):
        self.chessboard = Chessboard()

    def render_chessboard(self):
        print('  ', end=" ")
        for k in range(1, 9):
            print(complex_number_2_chess_notation(complex(k, 0)) + "", end=" ")
        print(" ")
        for i in range(8, 0, -1):
            print(i, end="  ")
            for k in range(1, 9):
                if self.chessboard.chess_board[complex(k, i)]:
                    print(self.chessboard.chess_board[complex(k, i)], end=" ")
                else:
                    print(".", end=" ")
            print(" " + str(i))
        print('  ', end=" ")
        for k in range(1, 9):
            print(complex_number_2_chess_notation(complex(k, 0)), end=" ")
        print("")

    def get_command(self):
        while True:
            input_command = input("Введите команду в шахмотной нотации: ").split('--')

            first_position, second_position = input_command[0], input_command[1]

            respond = self.chessboard.move(chess_notation_2_complex_number(first_position),
                                           chess_notation_2_complex_number(second_position))

            if respond[0]:
                os.system('cls')
                self.render_chessboard()

            print(respond[1])

if __name__ == "__main__":
    new_cli = Cli()
    new_cli.render_chessboard()
    new_cli.get_command()