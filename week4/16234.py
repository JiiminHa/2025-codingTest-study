from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    union = [(x, y)]
    total = graph[x][y]

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[cx][cy] - graph[nx][ny]) <= r:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    union.append((nx, ny))
                    total += graph[nx][ny]
    # 연합 구성 완료
    if len(union) > 1:
        avg = total // len(union)
        for x, y in union:
            graph[x][y] = avg
        return True  # 인구 이동 발생
    return False

day = 0
while True:
    visited = [[False]*n for _ in range(n)]
    moved = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    moved = True
    if not moved:
        break
    day += 1

print(day)