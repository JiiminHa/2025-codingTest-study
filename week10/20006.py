import sys
input = sys.stdin.readline

p, m = map(int, input().split())

rooms = []  

for _ in range(p):
    level, name = input().split()
    level = int(level)

    placed = False
    for room in rooms:
        if len(room["members"]) < m and abs(room["base"] - level) <= 10:
            room["members"].append((level, name))
            placed = True
            break

    if not placed:
        rooms.append({"base": level, "members": [(level, name)]})

for room in rooms:
    if len(room["members"]) == m:
        print("Started!")
    else:
        print("Waiting!")
    for lv, nm in sorted(room["members"], key=lambda x: x[1]):
        print(lv, nm)