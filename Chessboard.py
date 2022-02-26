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

    def get_king_position(self):
        for k, v in self.chess_board.items():
            if v and v.fraction == self.queue and v.name == 'k':
                return k

    # TODO method that checks is it possible to do a move without putting a king under a treat
    def is_king_safe(self) -> bool:
        enemy_units = {i: v for (i, v) in self.chess_board.items() if v != None and v.fraction != self.queue}
        king_position = self.get_king_position()
        check_position = lambda x: (
        self.chess_board.get(x), self.chess_board.get(x).fraction if self.chess_board.get(x) else None)

        print(king_position)
        print(enemy_units)

        for k, v in enemy_units.items():
            if king_position in v.get_probable_attack_trajectory(k, check_position):
                return False
        return True

    def restart(self):
        self.__init__()

    def move(self, old_position, new_position) -> (bool, str):
        chesspiece = self.chess_board[old_position]

        if not chesspiece:
            return False, 'Вы не можете пойти пустой клеткой'

        if self.queue != chesspiece.fraction:
            return False, 'Вы не можете пойти чужой фигурой'

        if self.chess_board[new_position]:
            figure_move = chesspiece.attack(old_position, new_position)
        else:
            figure_move = chesspiece.move_to(old_position, new_position, self.current_move)

        if not figure_move[0]:
            return False, figure_move[1]

        for index, i in enumerate(figure_move[2]):
            if self.chess_board[i]:

                if index != len(figure_move[2]) - 1:
                    return False, "Вы не можете пойти сквозь фигуру"

                if self.chess_board[i].fraction == chesspiece.fraction:
                    return False, "Вы не можете аттаковать свою же фигуру"

        self.chess_board[new_position] = chesspiece
        self.chess_board[old_position] = None
        self.current_move += 1
        self.queue = not self.queue

        return True, 'Ход завершен'


if __name__ == "__main__":
    cb = Chessboard()
    template = lambda x: (cb.chess_board.get(x), cb.chess_board.get(x).fraction if cb.chess_board.get(x) else None)
    white_n = Knight(True)
    cb = Chessboard()
    cb.move(2 + 2j, 2 + 4j)
    cb.move(2 + 7j, 2 + 5j)
    cb.move(3 + 1j, 2 + 2j)
    cb.move(1 + 7j, 1 + 6j)
    cb.move(2 + 2j, 5 + 5j)
    print(white_n.get_probable_attack_trajectory(2 + 1j, template))
    print(cb.is_king_safe())
