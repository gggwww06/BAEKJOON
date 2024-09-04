# https://www.acmicpc.net/problem/1991
# 1991번 트리 순회
# 실버1 트리, 재귀
# 31120KB 36ms 532B

def orders(n):
    if n == 0:
        return
    preo.append(nodes[n])
    orders(nodes.index(tree[n][0]))
    ino.append(nodes[n])
    orders(nodes.index(tree[n][1]))
    posto.append(nodes[n])

N = int(input())
nodes = [0] * (N+1)
tree = [[] for _ in range(N+1)]
nodes[0] = '.'
for i in range(1, N+1):
    nd, lft, rgt = input().split()
    nodes[i] = nd
    tree[i] = [lft, rgt]
    preo = []   # 전위
    ino = []    # 중위
    posto = []   # 후위

orders(1)

print(''.join(preo))
print(''.join(ino))
print(''.join(posto))