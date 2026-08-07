from collections import deque
def bfs_of_graph(adj: list[list[int]]) -> list[int]:
    n = len(adj)
    visited = [False] * n
    result = []
    queue = deque()

    visited[0] = True
    queue.append(0)

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return result