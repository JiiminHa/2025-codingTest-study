import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())  # M: 열, N: 행
board = [list(map(int, input().split())) for _ in range(N)]

dq = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            dq.append((i, j))

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
day = -1  # BFS 레벨(일수)

while dq:
    for _ in range(len(dq)):
        x, y = dq.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 1
                dq.append((nx, ny))
    day += 1

# 처음부터 다 익어 있었으면 day=0이 맞게 됨(위 레벨루프 설계상)
# 아직 0이 남아 있으면 -1
for row in board:
    if 0 in row:
        print(-1)
        break
else:
    print(max(day, 0))