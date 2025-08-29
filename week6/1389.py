import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    dist = [-1] * (N+1)
    dist[start] = 0
    q = deque([start])
    
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return sum(dist[1:])   # 1번부터 N번까지 거리 합

ans = (1, float('inf'))   # (번호, 케빈 합)

for i in range(1, N+1):
    s = bfs(i)
    if s < ans[1]:
        ans = (i, s)

print(ans[0])