import numpy as np
import time

def get_shortest(n, dest, matrix, index, visited):
    if index == dest:
        return 0
    
    minimum = 99999
    for i in range(len(matrix[index])):
        if i not in visited and matrix[index][i] > 0:
            m = get_shortest(n, dest, matrix, i, visited + [i]) + matrix[index][i]

            if m < minimum:
                minimum = m
            
    return minimum
    
 
def unit_test(function):
    
    n = int(input("\nHow many places do you want to exist in city? "))

    destination = np.random.randint(1, n)
    
    matrix = [[0 for i in range(n)] for j in range(n)]

    print("\ninformation of the city's roads :")
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == 0 and np.random.randint(0,2):
                matrix[i][j] = np.random.randint(1, n * n * n)
                matrix[j][i] = matrix[i][j]

            print(matrix[i][j], end=' ')
        print()

          

    print("Shortest path from source to",destination,'th place(destination)')

    s = get_shortest(n, destination, matrix, 0, [])
    print("Expected Answer:", s)

    start_time = time.time()
    if function(n, destination, matrix) == s:
        print("\nTEST ACCEPTED!")
    else:
        print("\nTEST FAILED!")

    print("Algorithm execution time:", time.time() - start_time, "s")
    
                
