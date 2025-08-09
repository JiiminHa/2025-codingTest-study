import sys
input = sys.stdin.readline

K = int(input().strip())
dirs = []
lens = []
for _ in range(6):
    d, l = map(int, input().split())
    dirs.append(d); lens.append(l)

# 가로 최대변, 세로 최대변 위치 찾기
max_w = 0; iw = -1  # 방향 1(동), 2(서)만 가로
max_h = 0; ih = -1  # 방향 3(남), 4(북)만 세로
for i, (d, l) in enumerate(zip(dirs, lens)):
    if d in (1, 2) and l > max_w:
        max_w = l; iw = i
    if d in (3, 4) and l > max_h:
        max_h = l; ih = i

small_w = lens[(iw+3) % 6]
small_h = lens[(ih+3) % 6]

area = max_w*max_h - small_w*small_h
print(area * K)