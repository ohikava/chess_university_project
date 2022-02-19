from math import copysign

notes_2_number = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8
}

numbers_2_notes = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')


def chess_notation_2_complex_number(notation):
    note_letter, note_number = notation[0], notation[1]

    real_number_b = notes_2_number[note_letter]
    real_number_a = int(note_number)

    return complex(real_number_b, real_number_a)


def complex_number_2_chess_notation(complex_number):
    return numbers_2_notes[int(complex_number.real - 1)] + str(
        int(complex_number.imag)) if complex_number.imag != 0 else numbers_2_notes[int(complex_number.real - 1)]


def sign(x):
    return copysign(1, x) if x > 10**(-3)  or x < -10 ** (-3) else 0


if __name__ == "__main__":
    print(chess_notation_2_complex_number('h2'))
    print(complex_number_2_chess_notation(2 + 2j))
