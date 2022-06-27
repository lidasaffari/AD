from gozar_test import *
answer = []
paths = []

def tsp(graph, v, currPos, n, count, cost, path):

    if count == n and graph[currPos][0]:
        answer.append(cost + graph[currPos][0])
        paths.append(path)
        return

    for i in range(n):
        if v[i] == False and graph[currPos][i]:
            v[i] = True
            tsp(graph, v, i, n, count + 1,
                cost + graph[currPos][i], path + [i])

            v[i] = False


def main(n=None, graph=[], source = None):
    global answer, paths
    answer = []
    paths = []
    if not n and not graph and not graph and not source:
        n = int(input("How many places do we want to see?"))
        source = int(input("What's The number of the place that are we there?"))

        print("Give me the information of the city's roads")

        for i in range(n):
            line = input().split()

            for i in range(n):
                line[i] = int(line[i])

            graph.append(line)
    v = [False for i in range(n)]
    v[0] = True

    tsp(graph, v, source, n, 1, 0, [])

    if len(answer) > 0:
        result = answer[0]
    else:
        result = "It's impossible"
        print(result)
        return result

    index = 0
    for i in range(1, len(answer)):
        if answer[i] < result:
            result = answer[i]
            index = i

    print(result)
    print([0] + paths[index] + [0])
    return result

while True:
    print("ok........Now we want to see some places and come back")
    print("Enter 1 to input data, 2 to do unit test: ")
    inp = input()
    if inp == "1":
        main()
        break
    elif inp == "2":
        unit_test1(main)
        unit_test2(main)
        unit_test3(main)
        unit_test4(main)
        break

