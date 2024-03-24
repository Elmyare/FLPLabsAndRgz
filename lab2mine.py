from fractions import Fraction
import time

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
    to_next = 0
    for i in range(length_r):
        while (to_next < (length_c-length_r)):
            result = swap_rows(result, i, to_next)
            if result[i][i+to_next] != 0:
                break
            to_next += 1
        divider = result[i][i+to_next]
        #print(to_next)
        for z in range(length_c):
            if divider != 0:
                #print("divide %s on %s" %(result[i][z],divider))
                result[i][z] = result[i][z]/divider
        #result[i] = [c/result[i][i] for c in result[i]]
        print("transform row")
        print_matrix(result)
        for i_2 in range(length_r):
            if (i == i_2) or (result[i][i+to_next] == 0):
                continue
            result[i_2] = [val-result[i][j]*result[i_2][i+to_next] for j, val in enumerate(result[i_2])]
        print("zeroing")
        print_matrix(result)
    return result
            

#def matrix_transform()

def swap_rows(matrix, startrow, j_to_next):
    index = startrow
    for i, val in enumerate(matrix[startrow+1:], start=startrow+1):
        if abs(matrix[i][startrow+j_to_next]) > abs(matrix[startrow][startrow+j_to_next]):
            index = i
    result = matrix.copy()
    result[startrow], result[index] = result[index], result[startrow]
    print("swapped %d and %d" %(startrow, index))
    print_matrix(result)
    return result

def get_i_x_to_find(matrixrow):
    result = []
    for i in range(len(matrixrow)-1):
        if matrixrow[i] != 0:
            result.append(i)
    return result

def get_answers(matrix):
    length_r = len(matrix)
    length_c = len(matrix[0])
    is_infinite = 0
    is_unsolvable = 0
    answers = [Fraction(0) for _ in matrix[0][:-1]]
    for i in range(length_r):
        i_x_to_find = get_i_x_to_find(matrix[i])
        if i_x_to_find != []:
            if len(i_x_to_find) == 1:
                answers[i_x_to_find[0]] = matrix[i][-1]/matrix[i][i_x_to_find[0]]
                #print("ye")
            else:
                #print("no", i_x_to_find)
                for j in range(len(i_x_to_find)):
                    answers[i_x_to_find[j]] = str(matrix[i][-1])+"".join([("-"+str(matrix[i][c])+"x("+str(c+1)+")").replace("--","+") for c in (i_x_to_find[:j]+i_x_to_find[j+1:])])
        elif matrix[i][-1] == 0:
            is_infinite = 1
        else:
            #print(i, i_x_to_find)
            is_unsolvable = 1
    return is_infinite, is_unsolvable, answers

def print_answers(answers):
    for i, val in enumerate(answers):
        print("x%d: %s  " %(i+1, val), end="")
    print("")

def comb_leveling(c_list, n,k):
    for i in range(k-1, 0, -1):
        #print(c_list[i], k+i)
        if c_list[i] == k+i:
            c_list[i-1] += 1
            c_list[i] = 0
            c_list = comb_leveling(c_list,n,k)
            c_list[i] = c_list[i-1]+1
    return c_list.copy()
    #time.sleep(0.3)

def find_basis(matrix):
    result = matrix.copy()
    n = len(result[0])-1
    while ([0] * (n+1)) in result:
        result.remove([0]*(n+1))
    k = len(result)
    #print("n:",n,"k:",k)
    baselist = [i for i in range(k)]
    combs = [baselist.copy()]
    #print("now:",combs)
    while True:
        #combs.append(baselist)
        baselist[-1] += 1
        baselist = comb_leveling(baselist,n,k)
        combs.append(baselist.copy())
        #print(combs)
        #time.sleep(0.3)
        if baselist == [c+(n-k) for c in range(k)]:
            break
    answers = []
    for comb in combs:
        #list_to_calc = 
        list_to_calc = [[result[i][c] for c in comb+[-1]] for i in range(k)]
        #list_to_calc.append(result[-1])
        #print_matrix(list_to_calc)
        list_to_calc = jordan_gauss(list_to_calc)
        is_inf, is_uns, answer = get_answers(list_to_calc)
        true_answer = []
        for i in range(n):
            if i in comb:
                true_answer.append(answer[0])
                answer.pop(0)
            else:
                true_answer.append(0)
        answers.append(true_answer)
    return answers
        

if __name__ == "__main__":
    matrix = enter_matrix()
    result = jordan_gauss(matrix)
    print_matrix(result)
    is_inf, is_unsolv, answers = get_answers(result)
    if is_unsolv:
        print("Unsolvable")
    elif is_inf:
        print("Infinite solutions")
        for answers in find_basis(result):
            print_answers(answers)
    else:
        print_answers(answers)
    #print(find_basis(result))

# (0, 1, 2) 
# (0, 1, 3)
# (0, 1, 4)
# (0, 2, 3)
# (0, 2, 4)
# (0, 3, 4)
# (1, 2, 3)
# (1, 2, 4)
# (1, 3, 4)
# (2, 3, 4)