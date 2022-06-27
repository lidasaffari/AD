import time

def unit_test1(parking):
    matrix = [[-1, 1, 1, 2],
              [4, 3, 3, 2],
              [4, 5, 5, 6],
              [7, 7, 0, 6]]
    n = 4
    print("Input of the Unit Test")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end = '\t')
        print()

    print("\n\nRequest to vacate [1,2]")
    print("\n\nExpected Answer:", "[7, 4, 3]")
    s = [7, 4, 3]
    start_time = time.time()

    if parking(4, matrix, [3, 2], [1, 2], []) == s:
        print("\nTEST ACCEPTED!")

    else:
        print("TEST FAILED")

    print("Algorithm execution time:", time.time() - start_time, "s")


def unit_test2(parking):
    matrix = [[0, -1, 1, 1],
              [4, 3, 3, 2],
              [4, 5, 5, 2],
              [7, 7, 6, 6]]
    n = 4
    print("Input of the Unit Test")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end = '\t')
        print()

    print("\n\nRequest to vacate [2,2]")
    print("\n\nExpected Answer:", "[4, 5]")
    s = [4, 5]
    start_time = time.time()

    if parking(4, matrix, [0, 0], [2, 2], []) == s:
        print("\nTEST ACCEPTED!")

    else:
        print("TEST FAILED")

    print("Algorithm execution time:", time.time() - start_time, "s")


def unit_test3(parking):
    matrix = [[0, -1, 1, 1],
              [4, 3, 3, 2],
              [4, 5, 5, 2],
              [7, 7, 6, 6]]
    n = 4
    print("Input of the Unit Test")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end = '\t')
        print()

    print("\n\nRequest to vacate [2,3]")
    print("\n\nExpected Answer:", "Not Possible")
    s = None
    start_time = time.time()

    if parking(4, matrix, [0, 0], [2, 3], []) == s:
        if s == None:
            print("Not Possible")
        print("\nTEST ACCEPTED!")

    else:
        print("TEST FAILED")

    print("Algorithm execution time:", time.time() - start_time, "s")