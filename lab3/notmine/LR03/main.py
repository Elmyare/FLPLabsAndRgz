from lib.color import Color

import sys, os


def printStep(stocks, needs, matrix):
    cell_width = 15
    # Строка 1
    print(
        (
            "    "
            + "┏{:━^15}┳{:━^"
            + str(cell_width * len(matrix[0]) + len(matrix[0]) - 1)
            + "}┳{:━^"
            + str(cell_width)
            + "}┓"
        ).format("", "", "")
    )
    # Строка 2
    print(
        (
            "    "
            + "┃{:^15}┃{:^"
            + str(cell_width * len(matrix[0]) + len(matrix[0]) - 1)
            + "}┃{:^"
            + str(cell_width)
            + "}┃"
        ).format("", "Потребитель", "")
    )
    # Строка 3
    print(
        (
            "    "
            + "┃{:^15}┣{:━^"
            + str(cell_width * len(matrix[0]) + len(matrix[0]) - 1)
            + "}┫{:^"
            + str(cell_width)
            + "}┃"
        ).format("Поставщик", "", "Запас")
    )
    # Строка 4
    print("    ┃{:^15}┃".format(""), end="")
    for i in range(len(matrix[0])):
        print(("{:^" + str(cell_width) + "}┃").format("B" + str(i + 1)), end="")
    print(("{:^" + str(cell_width) + "}┃").format(""))
    # Строка 5
    print("    ┣{:━^15}╋".format(""), end="")
    for i in range(len(matrix[0])):
        print(("{:━^" + str(cell_width) + "}╋").format(""), end="")
    print(("{:━^" + str(cell_width) + "}┫").format(""))
    # Строка 6 - 9 (3 * An раз)
    for line in enumerate(matrix):
        # Строка 6
        print("    ┃{:^15}┃".format(""), end="")
        for element in line[1]:
            print(
                ("{:>" + str(cell_width - 2) + "}  ┃").format(
                    "(0)"
                    if element["tariff"] == (sys.maxsize - 1)
                    else element["tariff"]
                ),
                end="",
            )
        print(("{:^" + str(cell_width) + "}┃").format(""))
        # Строка 7
        print("    ┃{:^15}┃".format("A" + str(line[0] + 1)), end="")
        for element in line[1]:
            print(("{:^" + str(cell_width) + "}┃").format(""), end="")
        print(("{:^" + str(cell_width) + "}┃").format(stocks[line[0]]))
        # Строка 8
        print("    ┃{:^15}┃".format(""), end="")
        for element in line[1]:
            print(
                ("{:^" + str(cell_width) + "}┃").format(
                    ""
                    if element["quantity"] is None
                    else ("---" if element["quantity"] == -1 else element["quantity"])
                ),
                end="",
            )

        print(("{:^" + str(cell_width) + "}┃").format(""))
        # Строка 9
        print("    ┣{:━^15}╋".format(""), end="")
        for i in range(len(matrix[0])):
            print(("{:━^" + str(cell_width) + "}╋").format(""), end="")
        print(("{:━^" + str(cell_width) + "}┫").format(""))
    # Строка 10 (После An)
    print("    ┃{:^15}┃".format("Потребность"), end="")
    for i in needs:
        print(("{:^" + str(cell_width) + "}┃").format(str(i)), end="")
    print(("{:^" + str(cell_width) + "}┃").format(""))
    # Строка 11 (После An)
    print("    ┗{:━^15}┻".format(""), end="")
    for i in range(len(matrix[0])):
        print(("{:━^" + str(cell_width) + "}┻").format(""), end="")
    print(("{:━^" + str(cell_width) + "}┛").format(""))


