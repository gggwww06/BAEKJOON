# 2606 바이러스
# 31120KB 48ms 557B

def dfs():
    stack = []
    visited[1] = 1
    v = 1
    while True:
        for w in arr[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                visited[w] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

N = int(input())
cp = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(cp):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0]*(N+1)
dfs()

print(sum(visited)-1)
