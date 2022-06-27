from bazsazi_test import *

import sys
def printMST(parent, graph, vertice):
	print("road \tlength")
	sum = 0
	for i in range(1, vertice):
		print(parent[i], "-", i, "\t", graph[i][parent[i]])
		sum += graph[i][parent[i]]
	print(sum)
	return sum

def minKey( key, mstSet, vertice):

	min = sys.maxsize

	for v in range(vertice):
		if key[v] < min and mstSet[v] == False:
			min = key[v]
			min_index = v

	return min_index

def primMST(graph, vertice):

	key = [sys.maxsize] * vertice
	parent = [None] * vertice
	key[0] = 0
	mstSet = [False] * vertice

	parent[0] = -1

	for cout in range(vertice):

		u = minKey(key, mstSet, vertice)


		mstSet[u] = True


		for v in range(vertice):

			if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]:
					key[v] = graph[u][v]
					parent[v] = u

	return printMST(parent, graph, vertice)


def main(vertice = None, graph = None):

    if not vertice and not graph:
        vertice = int(input("How meny sectors the neighborhood consists ?"))
        graph = []

        for i in range(vertice):
            line = input().split()

            for i in range(vertice):
                line[i] = int(line[i])

            graph.append(line)

    return primMST(graph, vertice)


while True:
    print("\nok..... now we want to rebuild the roads")
    print("\n---------> Enter 1 to input data, 2 to do unit test: ")
    inp = input()
    if inp == "1":
        main()
        break
    elif inp == "2":
        unit_test(main)
        break


# 4
# 1 2 1 0
# 1 3 2 3
# 1 2 1 0
# 3 2 3 1
