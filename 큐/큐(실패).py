n = int(input())
s = ''
queue = []
length = 0
for _ in range(n):
    command = input()
    if command.find('push')==0:
        queue.append(command.split(' ')[1])
        length += 1
        continue
    if command.find('pop')==0:
        if length==0:
            s += '-1\n'
            continue
        s += str(queue[0]) + '\n'
        queue = queue[1:]
        length -= 1
        continue
    if command.find('size')==0:
        s += str(length) + '\n'
        continue
    if command.find('empty')==0:
        if length==0:
            s += '1\n'
            continue
        s += '0\n'
        continue
    if command.find('front')==0:
        if length==0:
            s += '-1\n'
            continue
        s += queue[0] + '\n'
        continue
    if command.find('back')==0:
        if length==0:
            s += '-1\n'
            continue
        s += queue[-1] + '\n'

print(s)
