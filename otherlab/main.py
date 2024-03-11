from lib.fraction import Fraction
import itertools


def printMatrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = "".join("   {{:{}}}".format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print("\n".join(table))
    print("\n")


def methodJordanGauss(matrix, flag=True):
    print(f"""{'━'*14}┫ НАЧАЛЬНАЯ  МАТРИЦА ┣{'━'*14}\n""")
    printMatrix(matrix)
    # По столбцам
    for c in range(len(matrix)):
        index = c
        # По элементам столбца
        for i in range(c + 1, len(matrix)):
            if matrix[index][c].getABS() < matrix[i][c].getABS():
                index = i
        if index != c:
            matrix[index], matrix[c] = matrix[c], matrix[index]
            print(f"""{'━'*12}┫ ПРОИЗОШЛА ПЕРЕСТАНОВКА ┣{'━'*12}\n""")
            printMatrix(matrix)
        if matrix[c][c] == Fraction(0):
            continue
        # Сокращение строки
        if matrix[c][c] != Fraction(1):
            matrix[c] = [i / matrix[c][c] for i in matrix[c]]
            printMatrix(matrix)
        # По всем строкам для обнуления
        for i in range(len(matrix)):
            if matrix[i][c] == Fraction(0) or i == c:
                continue
            coefficient = matrix[i][c] * Fraction(-1)
            # По элементам строк, начиная с c-ого
            for j in range(c, len(matrix[0])):
                matrix[i][j] = matrix[i][j] + matrix[c][j] * coefficient
        printMatrix(matrix)

    countNullStr = 0
    for i in matrix:
        nullSumFlag = True
        for j in i[:-1]:
            if j != Fraction(0):
                nullSumFlag = False
                break
        # Если элементы строки нулевые и значение не нулевое
        if nullSumFlag and i[-1] != Fraction(0):
            countNullStr = 0
            break
        # Если строка нулевая
        elif nullSumFlag and i[-1] == Fraction(0):
            continue
        countNullStr += 1

    if not countNullStr:
        return None
    elif countNullStr == len(matrix) and countNullStr == len(matrix[0]) - 1:
        return [[matrix[i][-1] for i in range(len(matrix))]]
    else:
        result = [[], []]
        # Общее решение
        for i in matrix:
            tmpSum = Fraction(0)
            for j in i:
                tmpSum += j.getABS()
            if tmpSum != Fraction(0):
                result[0].append(i)
        matrix = result[0]
        # Базисное решение
        if flag:
            for i in itertools.combinations(
                [i for i in range(len(matrix[0]) - 1)], countNullStr
            ):
                print("━" * 50)
                print("  ", i)
                tmpResult = [0 for i in range(len(matrix[0]) - 1)]
                tmpMatrix = []
                # Получение необходимых столбов, как строк
                for j in i:
                    tmpMatrix.append([x[j] for x in matrix])
                tmpMatrix.append([x[-1] for x in matrix])
                # Транспонирование
                tmpMatrix = [list(j) for j in zip(*tmpMatrix)]
                result_r = methodJordanGauss(tmpMatrix, False)
                if not result_r:
                    print("Нет решения")
                elif len(result_r) == 1:
                    print("Решение:")
                    ans = result_r[0]
                    for j in range(len(ans)):
                        print("  x{} = {}".format(j + 1, ans[j]), end="")
                    t = 0
                    for j in i:
                        tmpResult[j] = ans[t]
                        t += 1
                    print("\n")
                    result[1].append(tmpResult)
                elif len(result_r) == 2:
                    print("\nСЛАУ имеет множество решений")
        return result


def main__choice(matrix):
    print(
        f"""{'━'*8}┫ Метод Жордана-Гаусса ┣{'━'*8}\n""",
        "\n Выберите способ матрицы:\n",
        "    1) Ввод матрицы с клавиатуры\n",
        '    2) Чтение матрицы из файла в директории "./matrices/"\n',
        "    Выход из программы - любой неперечисленный ввод",
    )
    answer = input(" > ")
    if answer == "1":
        R = int(input("Введите количество строк: "))
        for row in range(R):
            a = list(map(int, input().strip().split(" ")))
            matrix.append(list(map(Fraction, a)))
        return methodJordanGauss(matrix)
    elif answer == "2":
        filename = str(input("Введите название файла в формате .txt: "))
        try:
            f = open("matrices/" + filename + ".txt", "r")
        except:
            print(' \033[91m\033[1m[-]\033[0m Не удалось открыть файл "input.txt".')
            return
        for line in f:
            a = list(map(int, line.strip().split(" ")))
            matrix.append(list(map(Fraction, a)))
        return methodJordanGauss(matrix)


def main():
    matrix = []
    result = main__choice(matrix)

    print(f"""{'━'*14}┫ СОКРАЩЕННАЯ  МАТРИЦА ┣{'━'*14}\n""")
    printMatrix(matrix)
    print(f"""{'━'*14}┫ Результат вычислений ┣{'━'*14}\n""")

    if not result:
        print("Нет решения")
    elif len(result) == 1:
        print("Решение:")
        ans = result[0]
        for i in range(len(ans)):
            print("   x{} = {}".format(i + 1, ans[i]))
        print("\n")
    elif len(result) == 2:
        oAns = result[0]
        ans = result[1]

        print("Общее решение:")
        for i in oAns:
            tmpStr = "   "
            for j in range(len(i) - 1):
                tmp = i[j]
                if tmp != Fraction(0):
                    if tmp.getABS() != Fraction(1):
                        if tmp < Fraction(0):
                            tmpStr += " - "
                        else:
                            tmpStr += " + "
                        tmpStr += str(tmp.getABS()) + " * "
                    tmpStr += "x" + str(j + 1)
            tmpStr += " = " + str(i[-1])
            print(tmpStr)

        print("\nБазисные решения:")
        for i in ans:
            for j in range(len(i)):
                print("   x{} = {}".format(j + 1, i[j]))
            print()
    else:
        print("\033[91m\033[1m[-]\033 Произошла не предвиденная ошибка!")
    return


if __name__ == "__main__":
    main()
