# https://www.acmicpc.net/problem/1111
# 1111번: IQ Test
# gold 3

N = int(input())
lst = list(map(int, input().split()))
a = b = 0

if (N == 2 and lst[0] != lst[1]) or N <= 1:     # 다음 수가 여러 개
    print('A')
    exit()

# 앞 수 * a + b
# 4a + b = 13   -> a a a a b 13
# 13a + b = 40  -> a a a a a a a a a a a a a b 40 
# 9a = 27
# a = 3, b = 1

# a = (40-13)/(13-4)
# b = 13 - 4*a

if N == 2:
    a = 1
    b = 0
else:
    for i in range(N-2):
        a = (lst[i+2]-lst[i+1])/(lst[i+1]-lst[i])
        b = lst[i+1] - lst[i] * a
        # a, b 값이 바뀌거나 a가 정수가 아니면

print(a, b)

if a == int(a):
    print(lst[N-1] * a + b)
else:       # 다음 수를 구할 수 없음
    print('B')