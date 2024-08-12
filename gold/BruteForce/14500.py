# https://www.acmicpc.net/problem/14500
# 14500번 : 테트로미노
# gold 5
# 구현, 브루트포스 알고리즘

# 너무 깊음
# def tetromino(a, b, sq_num, snum, v):
#     if a >= N or b >= M:
#         return 0
#     elif sq_num == 4:
#         return snum
#     elif v[a][b] == 1:
#         tetromino(a+1, b, sq_num, snum, v)
#         tetromino(a, b+1, sq_num, snum, v)
#         tetromino(a-1, b, sq_num, snum, v)
#         tetromino(a, b-1, sq_num, snum, v)
#     else:
#         sq_num += 1
#         snum += arr[a][b]
#         v[a][b] = 1
#         tetromino(a+1, b, sq_num, snum, v)
#         tetromino(a, b+1, sq_num, snum, v)
#         tetromino(a-1, b, sq_num, snum, v)
#         tetromino(a, b-1, sq_num, snum, v)

# 도형 모양 모음
# tetromino = [
#     [(0, 1), (0, 2), (0, 3)],   # ㅡ
#     [(1, 0), (2, 0), (3, 0)],   # ㅣ
#     [(0, 1), (1, 0), (1, 1)],   # ㅁ
#     [(1, 0), (1, 1), (2, 1)],   # u
#     [(0, 1), (-1, 1), (-1, 2)], # s
#     [(1, 0), (2, 0), (2, 1)],   # ㄴ
#     [(0, 1), (0, 2), (-1, 2)],
#     [(0, 1), (1, 1), (2, 1)],   # ㄱ
#     [(1, 0), (0, 1), (0, 2)],
#     [(0, 1), (0, 2), (1, 1)],   # ㅜ
#     [(-1, 1), (0, 1), (1, 1)],  # ㅓ
#     [(-1, 1), (0, 1), (0, 2)],  # ㅗ
#     [(1, 0), (1, 1), (2, 0)]    # ㅏ 
# ]

# 도형 모양 모음
tetromino = []
v = [[0]*4 for _ in range(4)]
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

res = 0
for i in range(N):
    for j in range(M):
        for k in range(len(tetromino)):
            s = arr[i][j]
            for a, b in tetromino[k]:
                di = i + a
                dj = j + b
                if 0 <= di < N and 0 <= dj < M:
                    s += arr[di][dj]
                else:
                    break
            else:
                res = max(res, s)

print(res)