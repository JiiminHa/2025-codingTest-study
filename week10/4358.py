import sys

input = sys.stdin.readline
dic = {}
sum_tree = 0

while True:
    text = input().rstrip()
    if not text:
        break

    if text in dic:
        dic[text] += 1
    else:
        dic[text] = 1
    sum_tree += 1

for tree in sorted(dic.keys()):
    print(f"{tree} {dic[tree] / sum_tree * 100:.4f}")