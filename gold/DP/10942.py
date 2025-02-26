# https://www.acmicpc.net/problem/10942
# 펠린드롬?
# 골드 4 다이나믹 프로그래밍
# KB ms B

import sys
input = sys.stdin.readline

N = int(input())
chilpan = list(map(int, input().split()))
M = int(input())
qst = [list(map(int, input().split())) for _ in range(M)]


def check_pel(a, b):
    for i in range((b-a+1)//2):
        if chilpan[a+i] != chilpan[b]:
            return 0
    return 1


# 각 시작점에서 pel인 위치 모두 저장
pel = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        pel[i][j] = check_pel(i, j)


for i in range(M):
    a, b = qst[i]
    print(pel[a-1][b-1])
