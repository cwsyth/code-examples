import pydot

graph = {
    "A" : ["B", "C"],
    "B" : ["D", "E"],
    "C" : ["F"],
    "D" : [],
    "E" : ["F"],
    "F" : [],
}


def write_graph(graph):
    digraph = pydot.Dot(graph_type="digraph")
    for node in graph:
        digraph.add_node(pydot.Node(node))
    for node in graph:
        for edge in graph[node]:
            digraph.add_edge(pydot.Edge(node, edge))
    digraph.write_pdf("dfs-graph.pdf")


def dfs(graph, node, visited=None):
    if(visited == None):
        visited = []
    if(node not in visited):
        visited.append(node)
        for neighbor in graph[node]:
            visited = dfs(graph, neighbor, visited)
    return visited


def dfs_it(graph, root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if(node not in visited):
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

def dfs_it(graph, root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if(node not in visited):
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

def bfs_it(graph, root):
    queue = [root]
    visited = []
    while queue:
        node = queue.pop(0)
        if(node not in visited):
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited


write_graph(graph)
order1 = dfs(graph, "A")
print(order1)
order2 = dfs_it(graph, "A")
print(order2)
order3 = bfs_it(graph, "A")
print(order3)
