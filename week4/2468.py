import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, height, visited):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] > height:
                dfs(nx, ny, height, visited)

max_safe = 0

# 모든 가능한 강수량에 대해 시뮬레이션
for h in range(0, max(map(max, graph)) + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                dfs(i, j, h, visited)
                count += 1
    max_safe = max(max_safe, count)

print(max_safe)