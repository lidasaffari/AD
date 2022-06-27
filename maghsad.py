from maghsad_test import *

def minDistance(dist, queue):
    minimum = float("Inf")
    min_index = -1

    for i in range(len(dist)):

        if dist[i] < minimum and i in queue:
            minimum = dist[i]
            min_index = i

    return min_index


def printPath(parent, v):
    if parent[v] == -1:
        print(v, end=" ")
        return
    printPath(parent, parent[v])
    print(v, end=" ")


def printSolution(destination, dist, parent):
    src = 0
    print("Vertex \t\tDistance from Source\tPath")
    print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, destination, dist[destination]), end=" ")
    printPath(parent, destination)

    return dist[destination]


def dijkstra(graph, src, destination):

    row = len(graph)
    col = len(graph[0])
    dist = [float("Inf")] * row
    parent = [-1] * row
    dist[src] = 0
    queue = []

    for i in range(row):
        queue.append(i)

    while queue:

        u = minDistance(dist, queue)

        queue.remove(u)

        for i in range(col):

            if graph[u][i] and i in queue:
                if dist[u] + graph[u][i] <= dist[i]:
                    if dist[u] + graph[u][i] == dist[i] and i == destination:
                        printSolution(destination, dist, parent)
                    dist[i] = dist[u] + graph[u][i]
                    parent[i] = u

    return printSolution(destination, dist, parent)

def main(n = None, destination = None ,graph = None):

    if not n and not destination and not graph:
        n = int(input("How many sectors the neighborhood consists?"))
        destination = int(input("What's The number of the place that you wanna go there?"))
        graph = []

        for i in range(n):
            line = input().split()

            for i in range(n):
                line[i] = int(line[i])

            graph.append(line)

    return dijkstra(graph, 0, destination)


while True:
    print("ok...Now we want to go to the destination by the shortest way")
    print("Enter 1 to input data, 2 to do unit test: ")
    inp = input()
    if inp == "1":
        main()
        break
    elif inp == "2":
        unit_test(main)
        break

# 4
# 0 1 0 3
# 1 3 2 1
# 0 2 3 4
# 3 1 4 8
