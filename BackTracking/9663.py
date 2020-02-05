n, ans = int(input()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)
            #세로       #/ 방향 대각선      #\ 방향 대각선

def solve(i):
    global ans
    if i == n:
        print(i,ans)
        ans += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] =True 
            print("i",i)
            print("j",j)
            a[j]="TRUE111"
            b[i+j]="TRUE111"
            c[i-j+n-1]="TRUE111"
            print(a)
            print(b)
            print(c)
            a[j]=True
            b[i+j]=True
            c[i-j+n-1]=True
            solve(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

solve(0)
print(ans)


