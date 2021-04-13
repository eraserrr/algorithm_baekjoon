N = int(input())
stats = []
for i in range(N):
    stats.append(list(map(int, input().split())))

stats_sum = {}
for i in range(N):
    for j in range(i):
        stats_sum[j,i] = stats[i][j] + stats[j][i]

from itertools import combinations
score = []
for comb in list(combinations(range(N), int(N/2))):
    op = [x for x in range(N) if x not in comb]
    print(comb, op)
    score1= 0
    score2 = 0
    for comb2 in list(combinations(comb, 2)):
        print(comb2)
        score1 += stats_sum[comb2]
    print(score1)
    for comb2 in list(combinations(op, 2)):
        print(comb2)
        score2 += stats_sum[comb2]
    print(score2)
    score.append(abs(score2-score1))

print('정답', min(score))
