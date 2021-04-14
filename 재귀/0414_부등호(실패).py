# 각 인덱스마다 연속된 부등호의 깊이를 계산
# 최댓값을 구할때는 < > 가 쌓인 깊이
# 최솟값을 구할때는 > < 가 쌓인 깊이
# 레벨 별로 가장 높은 숫자부터 번호 부여 (최댓값)

# 9
# < < < > < < > < >
# 0<1<2<3>0<1<2>0<1>0
# <<<9><<><>
# <<8<9><<7><>
# <6<7<9><5<8><4>
# 3<6<7<9>2<5<8>1<4>0

k = int(input())
exp_list = input().split()

Z = list(range(10))
answer_max = [-1]* (k+1)
answer_min = [-1]*(k+1)
level = [1] * (k+1)

for i in range(len(exp_list)-1):
    if exp_list[i]=='>' and exp_list[i+1]=='<':
        level[i+1]= 0

for i in range(len(exp_list[:-1])):
    if exp_list[i]=='<':
        level[i+1] = level[i]+1

for i in range(len(exp_list)-1,1,-1):
    if exp_list[i]=='>':
        level[i+1] = level[i]-1

print(level)

cur_level = max(level)
Z = Z[len(Z)-k-1:]
while(Z):
    for i in range(len(level)):
        if level[i]==cur_level:
            answer_max[i] = Z.pop(-1)
    cur_level -= 1

# print(''.join([str(x) + ' ' + y for x,y in zip(answer_max, exp_list+[' '])]))

cur_level = min(level)
Z = list(range(10))
Z = Z[:k+1]
while(Z):
    for i in range(len(level)):
        if level[i]==cur_level:
            answer_min[i] = Z.pop(0)
    cur_level += 1

# print(''.join([str(x) + ' ' + y for x, y in zip(answer_min, exp_list + [' '])]))

print(''.join(map(str,answer_max)))
print(''.join(map(str,answer_min)))
