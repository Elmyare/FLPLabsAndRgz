import math
from decimal import *

def enter_matrix():
    print("enter matrix. If done, just press Enter.")
    text = " "
    result = []
    while True:
        text = input()
        if text != "":
            result.append(list(map(Decimal, text.split())))
        else:
            break
    return result

def print_matrix(pmatrix):
    for a in pmatrix:
        for b in a:
            print(str(b)+" ", end="")
        print("")
    print("")

def triangular_view(pmatrix):
    result = pmatrix.copy()
    length_s = len(result)
    length_w = len(result[0])
    if (length_s>1)and(length_w)>1:
        for i in range(1, length_s):
            result = row_swapper(result, i-1)
            for j in range(i, length_s):
                divider = result[j][i-1]/result[i-1][i-1]
                for k in range(i-1, length_w):
                    result[j][k] -= result[i-1][k]*divider
    return result

def get_answer(pmatrix):
    length_s = len(pmatrix)
    length_w = len(pmatrix[0])
    answers = [Decimal(0)]*(length_w-1)
    for i in range(length_s-1,-1,-1):
        plus_to = Decimal(0)
        for j in range(length_w-1):
            plus_to += pmatrix[i][j]*answers[j]
        pmatrix[i][-1] -= plus_to
        answers[i] = pmatrix[i][-1]/pmatrix[i][i]
    return answers

def print_answer(panswer):
    for i, c in enumerate(panswer):
        print("x%d: %f " %(i+1,c), end="")

def row_swapper(pmatrix, startrow):
    if (startrow<0) or (startrow>=len(pmatrix)):
        return None
    result = pmatrix.copy()
    index = startrow
    for i, val in enumerate(result[startrow+1:], start=startrow+1):
        if result[i][startrow]>result[startrow][startrow]:
            index = i
    result[startrow], result[index] = result[index], result[startrow]
    #print("swapped",startrow+1,"and",index+1)
    print_matrix(result)
    return result

if __name__=="__main__":
    matrix = enter_matrix()
    #print(matrix)
    print_matrix(matrix)
    matrix = triangular_view(matrix)
    #print(matrix)
    print_matrix(matrix)
    answers = get_answer(matrix)
    print(answers)
    print_answer(answers)
