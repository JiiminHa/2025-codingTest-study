w, h = map(int, input().split())
n = int(input())

P = 2 * (w + h)

def to_pos(d, dist):
    if d == 1:       # 북
        return dist
    elif d == 4:     # 동
        return w + dist
    elif d == 2:     # 남
        return w + h + (w - dist)
    else:            # 서
        return w + h + w + (h - dist)

shops = []
for _ in range(n):
    d, s = map(int, input().split())
    shops.append(to_pos(d, s))

gd, gs = map(int, input().split())
guard = to_pos(gd, gs)

ans = 0
for shop in shops:
    diff = abs(guard - shop)
    ans += min(diff, P - diff)

print(ans)