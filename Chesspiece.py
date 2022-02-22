from cmath import phase
from math import pi, sqrt, cos, sin
from utilities import sign
from typing import Callable


class Chesspiece:
    def __init__(self, name, fraction):
        self.name = name
        self.fraction = fraction

    def __str__(self):
        return self.name.upper() if self.fraction else self.name


class Pawn(Chesspiece):
    def __init__(self, fraction: bool):
        super().__init__('p', fraction)

    def get_probable_attack_trajectory(self, position, is_cage_empty: None) -> set:
        probable_moves = set()
        signature = 1 if self.fraction else -1
        probable_moves.add(complex(position.real - 1, position.imag + signature))
        probable_moves.add(complex(position.real + 1, position.imag + signature))

        return probable_moves

    @staticmethod
    def get_trajectory(position, new_position) -> list:
        position_difference = new_position - position
        trajectory = []
        i = position
        while i != new_position:
            i += complex(0, sign(sin(phase(position_difference * 180 / pi))))
            trajectory.append(i)

        return trajectory

    def move_to(self, position: complex, new_position: complex, move=1) -> (bool, str, list):
        first_move = True if move <= 2 else False
        position_difference = new_position - position

        trajectory = self.get_trajectory(position, new_position)

        if phase(position_difference) * 180 / pi == 90.0 and self.fraction and \
                (abs(position_difference) == 1 or abs(position_difference) == 2 and first_move):
            return True, "", trajectory

        if phase(position_difference) * 180 / pi == -90.0 and not self.fraction and \
                (abs(position_difference) == 1 or abs(position_difference) == 2 and first_move):
            return True, "", trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    def attack(self, position, goal) -> (bool, str, list):
        position_difference = goal - position

        if phase(position_difference) * 180 / pi in {45.0, 135.0} and self.fraction and abs(
                position_difference) == sqrt(2):
            return True, '', [goal, ]

        if phase(position_difference) * 180 / pi in {-45.0, -135.0} and not self.fraction and abs(
                position_difference) == sqrt(2):
            return True, '', [goal, ]

        return False, 'Нельзя атаковать эту клетку', []


class Bishop(Chesspiece):
    def __init__(self, fraction):
        super().__init__('b', fraction)

    def get_probable_attack_trajectory(self, position, is_cage_empty: Callable) -> []:
        probable_attack_trajectory = []
        for i in {(1, -1), (-1, 1), (1, 1), (-1, -1)}:
            iter_position = position
            for _ in range(1, 9):
                iter_position += complex(i[0], i[1])
                if 1 <= iter_position.real <= 8 and 1 <= iter_position.imag <= 8:
                    probable_attack_trajectory.append(iter_position)
                if is_cage_empty(iter_position):
                    break
        return probable_attack_trajectory

    @staticmethod
    def get_trajectory(position, new_position):
        position_difference = new_position - position
        trajectory = []
        i = position
        while i != new_position:
            i += complex(sign(cos(phase(position_difference))), sign(sin(phase(position_difference))))
            trajectory.append(i)
        return trajectory

    def move_to(self, position: complex, new_position: complex, move=1) -> (bool, str, list):
        position_difference = new_position - position

        if phase(position_difference) * 180 / pi in {45, 135, -45, -135}:
            trajectory = self.get_trajectory(position, new_position)
            return True, '', trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    def attack(self, position, goal):
        return self.move_to(position, goal)


class Knight(Chesspiece):
    def __init__(self, fraction):
        super().__init__('n', fraction)

    @staticmethod
    def get_probable_attack_trajectory(position, is_cage_free=None):
        probable_attack_trajectory = set()

        for i in {complex(position.real + 1, position.imag + 2), complex(position.real + 2, position.imag + 1),
                  complex(position.real + 2, position.imag - 1), complex(position.real + 1, position.imag - 2),
                  complex(position.real - 1, position.imag - 2), complex(position.real - 2, position.imag - 1),
                  complex(position.real - 2, position.imag + 1), complex(position.real + 2, position.imag - 1)}:
            if 1 <= i.real <= 8 and 1 <= i.imag <= 8:
                probable_attack_trajectory.add(i)
        return probable_attack_trajectory

    @staticmethod
    def get_trajectory(position, new_position) -> list:
        position_differenece = new_position - position
        angle = int(phase(position_differenece) * 180 / pi)

        trajectory = []

        if angle in {26, -26, 153, -153}:
            i = position
            while i.real != new_position.real:
                i += sign(cos(angle))
                trajectory.append(i)
            trajectory.append(complex(i.real, i.imag + sign(sin(angle))))
        else:
            i = position
            while i.imag != new_position.imag:
                i += complex(0, sign(sin(angle)))
                trajectory.append(i)
            trajectory.append(complex(i.real + sign(cos(angle)), i.imag))

        return trajectory

    def move_to(self, position, new_position, move=1) -> (bool, str, list):
        position_difference = new_position - position

        if int(phase(position_difference) * 180 / pi) in {63, 26, -26, -63, -116, 116, 153, -153} \
                and sqrt(5) == abs(position_difference):
            trajectory = [new_position, ]
            return True, "", trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    def attack(self, position, goal):
        return self.move_to(position, goal)


