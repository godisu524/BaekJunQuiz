from itertools import cycle


def solution(answers):
    winner = []   
    pattern1=[1,2,3,4,5]
    pattern2=[2,1,2,3,2,4,2,5]
    pattern3=[3,3,1,1,2,2,4,4,5,5]

    score=[0,0,0]

    for a,b,c, answer in zip(cycle(pattern1),cycle(pattern2), cycle(pattern3),answers):
        if a == answer:
           score[0]+=1
        if b == answer:
            score[1]+=1
        if c == answer:
            score[2]+=1 
    
    for i,a in enumerate(score):
        if a == max(score):
            winner.append(i+1)
        #print(score)
    return winner
        
        
    

print(solution([1,3,2,4,2]))