from fractions import Fraction

def enter_matrix():
    print("enter matrix. If done, just press Enter.")
    text = " "
    result = []
    while True:
        text = input()
        if text != "":
            #result.append(list(map(Fraction, list(map(int, text.split())))))
            #print([c.split("/")+["1"] for c in text.split()])
            result.append([Fraction(int(c[0]), int(c[1])) for c in [c2.split('/')+["1"] for c2 in text.split()]])
        else:
            break
    return result

def print_matrix(pmatrix):
    for a in pmatrix:
        for b in a:
            print(str(b)+" ", end="")
        print("")
    print("")

def jordan_gauss(matrix):
    result = matrix.copy()
    length_r = len(result)
    length_c = len(result[0])
    for i in range(length_r):
        result = swap_rows(result, i)
        for z in range(length_c):
            if result[i][i] != 0:
                print("divide %d on %d" %(result[i][z],result[i][i]))
                result[i][z] = result[i][z]/matrix[i][i]
        #result[i] = [c/result[i][i] for c in result[i]]
        print("transform row")
        print_matrix(result)
        for i_2 in range(length_r):
            if i == i_2:
                continue
            result[i_2] = [val-result[i][j]*result[i_2][i] for j, val in enumerate(result[i_2])]
        print("zeroing")
        print_matrix(result)
    return result
            

#def matrix_transform()

def swap_rows(matrix, startrow):
    index = startrow
    for i, val in enumerate(matrix[startrow+1:], start=startrow+1):
        if abs(matrix[i][startrow]) > abs(matrix[startrow][startrow]):
            index = i
    result = matrix.copy()
    result[startrow], result[index] = result[index], result[startrow]
    print("swapped %d and %d" %(startrow, index))
    print_matrix(result)
    return result

def get_answers(matrix):
    length_r = len(matrix)
    length_c = len(matrix[0])
    is_infinite = 0
    is_unsolvable = 0
    answers = [Fraction(0) for _ in matrix]
    for i in range(length_r):
        if matrix[i][i] != 0:
            answers[i] = matrix[i][-1]/matrix[i][i]
        elif matrix[i][-1] == 0:
            is_infinite = 1
        else:
            is_unsolvable = 1
    return is_infinite, is_unsolvable, answers

def print_answers(answers):
    for i, val in enumerate(answers):
        print("x%d: %s  " %(i+1, val), end="")
    print("")

if __name__ == "__main__":
    matrix = enter_matrix()
    result = jordan_gauss(matrix)
    print_matrix(result)
    is_inf, is_unsolv, answers = get_answers(result)
    if is_unsolv:
        print("Unsolvable")
    elif is_inf:
        print("Infinite solutions")
    else:
        print_answers(answers)