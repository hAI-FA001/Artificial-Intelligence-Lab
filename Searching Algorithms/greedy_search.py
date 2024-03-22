from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.graph = {
"A": [(146, ("A", "O")), (140, ("A", "S")), (494, ("A", "C"))],
"O": [(146, ("O", "A")), (151, ("O", "S"))],
"S": [(151, ("S", "O")), (140, ("S", "A")),(80, ("S", "R")),(99, ("S", "F"))],
"C": [(494, ("C", "A")), (146, ("C", "R"))],
"R": [(80, ("R", "S")), (146, ("R", "C")), (97, ("R", "P"))],
"F": [(99, ("F", "S")), (211, ("F", "B"))],
"B": [(211, ("B", "F")), (101, ("B", "P"))],
"P": [(101, ("P", "B")), (97, ("P", "R")), (138, ("P", "C"))]
                            }
        self.edges = {}
        self.weights = {}
        self.heuristics = {
            'A': 10,
            'O': 9,
            'S': 7,
            'C': 8,
            'R': 6,
            'F': 5,
            'P': 3,
            'B': 0
        }

        self.populate_edges()
        self.populate_weights()
        print("edges : ", self.edges)
        print("weights  : ", self.weights)

    def populate_edges(self):
        for key in self.graph:
            neighbours = []
            for each_tuple in self.graph[key]:
                neighbours.append(each_tuple[1][1])
            self.edges[key] = neighbours

    def populate_weights(self):
        for key in self.graph:
            neighbours = self.graph[key]
            for each_tuple in neighbours:
                self.weights[each_tuple[1]] = each_tuple[0]

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node,  to_node)]

    def get_heuristics(self, node):
        return self.heuristics[node]

def greedy_search(graph, start, goal):
    visited = []
    queue = PriorityQueue()
    queue.put((graph.get_heuristics(start), start))

    while not queue.empty():
        curHeuristic, currentNode = queue.get()

        if currentNode not in visited:
            visited.append(currentNode)
            if currentNode == goal:
                break

        for neighbor in graph.neighbors(currentNode):
            if neighbor not in visited:
                queue.put((graph.get_heuristics(neighbor), neighbor))

    return visited

def findPath(graph, visited):
    curNode = visited.pop()
    path = [curNode]
    for node in reversed(visited):
        if curNode in graph.neighbors(node):
            curNode = node
            path.append(curNode)
    return list(reversed(path))

graph = Graph()
solution = greedy_search(graph, 'A', 'B')
print('Whole Traversal: \t', solution)
print('Path: \t', findPath(graph, solution))