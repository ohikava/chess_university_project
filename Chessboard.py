from Chesspiece import Rook, Queen, Knight, King, Pawn, Bishop
from utilities import complex_number_2_chess_notation


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
        #dsfs
        self.queue = True
        self.last_move = None
        self.castling = {
            True: True,
            False: True
        }

    def get_king_position(self):
        for k, v in self.chess_board.items():
            if v and v.fraction == self.queue and v.name == 'k':
                return k

    def check_position(self, position):
        chesspiece = self.chess_board.get(position)
        return chesspiece, chesspiece.fraction if chesspiece else None

    def is_king_safe(self) -> (bool, complex):
        enemy_units = {i: v for (i, v) in self.chess_board.items() if v != None and v.fraction != self.queue}
        king_position = self.get_king_position()

        for k, v in enemy_units.items():
            if king_position in v.get_probable_attack_trajectory(k, self.check_position):
                return False, k
        return True, None

    def check_checkmate(self):
        units = {i: v for (i, v) in self.chess_board.items() if v != None and v.fraction == self.queue}
        possible_solutions = set()
        for u_position, u in units.items():
            possible_moves = u.get_probable_attack_trajectory(u_position, self.check_position)

            if hasattr(u, 'get_probable_trajectory'):
                possible_moves |= u.get_probable_trajectory(u_position, self.check_position)

            for i in possible_moves:
                if self.check_move(u_position, i):
                    possible_solutions.add((u_position, i))

        return False if len(possible_solutions) > 0 else True, possible_solutions

    def check_move(self, position, new_position) -> bool:
        # True if you can make a move, False if not
        result = True

        old = self.chess_board[position]
        new = self.chess_board[new_position]

        self.chess_board[new_position] = self.chess_board[position]
        self.chess_board[position] = None

        if not self.is_king_safe()[0]:
            result = False

        self.chess_board[position] = old
        self.chess_board[new_position] = new

        return result

    def restart(self):
        self.__init__()

    def make_castling(self, position, new_position):

        if not self.is_king_safe()[0]:
            return False

        iter_position = position
        chesspiece = self.chess_board[position]

        if self.chess_board[new_position + 1].name != 'r':
            return False

        while iter_position != new_position:
            iter_position += 1
            if self.chess_board[iter_position]:
                return False

            self.chess_board[iter_position] = chesspiece
            self.chess_board[position] = None
            if not self.is_king_safe()[0]:
                self.chess_board[position] = chesspiece
                self.chess_board[iter_position] = None
                return False
        self.chess_board[iter_position - 1] = self.chess_board[iter_position + 1]
        self.chess_board[iter_position + 1] = None
        self.last_move = (position, new_position)
        self.current_move += 1
        self.queue = not self.queue

        return True

    def update_pawn(self, position: complex, chesspiece: str) -> (bool, str):
        match chesspiece:
            case 'Пешка':
                new_chesspiece = Pawn(not self.queue)
            case 'Слон':
                new_chesspiece = Bishop(not self.queue)
            case 'Ладья':
                new_chesspiece = Rook(not self.queue)
            case 'Конь':
                new_chesspiece = Knight(not self.queue)
            case 'Ферзь':
                new_chesspiece = Queen(not self.queue)
            case 'Король':
                return False, 'Вы не можете получить еще одного короля'
            case _:
                return False, 'Нет такой фигуры'

        self.chess_board[position] = new_chesspiece
        return True, ''

    def make_en_passant(self, position, new_position):
        if not self.last_move:
            return False

        if not self.is_king_safe()[0]:
            return False

        chesspiece = self.chess_board[position]
        last_old_position, last_new_position = self.last_move[0], self.last_move[1]
        attacked_chesspiece = self.chess_board[last_new_position]
        sign = 1 if attacked_chesspiece.fraction else -1
        if attacked_chesspiece.name == 'p' and abs(last_new_position.imag - last_old_position.imag) == 2 \
                and chesspiece.attack(position, new_position) \
                and (last_new_position - complex(0, sign)) == new_position:
            self.chess_board[last_new_position] = None
            self.chess_board[new_position] = self.chess_board[position]
            self.chess_board[position] = None

            if not self.is_king_safe()[0]:
                self.chess_board[position] = chesspiece
                self.chess_board[new_position] = None
                self.chess_board[last_new_position] = attacked_chesspiece
                return False

            self.last_move = (position, new_position)
            self.current_move += 1
            self.queue = not self.queue
            return True
        return False

    def move(self, old_position, new_position) -> (bool, str):
        chesspiece = self.chess_board[old_position]

        if not chesspiece:
            return False, 'Вы не можете пойти пустой клеткой'

        if self.queue != chesspiece.fraction:
            return False, 'Вы не можете пойти чужой фигурой'

        if chesspiece.name == 'p' and self.make_en_passant(old_position, new_position):
            return True, 'Ход завершен'

        if chesspiece.name == 'k' and self.castling[self.queue] and self.make_castling(old_position, new_position):
            return True, 'Ход завершен'

        if self.chess_board[new_position]:
            figure_move = chesspiece.attack(old_position, new_position)
        else:
            figure_move = chesspiece.move_to(old_position, new_position)

        if not figure_move[0]:
            return False, figure_move[1]

        for index, i in enumerate(figure_move[2]):
            if self.chess_board[i]:

                if index != len(figure_move[2]) - 1:
                    return False, "Вы не можете пойти сквозь фигуру"

                if self.chess_board[i].fraction == chesspiece.fraction:
                    return False, "Вы не можете аттаковать свою же фигуру"

        if not self.is_king_safe()[0] and not self.check_move(old_position, new_position):
            return False, "Вы не можете так ходить, пока вам стоит шах"

        if chesspiece.name == 'k' or chesspiece.name == 'r' and old_position.real == 8:
            self.castling[self.queue] = False

        self.chess_board[new_position] = chesspiece
        self.chess_board[old_position] = None
        self.last_move = (old_position, new_position)
        self.current_move += 1
        self.queue = not self.queue

        if not (check := self.is_king_safe())[0]:

            checkmate = self.check_checkmate()
            if checkmate[0]:
                return True, f"Игра завершена, {'Белым поставлен мат' if self.queue else 'Чёрным поставлен мат'}"

            return True, f'Шах от фигуры с позиции {complex_number_2_chess_notation(check[1])}'

        if chesspiece.name == 'p' and new_position.imag in {1, 8}:
            return True, "Выберите желаемую фигуру"
        return True, 'Ход завершен'


if __name__ == "__main__":
    cb = Chessboard()
    print(cb.check_checkmate())
