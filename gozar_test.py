import time


##------------------test 1----------------------
def unit_test1(main):
    print("##------------------test 1---------------------\n\n")

    n = 4 
    matrix = [[0, 10, 15, 20],
              [10, 0, 35, 25],
              [15, 35, 0, 30],
              [20, 25, 30, 20]]
    
    print("\n\nnumber of places: ",n)
    print("\nGeographical characteristics of roads")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end = '\t')
        print()
        
    s = 80
    print("\n\nThe shortest route so that we can see all the places:")
    print("Expected Answer:", "80")
    start_time = time.time()

    if main(n, matrix, 0) == s:
        print("\nTEST ACCEPTED!")

    else:
        print("TEST FAILED")

    print("Algorithm execution time:", (time.time() - start_time) * 1000, "ms")


##------------------test 2----------------------
def unit_test2(main):
    print("##------------------test 2---------------------\n\n")
    n = 5
    matrix = [[0, 10, 0, 23, 10],
              [10, 0, 10, 17, 10],
              [0, 10, 0, 10, 10],
              [36, 40, 10, 0, 10],
              [10, 12, 0, 10, 0]]
    
    print("\n\nnumber of places: ",n)
    print("\nGeographical characteristics of roads")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end = '\t')
        print()
        
    s = 50
    print("\n\nThe shortest route so that we can see all the places:")
    print("Expected Answer:", s)
    start_time = time.time()

    if main(n, matrix, 0) == s:
        print("\nTEST ACCEPTED!")

    else:
        print("TEST FAILED")

    print("Algorithm execution time:", (time.time() - start_time) * 1000, "ms")

##------------------test 3----------------------
def unit_test3(main):
    print("##------------------test 3---------------------\n\n")
    n = 5
    matrix = [[0, 5, 0, 23, 14],
              [10, 0, 1, 17, 1],
              [0, 10, 0, 23, 3],
              [12, 2, 9, 0, 1],
              [10, 12, 0, 10, 0]]
    
       
    print("\n\nnumber of places: ",n)
    print("\n\Geographical characteristics of roads")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end = '\t')
        print()
        
    s = 31
    print("\n\nThe shortest route so that we can see all the places:")
    print("Expected Answer:", "80")
    start_time = time.time()

    if main(n, matrix, 0) == s:
        print("\nTEST ACCEPTED!")

    else:
        print("TEST FAILED")

    print("Algorithm execution time:", (time.time() - start_time) * 1000, "ms")

##------------------test 4----------------------
def unit_test4(main):
    print("##------------------test 4---------------------\n\n")
    n = 5
    matrix = [[0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],]

    print("\n\nnumber of places: ",n)
    print("\nGeographical characteristics of roads")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end = '\t')
        print()
        
    s = "It's impossible"
    print("\n\nThe shortest route so that we can see all the places:")
    print("Expected Answer:", s)
    start_time = time.time()

    if main(n, matrix, 0) == s:
        print("\nTEST ACCEPTED!")

    else:
        print("TEST FAILED")

    print("Algorithm execution time:", (time.time() - start_time) * 1000, "ms")
