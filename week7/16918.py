import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

# 상하좌우
DIRS = [(-1,0),(1,0),(0,-1),(0,1)]

def explode(grid):
    # 다음 짝수 시각엔 가득 채워짐 → 일단 모두 'O'로 만든 뒤,
    filled = [['O'] * C for _ in range(R)]
    # 이번에 터질 위치들(현재 grid에서 'O'였던 자리 + 이들의 인접칸)을 '.'으로 비운다
    to_clear = [[False]*C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if grid[y][x] == 'O':
                to_clear[y][x] = True
                for dy, dx in DIRS:
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < R and 0 <= nx < C:
                        to_clear[ny][nx] = True
    for y in range(R):
        for x in range(C):
            if to_clear[y][x]:
                filled[y][x] = '.'
    return filled

if N == 1:
    # 초기 상태 그대로
    result = board
elif N % 2 == 0:
    # 짝수초엔 전체 폭탄
    result = [['O'] * C for _ in range(R)]
else:
    # 홀수(>=3): t=3 상태와 t=5 상태만 준비해두고 모듈러로 선택
    t3 = explode(board)      # 초기 폭탄들이 터진 뒤 상태
    t5 = explode(t3)         # 그 다음 폭탄들이 터진 뒤 상태
    if N % 4 == 3:
        result = t3
    else:  # N % 4 == 1
        result = t5

for row in result:
    print(''.join(row))