# https://www.acmicpc.net/problem/10158
# 10158 개미
# 실버3 수학, 애드 혹, 사칙연산
# 31120KB 40ms 329B

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# w, h, p, q, t = map(int, open(0).read().split())

# 시간초과
# dx = dy = 1
# for _ in range(t):
#     if p == 0 or p == w:
#         dx = -dx
#     if q == 0 or q == h:
#         dy = -dy
#     p += dx
#     q += dy

# 가로
p += t
if (p // w) % 2:    # 벽에 홀수번 부딛힘
    p = w - p % w
else:   # 벽에 짝수번 부딛힘
    p = p % w
# 세로
q += t
if (q // h) % 2:    # 벽에 홀수번 부딛힘
    q = h - q % h
else:   # 벽에 짝수번 부딛힘
    q = q % h

print(p, q)