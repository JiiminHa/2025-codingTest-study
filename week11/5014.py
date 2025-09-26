from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [False] * (F + 1)
q = deque([(S, 0)])  # (현재층, 버튼횟수)
visited[S] = True

while q:
    floor, cnt = q.popleft()
    if floor == G:
        print(cnt)
        break
    for nxt in (floor + U, floor - D):
        if 1 <= nxt <= F and not visited[nxt]:
            visited[nxt] = True
            q.append((nxt, cnt + 1))
else:
    print("use the stairs")