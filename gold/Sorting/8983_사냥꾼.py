# https://www.acmicpc.net/problem/8983
# 사냥꾼
# 골드4 정렬, 이분탐색
# 45400KB 240ms 621B

from bisect import bisect_left
import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
sadae = sorted(map(int, input().split()))

res = 0

for _ in range(N):
    a, b = map(int, input().split())
    idx = bisect_left(sadae, a)
    if idx == M:
        x = sadae[idx-1]
        if abs(x-a) + b <= L:
            res += 1
    else:
        x = sadae[idx]
        if abs(x-a) + b <= L:
            res += 1
        elif idx:
            x = sadae[idx-1]
            if abs(x-a) + b <= L:
                res += 1

print(res)

# 다른 방법
# cut = False
# if idx > 0:
#     if abs(a - sadae[idx - 1]) + b <= L:
#         cut = True
# if idx < M:
#     if abs(a - sadae[idx]) + b <= L:
#         cut = True
# if cut:
#     res += 1

# +) abs함수가 직접 비교하는 것 보다 더 빠르다! 매우 최적화되어있다네요