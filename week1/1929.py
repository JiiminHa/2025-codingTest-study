N, M = map(int, input().split())

for i in range(N, M+1):
    if i == 1: # 1은 통과
        continue
        
    for j in range(2, int(i**0.5) + 1): # 2 ~ 제곱근 사이 값 확인
        if i % j == 0: 
            break
    else: 
        print(i)