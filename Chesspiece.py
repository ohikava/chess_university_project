class Chesspiece:
    def __init__(self, name, fraction, position):
        self.name = name
        self.fraction = fraction
        self.position = position

    def __str__(self):
        return self.name.upper() if self.fraction else self.name


class Pawn(Chesspiece):
    def __init__(self, fraction, position):
        super().__init__('p', fraction, position)

    def move_to(self, newPosition, first_move=False):
        # one_step_up = self.position[0] + str(int(self.position[1]) + 1)
        #
        # if one_step_up == newPosition:
        #     self.position = newPosition
        #     return True
        #
        # if first_move and self.fraction and \
        #         (two_steps_up := self.position[0] + str(int(self.position[1]) + 2)) == newPosition:
        #     self.position = newPosition
        #     return True
        #
        # return False
        pass


class Bishop(Chesspiece):
    def __init__(self, fraction, position):
        super().__init__('b', fraction, position)


class Knight(Chesspiece):
    def __init__(self, fraction, position):
        super().__init__('n', fraction, position)


class Rook(Chesspiece):
    def __init__(self, fraction, position):
        super().__init__('r', fraction, position)


class Queen(Chesspiece):
    def __init__(self, fraction, position):
        super().__init__('q', fraction, position)

class King(Chesspiece):
    def __init__(self, fraction, position):
        super().__init__('k', fraction, position)