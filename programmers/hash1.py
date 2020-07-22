import collections
players={}




def solution(participant, completion):
    answer = ''
    for a in completion:
        try:
            players[a]+=1
        except:
            players[a]=1
    for a in participant:
        try:
            if players[a] >0:
                players[a]-=1
            else:
                answer=a
                break
        except:
            answer=a
            break
    
    return answer
def solution2(participant, completion):
    answer = collections.Counter(participant)- collections.Counter(completion)
    return list(answer.keys())[0]
print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))
print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))
