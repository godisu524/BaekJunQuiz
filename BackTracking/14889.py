from itertools import permutations as pm
from itertools import combinations as cm
n=int(input())
stats=[]

for a in range(n):
    stats.append(list(map(int,input().split())))
#workers=[i for i in range(n)]


mins=[]
#너무 오래걸리나봄
#for a in set(pm(workers,len(workers))):
for a in cm(range(n),n//2):
    team1_power=0
    team2_power=0
    for w1 in a:
        for w2 in a:
            team1_power+=stats[w1][w2]
    
    for w1 in set(range(n)) -set(a):
        for w2 in set(range(n)) -set(a):
            team2_power+=stats[w1][w2]
    mins.append(abs(team1_power-team2_power))
print(min(mins))