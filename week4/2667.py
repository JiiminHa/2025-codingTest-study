n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    count = 1  # 현재 집 포함

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                count += dfs(nx, ny)
    return count

result = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            result.append(dfs(i, j))

result.sort()
print(len(result))  # 총 단지 수
for r in result:
    print(r)        # 각 단지의 집 수