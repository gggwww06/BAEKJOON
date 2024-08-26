# 1260 DFS와 BFS
# 32140KB 280ms 902B
# https://www.acmicpc.net/problem/1260

def dfs(st):
    visited = [0]*(N+1)
    stack = []
    visited[st] = 1
    w = st
    print(w, end=" ")
    while True:
        for i in arr[w]:
            if visited[i] == 0:
                stack.append(w)
                visited[i] = 1
                w = i
                print(w, end=" ")
                break
        else:
            if stack:
                w = stack.pop()
            else:
                return

def bfs(st):
    visited = [0]*(N+1)
    q = [st]
    visited[st] = 1
    while q:
        w = q.pop(0)
        print(w, end=" ")
        for i in arr[w]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1


N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
arr = list(map(sorted, arr))

dfs(V)
print()
bfs(V)
print()