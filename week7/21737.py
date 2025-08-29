import sys

s = sys.stdin.readline().strip()

def div_toward_zero(a, b):
    # C++14의 정수 나눗셈처럼 0을 향해 절단
    if b == 0:
        raise ZeroDivisionError
    sign = -1 if (a < 0) ^ (b < 0) else 1
    return sign * (abs(a) // abs(b))

ans = []
cur = None          # 누적 값
op = None           # 직전 연산자 (S M U P)
num = 0             # 현재 읽는 수(여러 자리)

for ch in s:
    if ch.isdigit():
        num = num * 10 + (ord(ch) - 48)
        continue

    # ch가 연산 문자거나 C인 경우, 직전 op로 cur 갱신
    if cur is None:
        cur = num
    else:
        if op == 'S': cur += num
        elif op == 'M': cur -= num
        elif op == 'U': cur *= num
        elif op == 'P': cur = div_toward_zero(cur, num)
    num = 0

    if ch == 'C':
        ans.append(str(cur))
        # C 이후에도 cur은 유지, 다음 연산자로 계속 진행
    else:
        op = ch  # S/M/U/P 중 하나

print('\n'.join(ans))