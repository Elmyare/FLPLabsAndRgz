import sys
from fraction import *
from readwrite import readFile, printStep

step = 0

# Преобразование вектора z
def z_vectorConversion(matrix, resolution_col, resolution_row, z):
    coeff = z[resolution_col] * Fraction(-1)  # Коэффициент для преобразования вектора z
    print(z,coeff)
    for i in range(len(z)):
        z[i] += matrix[resolution_row][i] * coeff  # Преобразование вектора z
    print(z)
# Преобразование матрицы
def matrixConversion(matrix, resolution_col, resolution_row):
    for i in range(len(matrix)):
        if i != resolution_row and matrix[i][resolution_col] != Fraction(0):
            coeff = matrix[i][resolution_col] * Fraction(-1)  # Коэффициент для преобразования матрицы
            for j in range(len(matrix[0])):
                matrix[i][j] += matrix[resolution_row][j] * coeff  # Преобразование матрицы

# Проверка отношения
def checkRelation(matrix, res, resolution_row, step, z):
    simplex_relation = list(Fraction(sys.maxsize) for i in range(len(matrix[0]) - 1))
    for i in range(len(matrix[0]) - 1):
        if matrix[resolution_row][i] < Fraction(0):
            simplex_relation[i] = z[i].abs() / matrix[resolution_row][i].abs()  # Вычисление отношения z[i]/matrix[resolution_row][i]
    resolution_col = simplex_relation.index(min(simplex_relation))  # Находим индекс столбца с минимальным отношением
    printStep(matrix, z, res, step, simplex_relation, dict(row=resolution_row, col=resolution_col))  # Выводим шаг алгоритма
    print("Разрешающий элемент - a[{}][{}] = {}".format(resolution_row, resolution_col,
                                                          matrix[resolution_row][resolution_col]))  # Выводим разрешающий элемент
    tmp = matrix[resolution_row][resolution_col]  # Сохраняем разрешающий элемент
    for i in range(len(matrix[resolution_row])):
        matrix[resolution_row][i] /= tmp  # Делим разрешающую строку на разрешающий элемент
    return resolution_col

# Проверка базиса
def checkBasis(matrix, res):
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
                res[j] = matrix[i][-1]  # Добавляем элемент в список решений
                break

# Основная функция двойственного симплекс-метода
def doubleSimplex(matrix, z):
    global step  # Объявляем переменную step как глобальную
    flag = True  # Флаг для проверки условия продолжения итераций
    while flag:
        step += 1  # Увеличиваем шаг на каждой итерации
        flag = any(x < Fraction(0) for x in [x[-1] for x in matrix])  # Проверяем, есть ли отрицательные элементы в последнем столбце матрицы

        res = list(Fraction(0) for _ in range(len(matrix[0]) - 1))  # Создаем список для хранения решения

        # Проверяем, является ли строка базисной, и если да, то добавляем соответствующий элемент в список решений
        checkBasis(matrix, res)

        if flag:
            if any(x < Fraction(0) for x in z[:-1]):
                print("Отрицательный элемент в Z строке. \nДальше необходимо решать простым симплекс методом")
                ###
                flag = False
                break

            # Поиск разрешающей строки
            b = list(x[-1] for x in matrix)
            negative_b = list(filter(lambda q: q < Fraction(0), b))
            resolution_row = b.index(min(negative_b))  # Находим индекс строки с минимальным отрицательным b

            if not any(x < Fraction(0) for x in matrix[resolution_row][:-1]):
                print("Нет решений.\nВ разрешающей строке нет отрицательных элементов")
                flag = False
                break

            resolution_col = checkRelation(matrix, res, resolution_row, step, z)  # Поиск разрешающего столбца
            matrixConversion(matrix, resolution_col, resolution_row)  # Преобразование матрицы
            z_vectorConversion(matrix, resolution_col, resolution_row, z)  # Преобразование вектора z

        else:
            printStep(matrix, z, res, step)  # Выводим шаг алгоритма

        print("--\n\n")  # Выводим разделитель между итерациями

        print("Z = " + str(z[-1].abs()))  # Выводим значение Z

def main():
    data = readFile()
    z, matrix = data["z"], data["matrix"]

    doubleSimplex(matrix, z)
    return
if __name__ == '__main__':
    main()