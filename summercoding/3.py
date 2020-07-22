def dfs(pos,edges,visited,answer):
    visited.append(pos)
    count=1
    
    for i in edges[pos]:
        if i in visited:
            continue
        else:
            count+= dfs(i,edges,visited,answer)
    answer[pos] = count
    return count


def solution(total_sp, skills):
    answer = [[] for i in range (total_sp)]
    edges = [[] for i in range(total_sp)]   
    numbers=[]
    used= []
    visited=[]
    root=0
    count=0
    for a in skills:
        
        edges[a[0]].append(a[1])
        if a[0] not in used:
            used.append(a[0])
        if a[1] not in used:
            used.append(a[1])
        if a[1] not in numbers:
            numbers.append(a[1])

    for a in used:
        if a not in numbers:
            root = a
            break
    
    sp_num = total_sp / (len(used)*2-1)
   
    count = dfs(root,edges,visited,answer)
   
    
    print(edges)
    for a in numbers:
        edges[a]
    real_answer=[]
    print(answer)
    for n,a in enumerate(answer):
        if type(a) == int:
            if n == root :
                a -= len(edges[n])
                real_answer.append(a*sp_num)
            elif a ==1 :
                real_answer.append(a*sp_num)
            else:
                continue




    return real_answer

print(solution(121,[[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]))