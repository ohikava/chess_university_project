from cmath import phase
from math import pi, sqrt, cos, sin
from utilities import sign


class Chesspiece:
    def __init__(self, name, fraction):
        self.name = name
        self.fraction = fraction

    def __str__(self):
        return self.name.upper() if self.fraction else self.name


class Pawn(Chesspiece):
    def __init__(self, fraction: bool):
        super().__init__('p', fraction)

    def move_to(self, position: complex, new_position: complex, move=1) -> (bool, str, list):
        first_move = True if move == 1 else False
        position_difference = new_position - position

        if phase(position_difference) * 180 / pi == 90.0 and self.fraction and \
                (abs(position_difference) == 1 or abs(position_difference) == 2 and first_move):
            trajectory = [new_position,] if abs(position_difference) == 1 else [position + 1j, new_position]
            return True, "", trajectory

        if phase(position_difference) * 180 / pi == -90.0 and not self.fraction and abs(position_difference) == 1:
            trajectory = [position - 1j]
            return True, "", trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    def attack(self, position, goal):
        position_difference = goal - position

        if phase(position_difference) * 180 / pi in {45.0, 135.0} and self.fraction and abs(
                position_difference) == sqrt(2):
            return True, ''

        if phase(position_difference) * 180 / pi in {-45.0, -135.0} and not self.fraction and abs(
                position_difference) == sqrt(2):
            return True, ''

        return False, 'Нельзя атаковать эту клетку'

    def check_cages(self, position, cage):
        pass


class Bishop(Chesspiece):
    def __init__(self, fraction):
        super().__init__('b', fraction)

    def move_to(self, position: complex, new_position: complex, move=1) -> (bool, str, list):
        position_difference = new_position - position

        if phase(position_difference) * 180 / pi in {45, 135, -45, -135}:
            trajectory = []
            i = position
            while i != new_position:
                i += complex(sign(cos(phase(position_difference))), sign(sin(phase(position_difference))))
                trajectory.append(i)
            return True, '', trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    def attack(self, position, goal):
        return self.move_to(position, goal)


class Knight(Chesspiece):
    def __init__(self, fraction):
        super().__init__('n', fraction)

    def move_to(self, position, new_position, move=1):
        position_difference = new_position - position

        print(f'phase of knigh is {phase(position_difference) * 180/pi}, abs is {abs(position_difference)}')

        if int(phase(position_difference) * 180/pi) in {63, 26, -26, -63, -116, 116, 153, -153} \
                and sqrt(5) == abs(position_difference):
            return True, ""

        return False, "Данная фигура не может пойти в эту клетку"

    def attack(self, position, goal):
        self.move_to(position, goal)


class Rook(Chesspiece):
    def __init__(self, fraction):
        super().__init__('r', fraction)

    def move_to(self, position,new_position, move=1) -> (bool, str, list):
        position_difference = new_position - position

        if phase(position_difference) * 180 / pi in {0, 90, 180, -90, -180}:
            trajectory = []
            i = position
            while i != new_position:
                i += complex(sign(cos(phase(position_difference))), sign(sin(phase(position_difference))))
                trajectory.append(i)

            return True, "", trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    def attack(self, position,  goal):
        self.move_to(position, goal)


class Queen(Chesspiece):
    def __init__(self, fraction):
        super().__init__('q', fraction)

    def move_to(self, position, new_position, move=1) -> (bool, str, list):
        position_difference = new_position - position

        if phase(position_difference) * 180 / pi in {0, 45, 90, 135, 180, -45, -90, -135, -180}:
            trajectory = []
            i = position
            while i != new_position:
                i += complex(sign(cos(phase(position_difference))), sign(sin(phase(position_difference))))
                trajectory.append(i)

            return True, "", trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    def attack(self, position, new_goal):
        return self.move_to(position, new_goal)


class King(Chesspiece):
    def __init__(self, fraction):
        super().__init__('k', fraction)

    def move_to(self, position, new_position, move=1) -> (bool, str, list):
        position_difference = new_position - position

        if abs(position_difference) in {1, sqrt(2)}:
            return True, "", [new_position,]

        return False, "Данная фигура не может пойти в эту клетку", []

    def attack(self, position, goal):
        return self.move_to(position, goal)

if __name__ == "__main__":
    # b = Bishop(True)
    # print(b.move_to(2 + 2j, 5 + 5j))
    r = Rook(True)
    print(r.move_to(1 + 1j, 1 + 7j))
    print(r.move_to(1 + 1j, 7 + 1j))
    q = Queen(True)
    print(q.move_to(2 + 5j, 1 + 4j))
