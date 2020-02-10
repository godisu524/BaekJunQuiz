import sys

n=int(input())

answer=0
def fibonach(n1,n2,i):
    if i == n:
        print(n1)
        sys.exit(0)
    else :
        fibonach(n2,n1+n2,i+1)

fibonach(0,1,0)
        

