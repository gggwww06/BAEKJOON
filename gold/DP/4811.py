# https://www.acmicpc.net/problem/4811
# 4811번 : 알약
# gold 5
# 수학, 다이나믹 프로그래밍

def eat(arr, w, h):
    global res
    if w < h: 
        return 0
    elif len(arr) < 2*N:
        if w < N and h < N:
            eat(arr+'w', w+1, h)
            eat(arr+'h', w, h+1)
        elif w == N:
            res += 1
            return 0
    else:
        res += 1


    
res = 0
N = int(input())
while N != 0:
    res = 0
    eat('', 0, 0)

    print(res)

    N = int(input())