import sys
input = sys.stdin.readline

n = int(input())
flowers = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    start = sm * 100 + sd
    end = em * 100 + ed
    flowers.append((start, end))

flowers.sort()  # 시작일 기준 정렬

target = 301
end_day = 1130
cnt = 0
idx = 0
max_end = 0

while target <= end_day:
    found = False
    while idx < n and flowers[idx][0] <= target:
        if flowers[idx][1] > max_end:
            max_end = flowers[idx][1]
        idx += 1
        found = True
    if not found:  # 이어갈 수 있는 꽃이 없음
        print(0)
        exit(0)
    cnt += 1
    target = max_end  # 가장 길게 이어주는 꽃으로 갱신
    if target > end_day:
        print(cnt)
        exit(0)

print(0)  # 못 덮으면 0