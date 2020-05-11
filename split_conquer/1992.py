import sys
input=sys.stdin.readline

answer=""
def devide(x, y, t):
    global blue, white

    type = arr[y][x]
    flag = True
    for i in range(y, y+t):
        if not flag:
            break
        for j in range(x, x+t):
            if type != arr[i][j]:
                flag = False
                answer+="("
                devide(x, y, t//2)
                devide(x+t//2, y, t//2)
                devide(x, y+t//2, t//2)
                devide(x+t//2, y+t//2, t//2)
                answer+=")"
                break
    if flag:
        if type == 0:
            answer+= 0
        else:
            answer+= 0

N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
blue, white = 0, 0
devide(0, 0, N)
print(answer)