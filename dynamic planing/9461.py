nums=[1,1,1,2,2]
tests=[]
i=int(input())
for _ in range(i):
    tests.append(int(input()))

for n in tests:
    if n<=3:
        print(1)
    else:
        for a in range(len(nums)-1,n+1):
            nums.append(nums[a]+nums[a-1]-nums[a-3])
        print(nums[n-1])

