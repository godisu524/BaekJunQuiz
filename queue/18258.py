import sys
input=sys.stdin.readline
#sys.stdin.readline 이게 속도의 주범
queue=[]
def push(num):
    queue.append(num)


def pop():
    if len(queue)==0:
        print(-1)
    else:
        print(queue[0])
        queue.pop(0)
        

def size():
    print(len(queue))

def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def back():
    if len(queue)==0:
        print(-1)
    else:
        print(queue[-1])


def front():
    if len(queue)==0:
        print(-1)
    else:
        print(queue[0])
for _ in range(int(input().strip())):
    todo=input().strip()
    if 'push' in todo:    
        n,m=map(str,todo.split())
    else:
        n= todo
    if n == 'push':
        push(int(m))
    elif n == 'pop':
        pop()
    elif n == 'size':
        size()
    elif n == 'front':
        front()
    elif n == 'back':
        back()    
    elif n == 'empty':
        empty()
    else:
        print(todo)
