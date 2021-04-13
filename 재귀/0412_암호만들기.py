result= []

def comb(n, selected, arr, s, e):
    if n==0:
        x = ''
        for i in range(len(selected)):
            if selected[i]:
                x += arr[i]
        v = [a for a in x if a in 'aeiou']
        c = [a for a in x if a not in v]
        if len(v)>=1 and len(c)>=2:
            result.append(''.join(sorted(x)))

    for i in range(s, e):
        selected[i] = 1
        comb(n-1, selected, arr, i+1, e)
        selected[i] = 0

L = int(input().split(' ')[0])
C = input().split(' ')

selected = [0] * len(C)
comb(L, selected, C, 0, len(C))

result.sort()
for r in result:
    print(r)
