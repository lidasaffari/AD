from parking_test import *
def promising(n, null, matrix):
    switch = False
    if null[0] - 2 >= 0 and matrix[null[0] - 1][null[1]] == matrix[null[0] - 2][null[1]]:
        switch = True
    if null[0] + 2 < n and matrix[null[0] + 1][null[1]] == matrix[null[0] + 2][null[1]]:
        switch = True
    if null[1] - 2 >= 0 and matrix[null[0]][null[1] - 1] == matrix[null[0]][null[1] - 2]:
        switch = True
    if null[1] + 2 < n and matrix[null[0]][null[1] + 1] == matrix[null[0]][null[1] + 2]:
        switch = True

    return switch


def parking(n, matrix, null, ask, order):
    if promising(n, null, matrix):
        if null == ask:
           print(order)
           return(order)
        else:
            if null[0] - 2 >= 0 and matrix[null[0] - 2][null[1]] not in order:
                if matrix[null[0] - 1][null[1]] == matrix[null[0] - 2][null[1]]:
                    order.append(matrix[null[0] - 1][null[1]])
                    matrix[null[0]][null[1]] = matrix[null[0] - 2][null[1]]
                    null[0] -= 2
                    matrix[null[0]][null[1]] = 0
                    return parking(n, matrix, null, ask, order)

            if null[0] + 2 < n and matrix[null[0] + 2][null[1]] not in order:
                if matrix[null[0] + 1][null[1]] == matrix[null[0] + 2][null[1]]:
                    order.append(matrix[null[0] + 2][null[1]])
                    matrix[null[0]][null[1]] = matrix[null[0] + 2][null[1]]
                    null[0] += 2
                    matrix[null[0]][null[1]] = 0
                    return parking(n, matrix, null, ask, order)

            if null[1] - 2 >= 0 and matrix[null[0]][null[1] - 2] not in order:
                if matrix[null[0]][null[1] - 2] == matrix[null[0]][null[1] - 2]:
                    order.append(matrix[null[0]][null[1] - 2])
                    matrix[null[0]][null[1]] = matrix[null[0]][null[1] - 2]
                    null[1] -= 2
                    matrix[null[0]][null[1]] = 0
                    return parking(n, matrix, null, ask, order)

            if null[1] + 2 < n and matrix[null[0]][null[1] + 2] not in order:
                if matrix[null[0]][null[1] + 1] == matrix[null[0]][null[1] + 2]:
                    order.append(matrix[null[0]][null[1] + 2])
                    matrix[null[0]][null[1]] = matrix[null[0]][null[1] + 2]
                    null[1] += 2
                    matrix[null[0]][null[1]] = 0
                    return parking(n, matrix, null, ask, order)


def main():
    n = 4
    matrix = [[7, 7, 0, 6],
             [3, 5, 5, 6],
             [3, 4, 4, -1],
             [1, 1, 2, 2]]

    ask = [2, 2]
    order = []


    for i in range(n):

        for j in range(n):

            if matrix[i][j] == 0:
                null = [i, j]
 
    if not parking(n, matrix, null, ask, order):
        print("Not possible to empty this part of the parking lot")


print("------------------TEST 1----------------")
unit_test1(parking)
print("----------------TEST 2----------------")
unit_test2(parking)
print("----------------TEST 3----------------")
unit_test3(parking)
