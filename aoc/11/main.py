from functools import lru_cache

def parse(text: str):

    graph = dict()

    for line in text.split("\n"):
        node, neighbours = line.split(":")
        graph[node.strip()] = neighbours.strip().split()

    return graph


def search(nodes: dict[str, list[str]]):

    paths = 0

    queue = nodes["you"]
    visited = set()

    while queue:
        node = queue.pop()

        for nbr in nodes[node]:
            if nbr == "out":
                paths += 1
            elif nbr not in visited:
                queue.append(nbr)

    return paths


def search_with_hubs(graph: dict[str, list[str]]):

    @lru_cache(maxsize=None)
    def reachable(cur, dac, fft):
        if cur == "out":
            return dac and fft
        else:
            if cur == "dac":
                dac = True
            if cur == "fft":
                fft = True
            return sum([reachable(x, dac, fft) for x in graph[cur]])

    return reachable("svr", False, False)

