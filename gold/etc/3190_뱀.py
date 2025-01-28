# https://www.acmicpc.net/problem/3190
# 뱀
# 골드4 구현, 자료구조, 시뮬레이션, 덱, 큐
# 32412KB 56ms 1156B

# N, K, *arr = open('../../input.txt').read().split()
# snake = [1, 1]
# N, K = int(N), int(K)
# apple = [[] for _ in range(K)]
# for i in range(K):
#     apple[i] = [int(arr[2*i]), int(arr[2*i + 1])]
# L = int(arr[2*K])
# snake_turn = [[] for _ in range(L)]
# for i in range(L):
#     snake_turn[i] = [int(arr[2*K + 2*i + 1]), arr[2*K + 2*i + 2]]
#
# print(N, K, apple, L, snake_turn)

def snake_move():
    # 이동
    snake.append([snake[-1][0] + snake_dir[0], snake[-1][1] + snake_dir[1]])
    # 충돌 확인
    if snake[-1] in snake[:-1] or snake[-1][0] < 1 or snake[-1][0] > N or snake[-1][1] < 1 or snake[-1][1] > N:
        return 1
    # 사과 먹으면
    if snake[-1] in apple:
        apple.pop(apple.index(snake[-1]))
    else:
        snake.pop(0)
    return 0


def change_dir(snake_dir, dir):
    idx = dxy.index(snake_dir)
    if dir == 'L':
        snake_dir = dxy[idx-1]
    else:
        snake_dir = dxy[(idx+1) % 4]
    return snake_dir


def snake_run(sec):
    global end_sec
    for _ in range(int(sec) - end_sec):
        end_sec += 1
        if snake_move():
            return 1
    return 0


dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

snake = [[1, 1]]
snake_dir = [0, 1]
end_sec = 0
N = int(input())
K = int(input())
apple = [[] for _ in range(K)]
for i in range(K):
    apple[i] = list(map(int, input().split()))
L = int(input())
for i in range(L):
    sec, dir = input().split()
    if snake_run(sec):
        break
    snake_dir = change_dir(snake_dir, dir)
else:
    snake_run(end_sec + N)

print(end_sec)

# 처음에 문제 이해를 잘못해서 코드가 구질구질해졌는데 수정하기 귀찮음
# 그냥 입력 다 받고 while True 해놓고 1초씩 증가시키는 형태로 하는 게 더 빠르다.