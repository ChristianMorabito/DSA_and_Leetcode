def create_graph(edges):
    graph = {}
    for array in edges:
        a = array[0]
        b = array[1]
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


graph = create_graph(e)
