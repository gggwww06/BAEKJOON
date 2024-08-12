# https://www.acmicpc.net/problem/4811
# 4811번 : 알약
# gold 5
# 수학, 다이나믹 프로그래밍
# 31120KB 72ms 305B

# 시간초과
# def eat(arr, w, h):
#     global res
#     if w < h: 
#         return 0
#     elif len(arr) < 2*N:
#         if w < N and h < N:
#             eat(arr+'w', w+1, h)
#             eat(arr+'h', w, h+1)
#         elif w == N:
#             res += 1
#             return 0
#     else:
#         res += 1

# An,n = An-1,n + An,n-1
arr = [[0]*31 for _ in range(31)]
for i in range(1, 31):
    arr[i][0] = 1
    for j in range(1, 31):
        if i < j:
            continue
        else:
            arr[i][j] = arr[i-1][j] + arr[i][j-1]


N = int(input())
while N != 0:
    print(arr[N][N])

    N = int(input())