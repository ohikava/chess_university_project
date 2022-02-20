from Chesspiece import Rook, Queen, Knight, King, Pawn, Bishop


class Chessboard:
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

        self.current_move = 1
        self.queue = True

    # TODO method that checks is it possible to do a move without putting a king under a treat
    def check_is_king_in_safe(self, position, new_position) -> bool:
        enemy_units = {i:v for (i, v) in self.chess_board.items() if v != None and v.fraction != self.queue}
        print(enemy_units)
        pass

    def restart(self):
        self.__init__()

    def move(self, old_position, new_position):
        chesspiece = self.chess_board[old_position]

        if not chesspiece:
            return False, 'Вы не можете пойти пустой клеткой'

        if self.queue != chesspiece.fraction:
            return False, 'Вы не можете пойти чужой фигурой'

        if not (figure_move := chesspiece.move_to(old_position, new_position, self.current_move))[0]:
            return False, figure_move[1]

        for i in figure_move[2]:
            if self.chess_board[i]:
                return False, "Вы не можете пойти сквозь фигуру"

        self.chess_board[new_position] = chesspiece
        self.chess_board[old_position] = None
        self.current_move += 1
        self.queue = not self.queue

        return True, 'Ход завершен'

if __name__ == "__main__":
    cb = Chessboard()
    cb.check_is_king_in_safe(1 + 1j, 1 + 2j)
    cb.move(1 + 2j, 1 + 3j)
    cb.check_is_king_in_safe(1 + 2j, 2 + 3j)
