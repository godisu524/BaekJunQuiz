def mergeSort(x):
    print("ㅅㅣ작",x)
    if len(x) > 1:
        mid = len(x)//2
        lx, rx = x[:mid], x[mid:]
        print("재귀전lx",x,lx)
        print("재귀전rx",x,rx)
        mergeSort(lx)
        mergeSort(rx)
        print("재귀후lx",x,lx)
        print("재귀후rx",x,rx)

        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]
    
    print("끝",x)
    return x

mergesort_list = []
for i in range(int(input())):
    num_input = int(input())
    mergesort_list.append(num_input)

res = mergeSort(mergesort_list)

for j in res:
    print(j)