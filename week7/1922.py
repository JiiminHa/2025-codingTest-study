import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

parent = list(range(N+1))
rank = [0]*(N+1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb: return False
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True

cost = 0
cnt = 0
for w, u, v in edges:
    if union(u, v):
        cost += w
        cnt += 1
        if cnt == N-1: break

print(cost)