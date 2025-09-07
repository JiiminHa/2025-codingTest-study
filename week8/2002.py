import sys

input = sys.stdin.readline

n = int(input().strip())

enter = [input().strip() for _ in range(n)]
exit_ = [input().strip() for _ in range(n)]

# 나간 차를 표시할 집합
gone = set()

p = 0          # enter에서 아직 안 나간 '첫 차'를 가리키는 포인터
ans = 0

for car in exit_:
    # 포인터가 가리키는 차가 이미 나갔다면, 아직 안 나간 첫 차를 찾을 때까지 전진
    while p < n and enter[p] in gone:
        p += 1
    
    # 아직 안 나간 첫 차와 지금 나가는 차가 다르면 => 추월
    if p < n and car != enter[p]:
        ans += 1
    
    # 현재 차는 나갔다고 표시
    gone.add(car)

print(ans)