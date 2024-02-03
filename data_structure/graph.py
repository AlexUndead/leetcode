inc = {
    1: [2, 8],
    2: [1, 3, 8],
    3: [2, 4, 8],
    4: [3, 7, 9],
    5: [6, 7],
    6: [5],
    7: [4, 5, 8],
    8: [1, 2, 3, 7],
    9: [4],
}

def dfs(start, graph):
    visit = []

    def _dfs(vertex):
        nonlocal visit
        nonlocal graph
        if vertex not in visit:
            print(vertex)
            visit.append(vertex)

            for link_vert in graph[vertex]: 
                _dfs(link_vert)

    _dfs(start)

#dfs(1, inc)

def bfs(start, graph):
    visit = []
    deq = [start]

    while deq:
        copy_deq = deq[:]
        deq = []
        for vert in copy_deq:
            if vert not in visit:
                print(vert)
                visit.append(vert)
                deq += graph[vert]

bfs(1, inc)
