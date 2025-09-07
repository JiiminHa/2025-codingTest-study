from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

# 집, 치킨집 좌표 따로 저장
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

ans = 10**9

# 치킨집 중 m개 선택하는 모든 경우
for comb in combinations(chickens, m):
    total = 0
    # 각 집마다, 선택된 치킨집 중 최소거리 찾기
    for hx, hy in houses:
        dist = min(abs(hx - cx) + abs(hy - cy) for cx, cy in comb)
        total += dist
    ans = min(ans, total)

print(ans)