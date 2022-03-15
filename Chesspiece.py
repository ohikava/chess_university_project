from cmath import phase
from math import pi, sqrt, cos, sin
from utilities import sign
from typing import Callable

"""
Класс реализующий общие своства шахматных фигур(Название фигуры и сторону)
Также прегружает метод перевода в строку, нужно для вывода фигуры в консоли
"""

class Chesspiece:
    def __init__(self, name: str, fraction: bool):
        self.name = name
        self.fraction = fraction

    def __str__(self):
        return self.name.upper() if self.fraction else self.name


"""
Класс пешки, наследует Chesspiece
"""
class Pawn(Chesspiece):
    def __init__(self, fraction: bool):
        super().__init__('p', fraction)

    """
    Возвращает возможные ходы для атаки фигуры, без учета угрозы шаха
    """
    def get_probable_attack_trajectory(self, position: complex, is_cage_occupied: Callable) -> set:
        probable_moves = set()
        signature = 1 if self.fraction else -1
        height = position.imag + signature

        if not 1 <= height <= 8:
            return probable_moves

        if 1 <= (a := position.real + 1) <= 8 and is_cage_occupied((c := complex(a, height)))[0]:
            probable_moves.add(c)

        if 1 <= (a := position.real - 1) <= 8 and is_cage_occupied((c := complex(a, height)))[0]:
            probable_moves.add(c)

        return probable_moves

    """
    Возвращает возможные ходы для фигуры, без учета угрозы шаха
    """
    def get_probable_trajectory(self, position: complex, is_cage_occupied: Callable) -> set:
        probable_moves = set()
        signature = 1 if self.fraction else -1

        if 1 <= (a := position.imag + signature) <= 8 and not is_cage_occupied((c := complex(position.real, a)))[0]:
            probable_moves.add(c)

        if position.imag in {2, 7} and 1 <= (a := position.imag + signature * 2) <= 8 and not is_cage_occupied((c := complex(position.real, a)))[0]:
            probable_moves.add(c)

        return probable_moves

    """
    Возвращает траекторию хода фигуры для определенной позиции
    """
    @staticmethod
    def get_trajectory(position: complex, new_position: complex) -> list:
        position_difference = new_position - position
        trajectory = []
        i = position
        while i != new_position:
            i += complex(0, sign(sin(phase(position_difference * 180 / pi))))
            trajectory.append(i)

        return trajectory

    """
    Метод проверяет может ли фигура пойти в данную клетку, без учета внешних факторов
    Лишь смотрит на правила хода для данной фигуры
    """
    def move_to(self, position: complex, new_position: complex) -> (bool, str, list):
        position_difference = new_position - position

        if phase(position_difference) * 180 / pi == 90.0 and self.fraction and \
                (abs(position_difference) == 1 or abs(position_difference) == 2 and position.imag == 2):
            trajectory = self.get_trajectory(position, new_position)
            return True, "", trajectory

        if phase(position_difference) * 180 / pi == -90.0 and not self.fraction and \
                (abs(position_difference) == 1 or abs(position_difference) == 2 and position.imag == 7):
            trajectory = self.get_trajectory(position, new_position)
            return True, "", trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    """
    Метод проверяет может ли данная фигура атаковать фигуру в данной клетке
    Так же как и предыдущий метод не делает проверки на шах и прочие внешние условия
    Лишь проверку простейших шахматных правил для хода данной фигуры
    """
    def attack(self, position: complex, goal: complex) -> (bool, str, list):
        position_difference = goal - position

        if phase(position_difference) * 180 / pi in {45.0, 135.0} and self.fraction and abs(
                position_difference) == sqrt(2):
            return True, '', [goal, ]

        if phase(position_difference) * 180 / pi in {-45.0, -135.0} and not self.fraction and abs(
                position_difference) == sqrt(2):
            return True, '', [goal, ]

        return False, 'Нельзя атаковать эту клетку', []


