from Chessboard import Chessboard
from Saver import Saver
from utilities import complex_number_2_chess_notation, chess_notation_2_complex_number

"""
Множество всех возможных позиций на шахматной доске
"""
check_move = {complex_number_2_chess_notation(i) + str(k) for i in range(1, 9) for k in range(1, 9)}

""" 
Класс интерфейса шахмат
В своей работе использует класс Chessboard, отвечающий за работу самой шахматной доски
"""
class Cli:
    def __init__(self):
        self.chessboard = Chessboard()
        self.saver = Saver(self.chessboard)
        self.page = 0
        self.points = set()

    """
    Функция выводит шахматную доску в её текущем состоянии, Ничего не возвращает
    """
    def render_chessboard(self) -> None:
        print('  ', end=" ")
        for k in range(1, 9):
            print(complex_number_2_chess_notation(complex(k, 0)) + "", end=" ")
        print(" ")

        if self.chessboard.queue:
            for i in range(8, 0, -1):
                print(i, end="  ")
                for k in range(1, 9):
                    if complex(k, i) in self.points:
                        print('x', end=" ")
                    elif self.chessboard.chess_board[complex(k, i)]:
                        print(self.chessboard.chess_board[complex(k, i)], end=" ")
                    else:
                        print(".", end=" ")
                print(" " + str(i))
            print('  ', end=" ")
        else:
            for i in range(1, 9):
                print(i, end="  ")
                for k in range(1, 9):
                    if complex(k, i) in self.points:
                        print('x', end=" ")
                    elif self.chessboard.chess_board[complex(k, i)]:
                        print(self.chessboard.chess_board[complex(k, i)], end=" ")
                    else:
                        print(".", end=" ")
                print(" " + str(i))
            print('  ', end=" ")

        for k in range(1, 9):
            print(complex_number_2_chess_notation(complex(k, 0)), end=" ")
        print("")
        print('\n')

    def game(self):
        while True:
            match self.page:
                case 0:
                    print('1. Новая Игра \n2. Загрузить игру')
                    input_command = input('Введите номер желаемого пункта: ')

                    match int(input_command):
                        case 1:
                            self.page = 3
                        case 2:
                            self.page = 1
                case 1:
                    print('\n')
                    for index, i in enumerate(savings := self.saver.get_list_savings()):
                        print(f'{index+1}. {i}')

                    input_command = int(input('Введите номер желаемого пункта: '))
                    self.saver.load_file(savings[input_command-1])
                    self.page = 4

                case 3:
                    self.render_chessboard()
                    self.game_controller()
                    self.page = 0

                case 4:
                    index = 0
                    while True:
                        if self.page == 3:
                            break

                        i = self.saver.quick_saves[index]
                        print(i)
                        self.chessboard.move(i[0], i[1])
                        self.render_chessboard()

                        while True:
                            input_command = input("Введите 'вперед' для следущего хода\n'Назад' для предыдущего\n'К игре' для "
                                            "начала игры с этого места")

                            if (com_c := self.common_commands(input_command)) == 0:
                                continue

                            if com_c == 1:
                                break


                            match input_command.lower():
                                case 'вперед':
                                    if index >= len(self.saver.quick_saves) - 1:
                                        print('Следущего хода не существует')
                                        break
                                    index += 1
                                    break
                                case 'назад':
                                    if index == 0:
                                        print('Предыдущего хода не существует')
                                        break
                                    index -= 1
                                    break
                                case 'к игре':
                                    if index >= len(self.saver.quick_saves) - 1:
                                        print('Вы не можете начать игру с этого хода, она уже заверщилась!')
                                        break
                                    self.saver.quick_saves = self.saver.quick_saves[:index+1]
                                    self.page = 3
                                    break
                                case _:
                                    print('Нет такой комманды')
                                    continue



    def common_commands(self, command: str) -> int:
        match command.lower():
            case 'помощь' | 'help':
                print("Ход назад - вернуть 1 ход назад\nФигуры под угрозой - обозначает через x ваши фигуры,\n"
                      "Меню - вернуться в главное меню, РЕЗУЛЬТАТ ИГРЫ БУДЕТ ПОТЕРЯН, ЕСЛИ ВЫ НЕ СОХРАНИЛИ ЕГО В ФАЙЛ"
                      "находящиеся под угрозой удара противника \nВам необходимо выбрать позицию фигуры для "
                      "совершения хода, просто введите позицию на поле в виде 'a2'\nДалее вам нужно ввести желаемую "
                      "клетку куда вы бы хотели переместить эту фигуру")
                return 0
            case 'меню' | 'в меню':
                self.page = 0
                self.saver.restart()
                self.chessboard.restart()
                return 1





    """
    Функция, отвечающая за получение команд пользователя и правильное реагирование на них
    При выполнении каждого хода, заново вызывает render_chessboard()
    """
    def game_controller(self) -> None:
        while True:
            input_command = input("Введите позицию желаемой фигуры для хода или же одну из доступных комманд: ")

            if (com_c := self.common_commands(input_command)) == 0:
                continue

            if com_c == 1:
                break

            if input_command == "Ход назад":
                if self.chessboard.current_move < 3:
                    print("Вы не можете вернуться назад на такой ранней стадии игры")
                    continue
                self.saver.back_one_move()
                self.render_chessboard()
                continue

            if input_command == "Фигуры под угрозой":
                if not self.chessboard.is_king_safe()[0]:
                    print('Вам поставлен шах')

                for i in self.chessboard.get_chesspieces_under_treatment():
                    self.points.add(i)
                if len(self.points) > 0:
                    self.render_chessboard()
                    input()
                    self.points = set()
                    self.render_chessboard()

                continue

            first_position = input_command

            if first_position not in check_move:
                print('Некорректная позиция')
                continue


            if not (chesspiece := self.chessboard.chess_board[chess_notation_2_complex_number(first_position)]):
                print('Клетка пуста')
                continue

            if chesspiece.fraction != self.chessboard.queue:
                print('Вы не можете выбрать чужую фигуру')
                continue

            possible_moves = chesspiece.get_probable_attack_trajectory(chess_notation_2_complex_number(first_position), self.chessboard.check_position)

            if hasattr(chesspiece, 'get_probable_trajectory'):
                possible_moves |= chesspiece.get_probable_trajectory(chess_notation_2_complex_number(first_position), self.chessboard.check_position)

            for i in possible_moves:
                if self.chessboard.check_move(chess_notation_2_complex_number(first_position), i):
                    self.points.add(i)


            self.render_chessboard()
            while True:
                second_position = input('Введите клетку для совершения хода: ')

                if second_position == 'Отмена':
                    break

                if second_position not in check_move:
                    print('Некорректная позиция')
                    continue

                respond = self.chessboard.move(chess_notation_2_complex_number(first_position),
                                               chess_notation_2_complex_number(second_position))
                if respond[0]:
                    if respond[1] == 'Выберите желаемую фигуру':
                        print(respond[1])
                        while True:
                            favourite_chesspiece = input("Пешка, Ладья, Конь, Слон или Ферзь")
                            if (respond := self.chessboard.update_pawn(chess_notation_2_complex_number(second_position),
                                                                       favourite_chesspiece))[0]:
                                break
                            print(respond[1])

                    self.saver.add((chess_notation_2_complex_number(first_position),
                                    chess_notation_2_complex_number(second_position)))
                    print(respond[1])
                    break
                print(respond[1])

            self.points = set()

            self.render_chessboard()

            if respond[1].find('Игра завершена, ') != -1:
                break


    def show_file(self, name:str) -> None:
        self.saver.load_file(name)

        for raw_move in self.saver.loaded_file:
            self.chessboard.move(*self.chessboard.short_notation_to_complex_numbers(raw_move))
            self.render_chessboard()
            print("\n \n")


if __name__ == "__main__":
    new_cli = Cli()
    # new_cli.render_chessboard()
    # new_cli.get_command()
    # new_cli.show_file('notations/test1.txt')
    new_cli.game()

    """
    c2--c4 b7--b5 c4--c5 d7--d5 c5--d6 - взятие на проходе, сложное правило пешки
    c2--c4 d7--d5 c4--c5 b7--b6 c5--b6 b8--c6 b6--b7 h7--h5 b7--b8 Ферзь - замена пешки любой фигурой, сложное правило пешки
    g1--h3 a7--a5 e2--e4 a8--a6 f1--e2 a6--b6 e1--g1 - Рокировка
    a2--a4 b7--b5 Ход назад - Ход назад(откат хода)
    e2--e4 a7--a5 d1--h5 a8--a6 h5--f7 - Шах, в итоге король будет под шахом и единственные доступные ходы, лишь те которые его избавляют от этого
    """