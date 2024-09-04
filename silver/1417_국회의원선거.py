# https://www.acmicpc.net/problem/1417
# 1417 국회의원 선거
# 실버5 구현, 자료 구조, 그리디, 시뮬레이션, 우선순위 큐
# 31120KB 40ms 194B

N = int(input())
arr = [int(input()) for _ in range(N)]
dasom = arr[0]
arr2 = arr[1:]

while arr2 and dasom <= max(arr2):
    arr2[arr2.index(max(arr2))] -= 1
    dasom += 1

print(dasom-arr[0])