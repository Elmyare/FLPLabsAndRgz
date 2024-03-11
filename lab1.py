from fractions import Fraction

def jordan_gauss(matrix):
    n = len(matrix)
    inverse = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    determinant = 1

    for i in range(n):
        if matrix[i][i] == 0:
            # Swap rows to make the diagonal element non-zero
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    matrix[[i, j]] = matrix[[j, i]]
                    determinant *= -1
                    break
            else:
                # Matrix is unsolvable
                return None, None

        factor = Fraction(1) / matrix[i][i]
        for j in range(n):
            inverse[i][j] = factor * matrix[i][j] if i == j else -factor * matrix[i][j]
            determinant *= matrix[i][i]

        for j in range(n):
            if i != j:
                factor = matrix[j][i]
                for k in range(n):
                    matrix[j][k] -= factor * matrix[i][k]
                    inverse[j][k] -= factor * inverse[i][k]
                determinant *= factor

    return inverse, determinant

def swap_row(matrix, row1, row2):
    matrix[[row1, row2]] = matrix[[row2, row1]]


if __name__ == "__main__":
# Example usage:
    matrix = [[Fraction(2), Fraction(1), Fraction(3)],
            [Fraction(1), Fraction(2), Fraction(0)],
            [Fraction(3), Fraction(0), Fraction(5)]]
    inverse, determinant = jordan_gauss(matrix)
    if inverse is not None:
        print("Inverse matrix:")
        for row in inverse:
            print(row)
        print("Determinant:", determinant)
    else:
        print("Matrix is unsolvable.")
