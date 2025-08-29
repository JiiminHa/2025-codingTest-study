import sys

def wins(b, ch):
    line = [
        [0,1,2],[3,4,5],[6,7,8],    # 가로
        [0,3,6],[1,4,7],[2,5,8],    # 세로
        [0,4,8],[2,4,6]             # 대각
    ]
    return any(all(b[i]==ch for i in L) for L in line)

for line in sys.stdin:
    s = line.strip()
    if s == 'end': break

    cntX = s.count('X')
    cntO = s.count('O')
    ok_cnt = (cntX == cntO) or (cntX == cntO+1)
    if not ok_cnt:
        print('invalid'); continue

    wx = wins(s, 'X')
    wo = wins(s, 'O')

    if wx and wo:
        print('invalid'); continue
    if wx and cntX != cntO+1:
        print('invalid'); continue
    if wo and cntX != cntO:
        print('invalid'); continue

    # 아무도 안 이김 -> 보드가 가득 차 있어야 최종 상태
    if not wx and not wo and '.' in s:
        print('invalid'); continue

    print('valid')