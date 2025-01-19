# https://www.acmicpc.net/problem/2578
# 빙고
# 실버4 구현, 시뮬레이션
# 32412KB 32ms 861B

# 빙고 개수 확인
def check_bingo(bi, bj):
    bg = 0
    # 가로
    if sum(bingopan[bi]) == 0:
        bg += 1
    # 세로
    if sum([bingopan[i][bj] for i in range(5)]) == 0:
        bg += 1
    # 대각선 \
    if bi == bj:
        if sum([bingopan[i][i] for i in range(5)]) == 0:
            bg += 1
    # 대각선 /
    if bi + bj == 4:
        if sum([bingopan[i][4-i] for i in range(5)]) == 0:
            bg += 1

    return bg

bingopan = [list(map(int, input().split())) for _ in range(5)]
called = [list(map(int, input().split())) for _ in range(5)]
bingo = 0

for tc in range(25):
    for i in range(5):
        for j in range(5):
            if bingopan[i][j] == called[tc//5][tc%5]:
                bingopan[i][j] = 0
                bingo += check_bingo(i, j)
                break

    if bingo >= 3:
        print(tc+1)
        break

'''
각 줄의 체크 개수를 모두 저장하는 방법
[가로 12345줄]
[세로 12345줄]
[대각선 / => 합이 4]
[대각선 \\ => 차가 0]
=> 매 횟수마다 

for n in bingo:
    i, j  = pos_lst[n]
    v[0][j] += 1
    v[1][i] += 1
    v[2][i+j] += 1
    v[3][i-j] += 1
    cnt = 0
    for tlst in v:
        cnt += tlst.count(5)
    if cnt >=3:
        break
print(sum(v[0]))
'''