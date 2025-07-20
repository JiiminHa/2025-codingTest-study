from collections import deque

# 입력
N = int(input())
grid = [list(input().strip()) for _ in range(N)]

# 색약 시야용 grid (G를 R로 바꿔줌)
color_blind_grid = [[c if c != 'G' else 'R' for c in row] for row in grid]

# 방향 벡터: 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# BFS 함수
def bfs(x, y, visited, grid):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    color = grid[y][x]

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[ny][nx] and grid[ny][nx] == color:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

# 일반 시야용 visited
visited_normal = [[False]*N for _ in range(N)]
count_normal = 0

for y in range(N):
    for x in range(N):
        if not visited_normal[y][x]:
            bfs(x, y, visited_normal, grid)
            count_normal += 1

# 색약 시야용 visited
visited_blind = [[False]*N for _ in range(N)]
count_blind = 0

for y in range(N):
    for x in range(N):
        if not visited_blind[y][x]:
            bfs(x, y, visited_blind, color_blind_grid)
            count_blind += 1

# 결과 출력
print(count_normal, count_blind)