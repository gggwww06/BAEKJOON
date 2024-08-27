# 1389 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389
# 31120KB 36ms 576B

def bfs(st):
    q = [st]
    visited = [-1]*(N+1)
    visited[st] = 0
    while q:
        w = q.pop(0)
        for i in arr[w]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[w]+1
        if not q:
            return sum(visited)

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
res = [0, N*N]
for i in range(1, N+1):
    tmp = bfs(i)
    if res[1] > tmp:
        res[0] = i
        res[1] = tmp
print(res[0])
