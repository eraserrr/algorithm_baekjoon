# 앞서 풀었던 2*n 타일링에서와 다르게 n-2 + (2개의타일) 을 계산할때
# 정사각형 모양의 타일 계산이 하나 늘었으니까 n-2 계산할때 계산을 두배해주면 된다

n = int(input())
tile = [1,3]
for i in range(n):
    tile.append(tile[-1] + 2*tile[-2])

print(tile[n-1]%10007)
