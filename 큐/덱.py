import sys

n = int(sys.stdin.readline())
deque = []
for _ in range(n):
    command = sys.stdin.readline()[:-1]

    if "push_front" in command:
        deque.insert(0,command.split(' ')[1])

    elif "push_back" in command:
        deque.append(command.split(' ')[1])

    elif "pop_front" in command:
        if len(deque)==0:
            print(-1)
            continue
        print(deque.pop(0))

    elif "pop_back" in command:
        if len(deque)==0:
            print(-1)
            continue
        print(deque.pop(-1))

    elif "size" in command:
        print(len(deque))

    elif "empty" in command:
        print(0 if len(deque) else 1)

    elif "front" in command:
        if len(deque)==0:
            print(-1)
            continue
        print(deque[0])
    elif "back" in command:
        if len(deque)==0:
            print(-1)
            continue
        print(deque[-1])
