# https://www.acmicpc.net/problem/2239
# 2239: 스도쿠
# 골드4: 구현, 백트래킹
#

def sudoku(n, pz):
    if n == 81 :
        res.append(pz)
    a, b = n//9, n%9
    num = arr[a][b]
    if num == '0':
        garo = arr[a][:]
        sero = [arr[j][b] for j in range(9)]
        nemo = []
        for i in range():
            for j in range():
                nemo.append()
        for i in list(map(str, list(range(1,10)))):
            if i not in arr[n//9][:] and


arr = [input() for _ in range(9)]
res = []

sudoku(0, arr[:])

