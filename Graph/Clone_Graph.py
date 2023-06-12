class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def __repr__(self):
        return f"(NODE{self.value})"

    def create_neighbors(self, neighbors):
        self.neighbors = [n for n in neighbors]


def clone_graph(node):
    node_map = {}

    def dfs(curr):
        clone = Node(curr.value)
        node_map[curr.value] = clone
        for neighbor in curr.neighbors:
            if neighbor.value not in node_map:
                dfs(neighbor)
            clone.neighbors.append(node_map[neighbor.value])


    return dfs(node) if node else None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.create_neighbors([node2, node3])
node2.create_neighbors([node1, node3])
node3.create_neighbors([node2, node1])

clone_graph(node1)