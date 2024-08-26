# 2178 미로탐색
# https://www.acmicpc.net/problem/2178
# 31120KB 60ms 689B

def bfs():
    q = [(0, 0)]
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] != 0 and visited[ni][nj] == 0:
                arr[ni][nj] = arr[i][j] + 1
                q.append((ni, nj))
                visited[ni][nj] = 1
            if (ni, nj) == (N-1, M-1):
                return(arr[ni][nj])


N, M = map(int, input().split())
arr_in = [input() for _ in range(N)]
arr = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        arr[i][j] = int(arr_in[i][j])
print(bfs())