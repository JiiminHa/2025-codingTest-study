from itertools import permutations

N = int(input())
inning = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for order in permutations(range(1, 9)):  # 2~9번 선수
    lineup = list(order[:3]) + [0] + list(order[3:])  # 0번이 1번 선수
    score, batter = 0, 0
    for i in range(N):  # 이닝 반복
        out = 0
        b1 = b2 = b3 = 0
        while out < 3:
            result = inning[i][lineup[batter]]
            if result == 0:
                out += 1
            elif result == 1:  # 안타
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif result == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif result == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else:  # 홈런
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            batter = (batter + 1) % 9
    answer = max(answer, score)

print(answer)