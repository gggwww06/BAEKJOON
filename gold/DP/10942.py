# https://www.acmicpc.net/problem/10942
# 팰린드롬?
# 골드 4 다이나믹 프로그래밍
# KB ms B

import sys
input = sys.stdin.readline

N = int(input())
chilpan = list(map(int, input().split()))
M = int(input())
qst = [list(map(int, input().split())) for _ in range(M)]
pel = [[0] * (N) for _ in range(N)]

# 각 시작점에서 pel인 위치 모두 저장
for i in range(N):
    for a in range(N):
        b = a+i
        if b >= N:
            continue
        elif i == 0:
            pel[a][b] = 1
        elif i == 1:
            if chilpan[a] == chilpan[b]:
                pel[a][b] = 1
        else:
            if pel[a+1][b-1] and chilpan[a] == chilpan[b]:
                pel[a][b] = 1


for i in range(M):
    a, b = qst[i]
    print(pel[a-1][b-1])


# 모든 위치에서 팰린드롬이 될 수 있는 최대 길이를 저장
# + 중심이 홀수인 경우, 짝수인 경우 저장
#
# input = sys.stdin.readline
# n = int(input())
# *a, = [0]+list(map(int, input().split()))
# m = int(input())
# dp = [0]*(n*2+1)
# for i in range(n*2+1):
#     p = q = i//2
#     q += i & 1
#     while p > 0 and q <= n and a[p] == a[q]:
#         p -= 1
#         q += 1
#     dp[i] = p
# ans = ''
# for _ in range(m):
#     s, e = map(int, input().split())
#     i = s+e
#     ans += '1\n' if dp[i] < s else '0\n'
# print(ans)
