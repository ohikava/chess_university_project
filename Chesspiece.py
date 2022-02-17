class Chesspiece:
    def __init__(self, name, fraction):
        self.name = name
        self.fraction = fraction

    def __str__(self):
        return self.name.upper() if self.fraction else self.name


class Pawn(Chesspiece):
    def __init__(self, fraction):
        super().__init__('p', fraction)


class Bishop(Chesspiece):
    def __init__(self, fraction):
        super().__init__('b', fraction)


class Knight(Chesspiece):
    def __init__(self, fraction):
        super().__init__('n', fraction)


class Rook(Chesspiece):
    def __init__(self, fraction):
        super().__init__('r', fraction)


class Queen(Chesspiece):
    def __init__(self, fraction):
        super().__init__('q', fraction)

class King(Chesspiece):
    def __init__(self, fraction):
        super().__init__('k', fraction)