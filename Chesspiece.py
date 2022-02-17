from cmath import phase
from math import pi, sqrt


class Chesspiece:
    def __init__(self, name, fraction):
        self.name = name
        self.fraction = fraction

    def __str__(self):
        return self.name.upper() if self.fraction else self.name


class Pawn(Chesspiece):
    def __init__(self, fraction):
        super().__init__('p', fraction)

    def move_to(self, position, new_position, first_move=False):
        position_difference = new_position - position

        if phase(position_difference) * 180 / pi == 90.0 and self.fraction and \
                (abs(position_difference) == 1 or abs(position_difference) == 2 and first_move):
            return True, ""

        if phase(position_difference) * 180 / pi == -90.0 and not self.fraction and abs(position_difference) == 1:
            return True, ""

        return False, "Данная фигура не может пойти в эту клетку"

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

    def move_to(self, position, new_position):
        position_difference = new_position - position

        if phase(position_difference) * 180 / pi in {45, 135, -45, -135}:
            return True, ''

        return False, "Данная фигура не может пойти в эту клетку"

    def attack(self, position, goal):
        return self.move_to(position, goal)


class Knight(Chesspiece):
    def __init__(self, fraction):
        super().__init__('n', fraction)

    def move_to(self, position, new_position):
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

    def move_to(self, position,new_position):
        position_difference = new_position - position

        if phase(position_difference) * 180 / pi in {0, 90, 180, -90, -180}:
            return True, ""

        return False, "Данная фигура не может пойти в эту клетку"

    def attack(self, position, goal):
        self.move_to(position, goal)


class Queen(Chesspiece):
    def __init__(self, fraction):
        super().__init__('q', fraction)

    def move_to(self, position, new_position):
        position_difference = new_position - position

        if phase(position_difference) * 180 / pi in {0, 45, 90, 135, 180, -45, -90, -135, -180}:
            return True, ""

        return False, "Данная фигура не может пойти в эту клетку"

    def attack(self, position, new_goal):
        return self.move_to(position, new_goal)


class King(Chesspiece):
    def __init__(self, fraction):
        super().__init__('k', fraction)

    def move_to(self, position, new_position):
        position_difference = new_position - position

        if abs(position_difference) in {1, sqrt(2)}:
            return True, ""

        return False, "Данная фигура не может пойти в эту клетку"

    def attack(self, position, goal):
        return self.move_to(position, goal)


if __name__ == "__main__":
    p = Pawn(True)
    print(p.move_to(2 + 2j, 2 + 4j, True))
    print(p.attack(2 + 2j, 3 + 3j))
    print(p.attack(2 + 2j, 1 + 3j))
    print(p.attack(2 + 2j, 3 + 1j))
    print(p.attack(2 + 2j, 1 + 1j))
    k = Knight(True)
    k.move_to(3 + 3j, 4 + 5j)
    k.move_to(3 + 3j, 5 + 4j)
    k.move_to(3 + 3j, 5 + 2j)
    k.move_to(3 + 3j, 4 + 1j)
    k.move_to(3 + 3j, 2 + 1j)
    k.move_to(3 + 3j, 1 + 2j)
    k.move_to(3 + 3j, 1 + 4j)
    k.move_to(3 + 3j, 2 + 5j)
