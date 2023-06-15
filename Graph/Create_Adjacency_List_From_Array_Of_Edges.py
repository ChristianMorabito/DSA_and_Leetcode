def create_graph(edges):
    graph = {}
    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph


#                  {
e = [['i', 'j'],  # 'i': ['j', 'k'],
     ['k', 'i'],  # 'j': ['i'],
     ['m', 'k'],  # 'k': ['i', 'm', 'l'],
     ['k', 'l'],  # 'm': ['k'],
     ['o', 'n']]  # 'l': ['k'],
#                   'o': ['n'],
#                   'n': ['o']
#                              }

print(create_graph(e))
