import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

bridge = deque([0]*w)  # 다리 위 상태
time = 0
cur_weight = 0

while trucks or cur_weight > 0:
    time += 1
    # 한 칸 전진
    out = bridge.popleft()
    cur_weight -= out

    if trucks and cur_weight + trucks[0] <= L:
        t = trucks.popleft()
        bridge.append(t)
        cur_weight += t
    else:
        bridge.append(0)

print(time)