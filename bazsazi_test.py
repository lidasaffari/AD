import numpy as np
import time

def create_tree(array):
    n = len(array)
    L = set(range(1, n+2+1))
    tree_edges = []
    for i in range(n):
        u, v = array[0], min(L - set(array))
        array.pop(0)
        L.remove(v)
        tree_edges.append((u,v))
    tree_edges.append((L.pop(), L.pop()))
    return tree_edges

def unit_test(function):
    print("How many sectors do you want to city have?")
    n = int(input())
    
    matrix = [ [0 for i in range(n)] for j in range(n) ]
    array = np.random.choice(range(1,n+1), n-2, replace=True).tolist()
    tree = create_tree(array)

    s = 0
    for item in tree:
        x = np.random.randint(1, n * n)
        s += x
        matrix[ item[0] - 1 ][ item[1] - 1 ] = x
        matrix[ item[1] - 1 ][ item[0] - 1 ] = x

    print("Geographic information of the city made by Unit Test with",n,"sectors:")
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == 0 and np.random.randint(0,2):
                matrix[i][j] = np.random.randint(n * n + 1, n * n * n)
                matrix[j][i] = matrix[i][j]

            print(matrix[i][j], end = '\t')
        print()

    print("\nMinimum length of required road:")
    print("answer of unit test :", s)
    print("answer of algorithm :")
    
    start_time = time.time()
    if function(n, matrix) == s:
        print("TEST ACCEPTED!")
    else:
        print("TEST FAILED!")
    print("Places are modeled with numbers")
    print("Algorithm execution time:", (time.time() - start_time)*1000, "ms")
    
                
