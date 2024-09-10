# https://www.acmicpc.net/problem/17478
# 17478: 재귀함수가 뭔가요?
# 실버5: 구현, 재귀
# 31120KB 32ms 903B

pstr = {
    1 : '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.',
    2 : '"재귀함수가 뭔가요?"',
    3 : '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
    4 : '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
    5 : '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."',
    6 : '"재귀함수는 자기 자신을 호출하는 함수라네"',
    7 : '라고 답변하였지.'
}

def m_print(n, lst):
    und = '____' * n
    for i in lst:
        print(f'{und}{pstr[i]}')


def rec(n):
    if n == N:
        m_print(n, [2, 6, 7])
        return
    m_print(n, [2, 3, 4, 5])
    rec(n+1)
    m_print(n, [7])


N = int(input())
m_print(0, [1])
rec(0)