class Rook(Chesspiece):
    def __init__(self, fraction):
        super().__init__('r', fraction)

    @staticmethod
    def get_probable_attack_trajectory(position, is_cage_free: Callable) -> set:
        probable_attack_trajectory = set()

        for i in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
            iter_position = position
            for _ in range(1, 9):
                iter_position += complex(position.real + i[0], position.imag + i[1])
                if 1 <= iter_position.real <= 8 and 1 <= iter_position.imag <= 8:
                    probable_attack_trajectory.add(iter_position)

                else:
                    break

                if is_cage_free(iter_position):
                    break
        return probable_attack_trajectory

    @staticmethod
    def get_trajectory(position, new_position):
        position_difference = new_position - position

        trajectory = []
        i = position
        while i != new_position:
            i += complex(sign(cos(phase(position_difference))), sign(sin(phase(position_difference))))
            trajectory.append(i)
        return trajectory

    def move_to(self, position, new_position, move=1) -> (bool, str, list):
        position_difference = new_position - position

        if phase(position_difference) * 180 / pi in {0, 90, 180, -90, -180}:
            trajectory = self.get_trajectory(position, new_position)

            return True, "", trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    def attack(self, position, goal):
        return self.move_to(position, goal)


class Queen(Chesspiece):
    def __init__(self, fraction):
        super().__init__('q', fraction)

    @staticmethod
    def get_probable_attack_trajectory(position, is_cage_free: Callable) -> set:
        probable_attack_trajectory = set()
        for i in {(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)}:
            iter_position = position
            for _ in range(1, 9):
                iter_position += complex(position.real + i[0], position.imag + i[1])
                if 1 <= iter_position.real <= 8 and 1 <= iter_position.imag <= 8:
                    probable_attack_trajectory.add(iter_position)
                else:
                    break

                if is_cage_free(iter_position):
                    break
        return probable_attack_trajectory

    @staticmethod
    def get_trajectory(position, new_position) -> list:
        position_difference = new_position - position

        trajectory = []
        i = position
        while i != new_position:
            i += complex(sign(cos(phase(position_difference))), sign(sin(phase(position_difference))))
            trajectory.append(i)
        return trajectory

    def move_to(self, position, new_position, move=1) -> (bool, str, list):
        position_difference = new_position - position

        if phase(position_difference) * 180 / pi in {0, 45, 90, 135, 180, -45, -90, -135, -180}:
            trajectory = self.get_trajectory(position, new_position)

            return True, "", trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    def attack(self, position, new_goal):
        return self.move_to(position, new_goal)


class King(Chesspiece):
    def __init__(self, fraction):
        super().__init__('k', fraction)

    @staticmethod
    def get_probable_attack_trajectory(position, is_cage_free:Callable) -> set:
        probable_attack_trajectory = set()

        for i in {(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)}:
            iter_position = complex(position.real + i[0], position.imag + i[1])

            if 1 <= iter_position.real <= 8 and 1 <= iter_position.imag <= 8:
                probable_attack_trajectory.add(iter_position)

        return probable_attack_trajectory

    @staticmethod
    def get_trajectory(position, new_position) -> list:
        return [new_position, ]

    def move_to(self, position, new_position, move=1) -> (bool, str, list):
        position_difference = new_position - position

        if abs(position_difference) in {1, sqrt(2)}:
            trajectory = self.get_trajectory(position, new_position)
            return True, "", trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    def attack(self, position, goal):
        return self.move_to(position, goal)


if __name__ == "__main__":
    b = Bishop(True)
    print(b.get_probable_attack_trajectory(3 + 3j, lambda x: True if x == 2 + 2j else False))