"""
Класс слона, наследует Chesspiece
"""
class Bishop(Chesspiece):
    def __init__(self, fraction: bool):
        super().__init__('b', fraction)

    """
    Возвращает возможные ходы для атаки фигуры, без учета угрозы шаха
    """
    def get_probable_attack_trajectory(self, position: complex, is_cage_occupied: Callable) -> []:
        probable_attack_trajectory = set()
        for i in {(1, -1), (-1, 1), (1, 1), (-1, -1)}:
            iter_position = position
            for _ in range(1, 9):
                iter_position += complex(i[0], i[1])
                is_empty = is_cage_occupied(iter_position)

                if is_empty[0] and is_empty[1] == self.fraction:
                    break

                if 1 <= iter_position.real <= 8 and 1 <= iter_position.imag <= 8:
                    probable_attack_trajectory.add(iter_position)
                else:
                    break

                if is_empty[0]:
                    break
        return probable_attack_trajectory

    """
    Возвращает траекторию хода фигуры для определенной позиции
    """
    @staticmethod
    def get_trajectory(position: complex, new_position: complex) -> list:
        position_difference = new_position - position
        trajectory = []
        i = position
        while i != new_position:
            i += complex(sign(cos(phase(position_difference))), sign(sin(phase(position_difference))))
            trajectory.append(i)
        return trajectory

    """
    Метод проверяет может ли фигура пойти в данную клетку, без учета внешних факторов
    Лишь смотрит на правила хода для данной фигуры
    """
    def move_to(self, position: complex, new_position: complex) -> (bool, str, list):
        position_difference = new_position - position

        if phase(position_difference) * 180 / pi in {45, 135, -45, -135}:
            trajectory = self.get_trajectory(position, new_position)
            return True, '', trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    """
    Метод вызывает move_to потому что траектория атаки у данной фигуры совпадает с траекторией обычного хода
    """
    def attack(self, position: complex, goal: complex) -> (bool, str, list):
        return self.move_to(position, goal)

"""
Класс коня, наследует Chesspiece
"""
class Knight(Chesspiece):
    def __init__(self, fraction: bool):
        super().__init__('n', fraction)
    """
    Возвращает возможные ходы для атаки фигуры, без учета угрозы шаха
    """
    def get_probable_attack_trajectory(self, position: complex, is_cage_occupied=None):
        probable_attack_trajectory = set()

        for i in {complex(position.real + 1, position.imag + 2), complex(position.real + 2, position.imag + 1),
                  complex(position.real + 2, position.imag - 1), complex(position.real + 1, position.imag - 2),
                  complex(position.real - 1, position.imag - 2), complex(position.real - 2, position.imag - 1),
                  complex(position.real - 2, position.imag + 1), complex(position.real - 1, position.imag + 2)}:
            is_free = is_cage_occupied(i)
            if is_free[0] and is_free[1] == self.fraction:
                continue

            if 1 <= i.real <= 8 and 1 <= i.imag <= 8:
                probable_attack_trajectory.add(i)
        return probable_attack_trajectory

    """
    Возвращает траекторию хода фигуры для определенной позиции
    """
    @staticmethod
    def get_trajectory(position: complex, new_position: complex) -> list:
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

    """
    Метод проверяет может ли фигура пойти в данную клетку, без учета внешних факторов
    Лишь смотрит на правила хода для данной фигуры
    """
    def move_to(self, position: complex, new_position: complex) -> (bool, str, list):
        position_difference = new_position - position

        if int(phase(position_difference) * 180 / pi) in {63, 26, -26, -63, -116, 116, 153, -153} \
                and sqrt(5) == abs(position_difference):
            trajectory = [new_position, ]
            return True, "", trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    """
    Метод вызывает move_to потому что траектория атаки у данной фигуры совпадает с траекторией обычного хода
    """
    def attack(self, position: complex, goal: complex) -> (bool, str, list):
        return self.move_to(position, goal)

"""
Класс ладьи, наследует Chesspiece
"""
class Rook(Chesspiece):
    def __init__(self, fraction: bool):
        super().__init__('r', fraction)
    """
    Возвращает возможные ходы для атаки фигуры, без учета угрозы шаха
    """
    def get_probable_attack_trajectory(self, position: complex, is_cage_occupied: Callable) -> set:
        probable_attack_trajectory = set()

        for i in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
            iter_position = position
            for _ in range(1, 9):
                iter_position += complex(i[0], i[1])

                is_free = is_cage_occupied(iter_position)

                if is_free[0] and is_free[1] == self.fraction:
                    break

                if 1 <= iter_position.real <= 8 and 1 <= iter_position.imag <= 8:
                    probable_attack_trajectory.add(iter_position)
                else:
                    break

                if is_free[0]:
                    break

        return probable_attack_trajectory

    """
    Возвращает траекторию хода фигуры для определенной позиции
    """
    @staticmethod
    def get_trajectory(position: complex, new_position: complex) -> list:
        position_difference = new_position - position

        trajectory = []
        i = position
        while i != new_position:
            i += complex(sign(cos(phase(position_difference))), sign(sin(phase(position_difference))))
            trajectory.append(i)
        return trajectory

    """
    Метод проверяет может ли фигура пойти в данную клетку, без учета внешних факторов
    Лишь смотрит на правила хода для данной фигуры
    """
    def move_to(self, position: complex, new_position: complex) -> (bool, str, list):
        position_difference = new_position - position

        if phase(position_difference) * 180 / pi in {0, 90, 180, -90, -180}:
            trajectory = self.get_trajectory(position, new_position)

            return True, "", trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    """
    Метод вызывает move_to потому что траектория атаки у данной фигуры совпадает с траекторией обычного хода
    """
    def attack(self, position: complex, goal: complex) -> (bool, str, list):
        return self.move_to(position, goal)

