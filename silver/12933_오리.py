# https://www.acmicpc.net/problem/12933
# 오리
# 실버2 구현, 그리디, 문자열
# 32412KB 40ms 419B

sound = input()
duck = [0]
quack = {
    'q': 0,
    'u': 1,
    'a': 2,
    'c': 3,
    'k': 4
}

for i in sound:
    i = quack[i]
    if i in duck:
        if i == 4:
            duck[duck.index(i)] = 0
        else:
            duck[duck.index(i)] += 1
    elif i == 0:
        duck.append(1)
    else:
        print(-1)
        break
else:
    if sum(duck) == 0:
        print(len(duck))
    else:
        print(-1)


# [q, u, a, c, k]의 수를 세면서 하는 방법도 있다. append가 필요없어 시간이 단축된다.
# 32412KB 36ms 433B
# sound = input()
# quack = {
#     'q': 0,
#     'u': 1,
#     'a': 2,
#     'c': 3,
#     'k': 4
# }
lst = [0] * 5
cnt = 0
for i in sound:
    i = quack[i]
    if i == 0:
        lst[i] += 1
        if lst[-1]:
            lst[-1] -= 1
        else:
            cnt += 1
    else:
        if lst[i-1]:
            lst[i-1] -= 1
            lst[i] += 1
        else:
            lst[0] = 1
            break
print(cnt if sum(lst[:-1]) == 0 else -1)