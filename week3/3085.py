def check(board):
    n = len(board)
    max_count = 1

    for i in range(n):
        # 행에서 최대 연속 찾기
        count = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

        # 열에서 최대 연속 찾기
        count = 1
        for j in range(1, n):
            if board[j][i] == board[j - 1][i]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

    return max_count


n = int(input())
board = [list(input().strip()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        # 오른쪽과 바꾸기
        if j + 1 < n:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            answer = max(answer, check(board))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        # 아래와 바꾸기
        if i + 1 < n:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            answer = max(answer, check(board))
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(answer)