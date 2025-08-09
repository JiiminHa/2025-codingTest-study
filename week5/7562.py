import sys
from collections import deque
input = sys.stdin.readline

moves = [(-2,-1), (-1,-2), (1,-2), (2,-1),
         (2,1), (1,2), (-1,2), (-2,1)]

T = int(input().strip())
for _ in range(T):
    l = int(input().strip())
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())

    if (sx, sy) == (tx, ty):
        print(0)
        continue

    dist = [[-1]*l for _ in range(l)]
    dq = deque([(sx, sy)])
    dist[sx][sy] = 0

    while dq:
        x, y = dq.popleft()
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < l and 0 <= ny < l and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                if (nx, ny) == (tx, ty):
                    dq.clear()
                    break
                dq.append((nx, ny))

    print(dist[tx][ty])