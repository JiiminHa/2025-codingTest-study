N, M, B = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

min_time = float('inf')
best_height = 0

for h in range(257):  # 0~256 높이 전부 시도
    remove = 0
    place = 0
    for y in range(N):
        for x in range(M):
            diff = land[y][x] - h
            if diff > 0:
                remove += diff  # 블록 캐기
            elif diff < 0:
                place -= diff   # 블록 놓기 (음수니까 부호 반대)

    if remove + B >= place:
        time = (remove * 2) + (place * 1)
        if time < min_time or (time == min_time and h > best_height):
            min_time = time
            best_height = h

print(min_time, best_height)