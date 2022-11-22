#!/usr/bin/env python3

import copy
import pydot

graph = [[0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0],]
names = ["A", "B", "C", "D", "E", "F"]

def warshall(A):
    T = copy.deepcopy(A)
    n = len(A)
    for i in range(len(T)):
        T[i][i] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if T[i][j] == 0: 
                    if T[i][k] > 0 and T[k][j] > 0:
                        T[i][j] = 1

    return T


def write_graph(graph, closure):
    digraph = pydot.Dot(graph_type="digraph")

    for i in range(len(graph)):
        digraph.add_node(pydot.Node(i, label=names[i]))

    for i in range(len(graph)):
        for j in range(len(graph)):
            if closure[i][j] > 0:
                if graph[i][j] > 0:
                    digraph.add_edge(pydot.Edge(i, j, color="black"))
                    continue
                digraph.add_edge(pydot.Edge(i, j, color="red"))

    digraph.write_pdf('graph.pdf')

graph_t = warshall(graph)
write_graph(graph, graph_t)