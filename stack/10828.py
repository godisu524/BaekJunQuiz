import sys
input=sys.stdin.readline

stack=[]
def push(num):
    stack.append(num)


def pop():
    if len(stack)==0:
        print(-1)
    else:
        print(stack[-1])
        stack.pop(-1)

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack)==0:
        print(-1)
    else:
        print(stack[-1])

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
    elif n == 'top':
        top()
    elif n == 'empty':
        empty()
    else:
        print(todo)
