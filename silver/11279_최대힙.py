# https://www.acmicpc.net/problem/11279
# 11279 최대 힙
# 실버2 자료 구조, 우선순위 큐
# 42036KB 168ms 670B

# 최대 힙
def enq(n):
    global last
    last += 1
    h[last] = n
    c = last
    p = c//2
    while p >= 1 and h[p] < h[c]:
        h[p], h[c] = h[c], h[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = h[1]
    h[1] = h[last]
    last -= 1
    p = 1
    c = p*2
    while c <= last:
        if c+1 <= last and h[c] < h[c+1]:
            c += 1
        if h[p] < h[c]:
            h[p], h[c] = h[c], h[p]
            p = c
            c = p*2
        else:
            break
    return tmp

N, *arr = map(int, open(0).read().split())
h = [0] * (N+1)
last = 0

for x in arr:
    enq(x)
    if x == 0:  # 출력 후 제거
        print(deq())
