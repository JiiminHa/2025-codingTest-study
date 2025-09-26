from collections import Counter

first = input().strip()
n = int(input())
base = Counter(first)
ans = 0

for _ in range(n-1):
    word = input().strip()
    diff = sum((base - Counter(word)).values()) + sum((Counter(word) - base).values())
    if diff <= 2 and abs(len(first) - len(word)) <= 1:
        ans += 1

print(ans)