# https://www.acmicpc.net/problem/1780
# 종이의 개수
# 실버2 분할정복, 재귀
# 70232KB 3812ms 720B


def check_paper(sti, stj, gap):
    if gap == 1:
        pnum[paper[sti][stj]+1] += 1
    else:
        num = sum([sum(paper[sti + i][stj:stj+gap]) for i in range(gap)])
        if num == -gap**2:
            pnum[0] += 1
        elif num == gap**2:
            pnum[2] += 1
        elif sum([paper[sti + i][stj:stj+gap].count(0) for i in range(gap)]) == gap**2:
            pnum[1] += 1
        else:
            gap //= 3
            for i in range(3):
                for j in range(3):
                    check_paper(sti + gap*i, stj + gap*j, gap)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
pnum = [0, 0, 0]    # -1 0 1

check_paper(0, 0, N)
for i in range(3):
    print(pnum[i])