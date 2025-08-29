import sys
input = sys.stdin.readline

N = int(input().strip())                  # 사진틀 수
_ = int(input().strip())                  # 총 추천 수(사용만 하고 변수명은 안 써도 됨)
recs = list(map(int, input().split()))    # 추천 시퀀스

frames = {}   # student -> [count, time]
time = 0

for s in recs:
    time += 1
    if s in frames:
        # 이미 걸려 있으면 추천수만 증가
        frames[s][0] += 1
    else:
        if len(frames) < N:
            # 빈자리가 있으면 올림
            frames[s] = [1, time]
        else:
            # 교체: (추천수 오름차순, 게시시각 오름차순)
            to_remove = min(frames.items(), key=lambda item: (item[1][0], item[1][1]))[0]
            del frames[to_remove]
            frames[s] = [1, time]

# 최종 남은 학생 오름차순 출력
print(*sorted(frames.keys()))