"""
Класс ферзя, наследует Chesspiece
"""
class Queen(Chesspiece):
    def __init__(self, fraction):
        super().__init__('q', fraction)
    """
    Возвращает возможные ходы для атаки фигуры, без учета угрозы шаха
    """
    def get_probable_attack_trajectory(self, position: complex, is_cage_occupied: Callable) -> set:
        probable_attack_trajectory = set()
        for i in {(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)}:
            iter_position = position
            for _ in range(1, 9):
                iter_position += complex(i[0], i[1])
                is_free = is_cage_occupied(iter_position)

                if is_free[0] and is_free[1] == self.fraction:
                    break

                if 1 <= iter_position.real <= 8 and 1 <= iter_position.imag <= 8:
                    probable_attack_trajectory.add(iter_position)
                else:
                    break

                if is_free[0]:
                    break
        return probable_attack_trajectory

    """
    Возвращает траекторию хода фигуры для определенной позиции
    """
    @staticmethod
    def get_trajectory(position: complex, new_position: complex) -> list:
        position_difference = new_position - position

        trajectory = []
        i = position
        while i != new_position:
            i += complex(sign(cos(phase(position_difference))), sign(sin(phase(position_difference))))
            trajectory.append(i)
        return trajectory

    """
    Метод проверяет может ли фигура пойти в данную клетку, без учета внешних факторов
    Лишь смотрит на правила хода для данной фигуры
    """
    def move_to(self, position: complex, new_position: complex) -> (bool, str, list):
        position_difference = new_position - position

        if phase(position_difference) * 180 / pi in {0, 45, 90, 135, 180, -45, -90, -135, -180}:
            trajectory = self.get_trajectory(position, new_position)

            return True, "", trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    """
    Метод вызывает move_to потому что траектория атаки у данной фигуры совпадает с траекторией обычного хода
    """
    def attack(self, position: complex, new_goal: complex) -> (bool, str, list):
        return self.move_to(position, new_goal)

"""
Класс короля, наследует Chesspiece
"""
class King(Chesspiece):
    def __init__(self, fraction: bool):
        super().__init__('k', fraction)
    """
    Возвращает возможные ходы для атаки фигуры, без учета угрозы шаха
    """
    def get_probable_attack_trajectory(self, position: complex, is_cage_occupied: Callable) -> set:
        probable_attack_trajectory = set()

        for i in {(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)}:
            iter_position = complex(position.real + i[0], position.imag + i[1])

            is_free = is_cage_occupied(iter_position)

            if is_free[0] and is_free[1] == self.fraction:
                continue

            if 1 <= iter_position.real <= 8 and 1 <= iter_position.imag <= 8:
                probable_attack_trajectory.add(iter_position)

        return probable_attack_trajectory

    """
    Возвращает траекторию хода фигуры для определенной позиции
    """
    @staticmethod
    def get_trajectory(position: complex, new_position: complex) -> list:
        return [new_position, ]

    """
    Метод проверяет может ли фигура пойти в данную клетку, без учета внешних факторов
    Лишь смотрит на правила хода для данной фигуры
    """
    def move_to(self, position: complex, new_position: complex) -> (bool, str, list):
        position_difference = new_position - position

        if abs(position_difference) in {1, sqrt(2)}:
            trajectory = self.get_trajectory(position, new_position)
            return True, "", trajectory

        return False, "Данная фигура не может пойти в эту клетку", []

    """
    Метод вызывает move_to потому что траектория атаки у данной фигуры совпадает с траекторией обычного хода
    """
    def attack(self, position: complex, goal: complex) -> (bool, str, list):
        return self.move_to(position, goal)


if __name__ == "__main__":
    b = Bishop(True)
