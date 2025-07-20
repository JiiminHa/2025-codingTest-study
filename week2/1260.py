from collections import deque

N, M, V = map(int, input().split())

# 인접 리스트 생성
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 순서를 위해 정렬
for neighbors in graph:
    neighbors.sort()

# DFS
def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited)

# BFS
def bfs(v):
    visited = [False] * (N + 1)
    queue = deque([v])
    visited[v] = True

    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 실행
visited = [False] * (N + 1)
dfs(V, visited)
print()
bfs(V)