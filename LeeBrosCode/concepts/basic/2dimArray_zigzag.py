# Module
import sys

# Input
n, m = map(int, sys.stdin.readline().strip().split())

# isEdge
def isEdge(number):
    if (number // n) % 2 != 0:
        return True
    else:
        return False


# backward
def backward(matrix, number, row, col):
    # col -= m
    row = -row - 1  # 여기서 한참 헤맴
    # print(f'\t[col] {col}')
    # print(f'\t[row] {row} [-row] {-row}')

    matrix[row][col] = number
    # print(f'\t[BACK]')
    # print(f'\t{matrix}')  # Check
    return matrix


# write
def write(matrix, number, row, col):
    matrix[row][col] = number
    # print(matrix)  # Check
    return matrix


# Main
def main():
    matrix_nm = [[-1 for _ in range(m)] for _ in range(n)]  # n*m Matrix
    number = 1

    for col in range(0, m):  # col
        for row in range(0, n):  # row

            # print(f'\n[Loop Check]\nrow : {row} \ncol : {col}\n')
            # if isEdge(row, col):  # True -> number is on the edge side
            if row == 0 and col == 0:  # Start Point
                matrix_nm[0][0] = 0
                continue

            if isEdge(number):  # backward
                # print(f'[backward]')
                backward(matrix_nm, number, row, col)
                number += 1

            else:
                # print(f'[foward]')
                write(matrix_nm, number, row, col)
                number += 1

    # [OUTPUT]
    for row in range(n):
        for col in range(m):
            print(matrix_nm[row][col], end=" ")
        print()


if __name__ == "__main__":
    main()
