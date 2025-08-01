import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기

n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]

# 양방향 그래프(트리) 입력 받기
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 부모를 저장할 배열 (1번 노드는 루트이므로 제외)
parent = [0] * (n + 1)

def dfs(current):
    for neighbor in graph[current]:
        if parent[neighbor] == 0:
            parent[neighbor] = current  
            dfs(neighbor)  # 자식 노드로 내려가기


dfs(1)


for i in range(2, n + 1):
    print(parent[i])