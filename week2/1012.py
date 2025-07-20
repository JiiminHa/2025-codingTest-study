from collections import deque

def bfs(x, y, graph, visited):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    dx = [0, 0, -1, 1]  # 좌우
    dy = [-1, 1, 0, 0]  # 상하

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph):
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())  # M: 가로, N: 세로
    graph = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and not visited[y][x]:
                bfs(x, y, graph, visited)
                count += 1
    print(count)