def main(File, DEBUG):
    print("\n")
    # Чтение из файла
    with File as f:
        lines = list(
            filter(
                lambda x: x != "" and "#" not in x,
                list(map(lambda x: x.strip(), f.readlines())),
            )
        )
    f.close()
    if DEBUG != False:
        print(Color.bg.blue + Color.bold + "[DEBUG]" + Color.reset)
        print("  lines = ", lines)

    # Парсинг файла по переменным
    stocks = list(map(int, lines[0].split(" ")))  # Запасы
    needs = list(map(int, lines[1].split(" ")))  # Потребности
    matrix = list(
        list(dict(tariff=int(y), quantity=None, used=False) for y in x.split(" "))
        for x in lines[2:]
    )
    if DEBUG != False:
        print("  stocks =", stocks)
        print("  needs = ", needs)
        print("  matrix:", *matrix, sep="\n    ")
        print(Color.bg.blue + Color.bold + "[/DEBUG]" + Color.reset + "\n")

    result = 0  # Ответ

    # Проверка на тип модели и добавление в случае чего
    if sum(stocks) < sum(needs):
        print(
            Color.bold
            + "Открытая модель транспортной задачи (фиктивный поставщик)"
            + Color.reset
        )
        matrix.append(
            list(
                dict(tariff=sys.maxsize - 1, quantity=None, used=False)
                for _ in range(len(matrix[0]))
            )
        )
        stocks.append(sum(needs) - sum(stocks))
    elif sum(stocks) > sum(needs):
        print(
            Color.bold
            + "Открытая модель транспортной задачи (фиктивный потребитель)"
            + Color.reset
        )
        for i in range(len(matrix)):
            matrix[i].append(dict(tariff=sys.maxsize - 1, quantity=None, used=False))
        needs.append(sum(stocks) - sum(needs))
    else:
        print(Color.bold + "Закрытая модель транспортной задачи" + Color.reset)

    print("  Начальное  состояние:")
    printStep(stocks, needs, matrix)
    print("\n")

    print("  Вычисление:")
    while sum(stocks) != 0 and sum(needs) != 0:
        row = -1
        column = -1
        minElement = sys.maxsize

        # Поиск минимального тарифа
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]["tariff"] < minElement and not matrix[i][j]["used"]:
                    row = i
                    column = j
                    minElement = matrix[i][j]["tariff"]

        minElement = min(needs[column], stocks[row])
        matrix[row][column]["used"] = True
        matrix[row][column]["quantity"] = minElement
        needs[column] -= minElement
        stocks[row] -= minElement

        # "Вычеркивание" строк/столбцов
        if sum(stocks) != 0 and sum(needs) != 0:
            if needs[column] < stocks[row]:
                for i in matrix:
                    if not i[column]["used"]:
                        i[column]["used"] = True
                        i[column]["quantity"] = -1
            elif needs[column] > stocks[row]:
                for i in matrix[row]:
                    if not i["used"]:
                        i["used"] = True
                        i["quantity"] = -1
            else:
                minTmp = sys.maxsize
                rowTmp = -1
                columnTmp = -1
                for i in range(len(matrix)):
                    if not matrix[i][column]["used"]:
                        matrix[i][column]["used"] = True
                        matrix[i][column]["quantity"] = -1
                        if matrix[i][column]["tariff"] < minTmp:
                            rowTmp = i
                            columnTmp = column
                            minTmp = matrix[i][column]["tariff"]
                for j in range(len(matrix[row])):
                    if not matrix[row][j]["used"]:
                        matrix[row][j]["used"] = True
                        matrix[row][j]["quantity"] = -1
                        if matrix[row][j]["tariff"] < minTmp:
                            rowTmp = row
                            columnTmp = j
                            minTmp = matrix[row][j]["tariff"]
                matrix[rowTmp][columnTmp]["quantity"] = 0

        printStep(stocks, needs, matrix)
        print("\n")
        result += (
            0
            if matrix[row][column]["tariff"] == (sys.maxsize - 1)
            else matrix[row][column]["tariff"] * matrix[row][column]["quantity"]
        )

    print(Color.fg.green + Color.bold + "  [ОТВЕТ] ", end=Color.reset)
    print(str(result))
    return


if __name__ == "__main__":
    filename = str(input("Введите название файла:\n  > "))
    try:
        file = open("tasks/" + filename, "r")
        main(file, False)
    except:
        print(Color.fg.red + Color.bold + "[ОШИБКА] ", end=Color.reset)
        print("Файл 'tasks/" + filename + "' не найден!")
