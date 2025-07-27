n = int(input())  # 스위치 개수
switches = list(map(int, input().split()))  # 스위치 상태 입력

students = int(input())  # 학생 수

for _ in range(students):
    gender, num = map(int, input().split())  # 성별, 받은 수 입력
    if gender == 1:  # 남학생
        for i in range(num - 1, n, num):  # 배수인 인덱스만 탐색
            switches[i] = 1 - switches[i]  # 상태 반전
    else:  # 여학생
        idx = num - 1  # 0-indexed 위치
        left = right = idx
        while left - 1 >= 0 and right + 1 < n and switches[left - 1] == switches[right + 1]:
            left -= 1
            right += 1
        for i in range(left, right + 1):
            switches[i] = 1 - switches[i]

# 출력 형식 맞추기: 20개씩 끊어서 출력
for i in range(n):
    print(switches[i], end=' ')
    if (i + 1) % 20 == 0:
        print()