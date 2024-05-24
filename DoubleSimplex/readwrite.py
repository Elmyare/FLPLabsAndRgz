import sys
from fraction import *

def readFile(filename: str = "input.txt"):
    with open(filename, 'r', encoding="utf-8") as f:
        lines = list(filter(lambda x: x != '' and '#' not in x, list(map(lambda x: x.strip(), f.readlines()))))
    f.close()
    z = list(map(Fraction, map(int, lines[0].split(' '))))
    z = list((i * Fraction(-1))for i in z[:-1]) + z[-1:]
    matrix = list(list(Fraction(int(y)) for y in x.split(' ')) for x in lines[1:])
    # print(z, *matrix, sep='\n')
    return dict(z=z, matrix=matrix)
def printStep(matrix, z, x, step_num, simplex_relation=None, resolution_element=None):
    """
    Функция, выводящая шаг работы алгоритма
    :param matrix: Матрица
    :param z: Z - функция (список)
    :param x: X (список)
    :param step_num: Номер шага (инт)
    :param simplex_relation: Симплексное отношение (список)
    :param resolution_element: Индекс разрешаюшего элемента (словарь(row, col))
    :return: None
    """

    # Шапка
    field_width = 10
    print("{:^6}┃".format("б.п."), end='')
    print("{:^{size}}┃".format("1", size=field_width), end='')
    for i in range(len(matrix[0]) - 1):
        print("{:^{size}} ".format("x" + str(i + 1), size=field_width), end='')
    print(("\n{:━^6}╋{:━^{size}}╋{:━^" + str(field_width * (len(matrix[0]) - 1) + len(matrix[0]) - 1) + "}").format('', '', '', size=field_width))

    # Строки

    x_index = list()
    for i in range(len(matrix)):
        tmp_flag = False
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] == Fraction(1):
                for k in range(len(matrix)):
                    if matrix[k][j] == Fraction(0) or k == i:
                        tmp_flag = True
                    else:
                        tmp_flag = False
                        break
            if tmp_flag:
                x_index.append(j)
                break

    for i in range(len(matrix)):
        print("{:^6}┃".format("x" + str(x_index[i] + 1)), end='')
        print("{:^{size}}┃".format(str(matrix[i][-1]), size=field_width), end='')
        for j in range(len(matrix[0]) - 1):
            print("{:^{size}} ".format(str(matrix[i][j]), size=field_width), end='')
        # стрелочка
        if resolution_element and i == resolution_element["row"]:
            print("  🠈", end="")
        print()
    print(("{:━^6}╋{:━^{size}}╋{:━^" + str(field_width * (len(matrix[0]) - 1) + len(matrix[0]) - 1) + "}").format('', '', '', size=field_width))

    # Z
    print("{:^6}┃".format("Z1"), end='')
    print("{:^{size}}┃".format(str(z[-1]), size=field_width), end='')
    for i in range(len(z) - 1):
        print("{:^{size}} ".format(str(z[i]), size=field_width), end='')

    # СО
    if simplex_relation:
        print(("\n{:━^6}╋{:━^{size}}╋{:━^" + str(field_width * (len(matrix[0]) - 1) + len(matrix[0]) - 1) + "}").format('', '', '', size=field_width))
        print("{:^6}┃".format("СО"), end='')
        print("{:^{size}}┃".format('', size=field_width), end='')
        for i in range(len(simplex_relation)):
            if simplex_relation[i] != Fraction(sys.maxsize):
                print("{:^{size}} ".format(str(simplex_relation[i]), size=field_width), end='')
            else:
                print("{:^{size}} ".format("━", size=field_width), end='')
    print()
    # стрелочка ↑
    if resolution_element:
        print(("{:^6} {:^{size}} {:^" + str(field_width * (resolution_element["col"]) + resolution_element["col"]) + "}{:^{size}}").format('', '', '', "🠉", size=field_width))
    print()

    # X
    print("X" + str(step_num) + " = " + "(", end='')
    print(*x, sep=', ', end='')
    print(")")

    # Z(X)

    print("Z1(X" + str(step_num) + ") = " + str(z[-1]))