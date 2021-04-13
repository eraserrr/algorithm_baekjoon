```
def comb(consulting, selected, arr, s, e, pay, x):
    for i in range(s, e):
        consulting -= 1
        # print('진행상황', selected,'남은 상담', consulting,'금액', pay)
        # 가능한지 보기
        if e-i >= arr[i][0] and consulting<=0:
            selected[i] = True
            comb(arr[i][0],selected, arr, i+1, e, pay+arr[i][1],x)
            selected[i] = False

    # 종료 조건 : 뽑을 게 더이상 없다 , 끝까지 감
    # print(selected, '의 조합', pay)
    x.append(pay)
    return max(x)

N = int(input())
calendar = []
for _ in range(N):
    a = input().split()
    calendar.append([int(a[0]), int(a[1])])

selected = [False] * N

print(comb(0, selected, calendar, 0, N, 0, []))
```


<br>
아래는 내가 푼건 아니지만 좋은 코드!
```
n = int(input())
plan = []
benefit = []
for i in range(n):
    plan.append(tuple(map(int,input().split())))
    benefit.append(-1)
benefit.append(0)

if plan[n-1][0] == 1:
    benefit[n-1] = plan[n-1][1]
else:
    benefit[n-1] = 0
    
for i in range(n-2,-1,-1):
    benefit[i] = benefit[i+1]
    if i + plan[i][0] - 1 < n: #선택할 수 있는 경우
        t = plan[i][1] + benefit[i+plan[i][0]]
        if benefit[i] < t:
            benefit[i] = t

print(benefit[0])
```

benefit 의 i번째의 값은 뒤에서부터 i 를 선택했을때 가장 최대가 되는 값이다


i 번째를 선택하지 않은 경우와 (benefit[i+1] 과 같겠다)


i 번째를 선택한 경우 (i 번째에서의 상담금액과 i 번째의 상담일자를 건너뛴 날짜에서의 benefit 값을 더함)


중 최대인 값이 그 값이다.
