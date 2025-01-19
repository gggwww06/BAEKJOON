# https://www.acmicpc.net/problem/2615
# 오목
# 실버1 구현, 브루트포스
# 32412KB 36ms 1522B

def check_win(i, j, n):
    garo = sero = dae1 = dae2 = 0

    # 가로
    for nj in range (j, 19):
        if omokpan[i][nj] == n:
            garo += 1
        else:
            break
    for nj in range (j-1, -1, -1):
        if omokpan[i][nj] == n:
            garo += 1
        else:
            break

    # 세로
    for ni in range(i, 19):
        if omokpan[ni][j] == n:
            sero += 1
        else:
            break
    for ni in range(i - 1, -1, -1):
        if omokpan[ni][j] == n:
            sero += 1
        else:
            break

    # 대각 \
    for k in range(19):
        if i+k < 19 and j+k < 19 and omokpan[i+k][j+k] == n:
            dae1 += 1
        else:
            break
    for k in range(1, 19):
        if i-k >= 0 and j-k >= 0 and omokpan[i-k][j-k] == n:
            dae1 += 1
        else:
            break

    # 대각 /
    for k in range(19):
        if i+k < 19 and j-k >= 0 and omokpan[i+k][j-k] == n:
            dae2 += 1
        else:
            break
    for k in range(1, 19):
        if i-k >= 0 and j+k < 19 and omokpan[i-k][j+k] == n:
            dae2 += 1
        else:
            break

    # 승
    if 5 in (garo, sero, dae1, dae2):
        print(n)
        print(i+1, j+1)
        return True
    else:
        return False

omokpan = [input().split() for _ in range(19)]

for i in range(19):
    for j in range(19):
        if omokpan[j][i] == '0':
            continue
        elif check_win(j, i, omokpan[j][i]):
            exit()
else:
    print(0)