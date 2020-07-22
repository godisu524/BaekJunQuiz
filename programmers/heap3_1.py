def solution(jobs):
    answer = 0
    tictoc = 0
    length = len(jobs)
    jobs.sort(key= lambda x: x[1]) #뒤에껄로 솔팅
    
    while len(jobs)!= 0:
        for i in range(len(jobs)):
            if jobs[i][0] <=tictoc:
                tictoc += jobs[i][1]
                answer += tictoc - jobs[i][0]
                jobs.pop(i)
                break
            if i ==len(jobs)-1:
                tictoc+=1
    




    return answer//length





print(solution([[0, 3], [1, 9], [2, 6]]))   
