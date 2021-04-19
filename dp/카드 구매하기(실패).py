N = int(input())
pack = []

pack = list(map(int,input().split()))
pack = [0] + pack
dp = [0,pack[1]]
for i in range(2,N+1):
    x = []
    for j in range(1,i):
        if i%j==0:
            x.append(dp[j]*(i//j))
    dp.append(max([pack[i], max(x), pack[i-1]+pack[1]]))
print(dp[-1])
