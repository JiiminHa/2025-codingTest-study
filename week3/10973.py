n = int(input())
arr = list(map(int, input().split()))

i = n - 1
# 1. 뒤에서부터 처음으로 감소하는 위치 찾기
while i > 0 and arr[i - 1] <= arr[i]:
    i -= 1

if i <= 0:
    print(-1)
else:
    # 2. i-1보다 작은 수 중 가장 큰 수 찾기
    j = n - 1
    while arr[j] >= arr[i - 1]:
        j -= 1
    # 3. 교환
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # 4. i부터 끝까지 내림차순 (reverse)
    arr[i:] = reversed(arr[i:])
    print(*arr)