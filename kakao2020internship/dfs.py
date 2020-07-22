def dfs_recursive(board, cp,path,direction,money,returned=[],visited=[]):
    
    visited.append(cp.copy())
    path.append(cp.copy())
    
    print(path)
    print(money)

    #종료지점인지 확인 
    if cp == [len(board)-1,len(board)-1]:
        return money
    #dfs 이므로 아래내려가기부터시작
    #세로 방향이였으면 세로먼저 체크
    if direction == "vertical" :
        #아래 갈 수 있을떄
        if cp[0]+1 <len(board[0]) and board[cp[0]+1][cp[1]] != 1 and [cp[0]+1,cp[1]] not in visited:
            cp[0] +=1
            money+=100
            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
        #위로가기
        elif cp[0]-1 < len(board[0]) and cp[0]-1 >=0  and board[cp[0]-1][cp[1]] != 1 and [cp[0]-1,cp[1]] not in visited:

            cp[0] -=1
            money+=100
            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
        # 오른쪽으로 갈 수 있을떄
        elif cp[1]+1< len(board[0]) and board[cp[0]][cp[1]+1] !=1 and [cp[0],cp[1]+1] not in visited:

            cp[1] +=1
            direction = "horizontal"
            money+=600
            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
        
        #오른쪽 아래 왼쪽 다없을떄 위로 돌아갈때
        elif cp[0]-1 >=0 and board[cp[0]-1][cp[1]]!=1 and [cp[0]-1,cp[1]] not in returned :

            if [cp[0]-1,cp[1]] in path:
                
                while [cp[0]-1,cp[1]]  in path: # 돌아가려는 지점이 나올때까지 진행한 지점에서 없앤다.
                    path.pop()
            cp[0] -=1
            money-=100
            returned.append([cp[0],cp[1]])
            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
         
        #오른쪽 아래 둘다 없을때 왼쪽으로 돌아가야할때
        elif cp[1]-1 >=0 and board[cp[0]][cp[1]-1] != 1 and [cp[0],cp[1]-1] not in returned and [cp[0],cp[1]-1] in visited :

            if [cp[0],cp[1]-1] in path:
                while [cp[0],cp[1]-1]  in path:
                    path.pop()
            cp[1] -=1
            money-=600
            direction = "vertical"
            returned.append([cp[0],cp[1]])
            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
        #오른쪽 아래 둘다 없을때 오른쪽으로 돌아가야할때
        elif cp[1]+1 >=0 and board[cp[0]][cp[1]+1] != 1 and [cp[0],cp[1]+1] not in returned :
           
            if [cp[0],cp[1]+1] in path:
                while [cp[0],cp[1]+1]  in path:
                    path.pop()
            
            cp[1] +=1
            money-=600
            direction = "vertical"
            returned.append([cp[0],cp[1]])

            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
        #안가본곳이 위 왼쪽 오른쪽 아래 다없을떄 아래로 돌아가기(왼쪽돌아가려하는데 벽일때)
        
        elif cp[0]+1< len(board[0]) and board[cp[0]+1][cp[1]]!=1 and [cp[0]+1,cp[1]] not in returned:
            if [cp[0]+1,cp[1]] in path:
                while [cp[0]+1,cp[1]]  in path:
                    path.pop()
            cp[0] +=1
            money-=600
            direction = "vertical"
            returned.append([cp[0],cp[1]])
            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
    #가로 방향이였으면 가로먼저 체크
    elif direction == "horizontal" :
         #오른쪽 왼쪽 둘다 못갈때 아래로가기
        if cp[0]+1 <len(board[0]) and board[cp[0]+1][cp[1]] != 1 and [cp[0]+1,cp[1]] not in visited:

            cp[0] +=1
            direction = "vertical"
            money+=600
            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
        #오른쪽 갈 수 있을때(가본적없고)
        elif cp[1]+1< len(board[0]) and board[cp[0]][cp[1]+1] !=1 and [cp[0],cp[1]+1] not in visited:
            cp[1] +=1
            money+=100
            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
        #왼쪽 갈 수 있을때(가본적없고)
        elif cp[1]-1 >=0 and board[cp[0]][cp[1]-1] != 1 and [cp[0],cp[1]-1] not in visited :

            cp[1] -=1
            money+=100
            direction= "vertical"
            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
        
       
        #위로가기
        elif cp[0]-1 < len(board[0]) and cp[0]-1 >=0  and board[cp[0]-1][cp[1]] != 1 and [cp[0]-1,cp[1]] not in visited:

            cp[0] -=1
            money+=600
            direction=="vertical"
            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
        #오른쪽 왼쪽 아래쪽 다 가봤고 못갈때 왼쪽으로 돌아가기
        elif cp[1]-1 >=0 and board[cp[0]][cp[1]-1] != 1 and [cp[0],cp[1]-1] not in returned :
            if [cp[0],cp[1]-1] in path:
                while [cp[0],cp[1]-1]  in path:
                    path.pop()
            cp[1] -=1
            money-=100
            returned.append([cp[0],cp[1]])
            direction = "horizontal"
            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
        #오른쪽 왼쪽 아래쪽 다 가봤고 못갈때 오른쪽으로 돌아가기
        elif cp[1]+1 >=0 and board[cp[0]][cp[1]+1] != 1 and [cp[0],cp[1]+1] not in returned:
            if [cp[0],cp[1]+1] in path:
                while [cp[0],cp[1]+1]  in path:
                    path.pop()
            cp[1] +=1
            money-=100
            returned.append([cp[0],cp[1]])
            direction = "horizontal"
            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
        #오른쪽 왼쪽 아래쪽 다 가봤고 못갈때 위쪽으로 돌아가기
        
        elif cp[0]-1 >=0 and board[cp[0]-1][cp[1]]!=1 and [cp[0]-1,cp[1]] not in returned :
            if [cp[0]-1,cp[1]] in visited:
                while [cp[0]-1,cp[1]]  in path:
                    path.pop()
            cp[0] -=1
            direction = "vertical"
            returned.append([cp[0],cp[1]])
            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
         #안가본곳이 왼쪽오른쪽아래 다없을떄 아래로 돌아가기(왼쪽돌아가려하는데 벽일때)
        
        elif cp[0]+1< len(board[0]) and board[cp[0]+1][cp[1]]!=1 and [cp[0]+1,cp[1]] not in returned :
            if [cp[0]+1,cp[1]] in path:
                while [cp[0]+1,cp[1]]  in path:
                    path.pop()
            cp[0] +=1
            money-=600
            returned.append([cp[0],cp[1]])
            direction = "horizontal"
            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
        
    return money


def bfs_recursive(board, cp,path,direction,money,returned=[],visited=[]):
    #벽끝인지 확인
    visited.append(cp.copy())
    path.append(cp.copy())
    print(path)
    print(money)
    if path[-1] == [len(board)-1,len(board)-1]:
        return money

    
    
    #가로 방향이였으면 세로먼저 체크
    if direction == "horizontal" :
        #오른쪽 갈수 있을때(간적없고)
        if cp[1]+1< len(board[0]) and board[cp[0]][cp[1]+1] !=1 and [cp[0],cp[1]+1] not in visited:
            cp[1] +=1
            money+=100
            money = bfs_recursive(board,cp,path,direction, money, visited)
       
        
        #양쪽다 가봤을때 아래 체크
        elif cp[0]+1 <len(board[0]) and board[cp[0]+1][cp[1]] != 1 and [cp[0]+1,cp[1]] not in visited:
            cp[0] +=1

            direction = "vertical"
            money+=600
            money = bfs_recursive(board,cp,path,direction, money, visited)
        
        #왼쪽 갈수 있을때(간적없고)
        elif cp[1]-1 >=0 and board[cp[0]][cp[1]-1] != 1 and [cp[0],cp[1]-1] not in visited :
            cp[1] -=1

            money+=100
            money = bfs_recursive(board,cp,path,direction, money, visited)
        #위로 갈 수 있을때(가본적없고)
        elif cp[0]-1 < len(board[0]) and cp[0]-1 >=0  and board[cp[0]-1][cp[1]] != 1 and [cp[0]-1,cp[1]] not in visited:
            cp[0] -=1
            money+=600
            direction= 'vertical'
            money = bfs_recursive(board,cp,path,direction, money, visited)
        #안가본곳이 왼쪽오른쪽아래 다없을떄 왼쪽으로 돌아가기
        elif cp[1]-1 >=0 and board[cp[0]][cp[1]-1] != 1 and [cp[0],cp[1]-1] not in returned:
            if [cp[0],cp[1]-1] in path:
                while [cp[0],cp[1]-1]  in path:
                    path.pop()
            cp[1] -=1
            money-=100
            returned.append([cp[0],cp[1]])
            money = bfs_recursive(board,cp,path,direction, money, visited)
        #안가본곳이 왼쪽오른쪽아래 다없을떄 오른쪽으로 돌아가기(위나 왼쪽돌아가려하는데 벽일때)
        elif cp[1]+1 <len(board) and board[cp[0]][cp[1]+1] != 1 and [cp[0],cp[1]+1] not in returned:
            if [cp[0],cp[1]+1] in path:
                while [cp[0],cp[1]+1]  in path:
                    path.pop()
            cp[1] +=1
            money-=100
            direction = "horizontal"
            returned.append([cp[0],cp[1]])
            money = dfs_recursive(board,cp,path,direction, money,returned, visited)
        #안가본곳이 왼쪽오른쪽아래 다없을떄 위로 돌아가기(왼쪽돌아가려하는데 벽일때)
        elif cp[0]-1 >=0 and board[cp[0]-1][cp[1]]!=1 and [cp[0]-1,cp[1]] not in returned :

            if [cp[0]-1,cp[1]] in visited:
                while [cp[0]-1,cp[1]]  in path:
                    path.pop()
            cp[0] -=1
            money-=600
            direction = "vertical"
            returned.append([cp[0],cp[1]])
            money = bfs_recursive(board,cp,path,direction, money, visited)
       
        #안가본곳이 왼쪽오른쪽아래 다없을떄 아래로 돌아가기(왼쪽돌아가려하는데 벽일때)
        
        elif cp[0]+1< len(board[0]) and board[cp[0]+1][cp[1]]!=1 and [cp[0]+1,cp[1]] not in returned:
            if [cp[0]+1,cp[1]] in visited:
                while [cp[0]+1,cp[1]]  in path:
                    path.pop()
            cp[0] +=1
            money-=600
            direction = "vertical"
            returned.append([cp[0],cp[1]])
            money = bfs_recursive(board,cp,path,direction, money, visited)
    #가던방향이 수직일때 세로방향 먼저체크
    elif direction == "vertical" :
        #오른쪽으로 갈 수 있을때(가본적없고)
        if cp[1]+1< len(board[0]) and board[cp[0]][cp[1]+1] !=1 and [cp[0],cp[1]+1] not in visited:
            cp[1] +=1

            direction = "horizontal"
            money+=600
            money = bfs_recursive(board,cp,path,direction, money, visited)
        #아래로 갈수 있을때 (가본적없고)
        
        elif cp[0]+1 <len(board[0]) and board[cp[0]+1][cp[1]] != 1 and [cp[0]+1,cp[1]] not in visited:
            cp[0] +=1
            money+=100
            money = bfs_recursive(board,cp,path,direction, money, visited)
        #위로 갈 수 있을때(가본적없고)
        elif cp[0]-1 < len(board[0]) and cp[0]-1 >=0  and board[cp[0]-1][cp[1]] != 1 and [cp[0]-1,cp[1]] not in visited:
            cp[0] -=1
            money+=100
            money = bfs_recursive(board,cp,path,direction, money, visited)
        
        #왼쪽으로 갈 수 있을때(가본적없고)
        elif cp[1]-1< len(board[0]) and cp[1]-1 >=0 and board[cp[0]][cp[1]-1] !=1 and [cp[0],cp[1]-1] not in visited:
            cp[1] -=1
            direction = "horizontal"
            money+=600
            money = bfs_recursive(board,cp,path,direction, money, visited)
        
        
        #아래 오른쪽 왼쪽 다 못갈때 위로 다시 돌아가기
        elif cp[0]-1 >=0 and board[cp[0]-1][cp[1]]!=1 and [cp[0]-1,cp[1]] not in returned :
            if [cp[0]-1,cp[1]] in visited:
                while [cp[0]-1,cp[1]]  in path:
                    path.pop()
            cp[0] -=1
            money-=100
            returned.append([cp[0],cp[1]])
            money = bfs_recursive(board,cp,path,direction, money, visited)
        #안가본곳이 왼쪽오른쪽아래 다없을떄 아래로 돌아가기(왼쪽돌아가려하는데 벽일때)
        
        elif cp[0]+1< len(board[0]) and board[cp[0]+1][cp[1]]!=1 and [cp[0]+1,cp[1]] not in returned:
            if [cp[0]+1,cp[1]] in visited:
                while [cp[0]+1,cp[1]]  in path:
                    path.pop()
            cp[0] +=1
            direction = "horizontal"
            money-=600
            returned.append([cp[0],cp[1]])
            money = bfs_recursive(board,cp,path,direction, money, visited)
        #아래 오른쪽 다 못 갈때 왼쪽으로 돌아가기
        elif cp[1]-1 >=0 and board[cp[0]][cp[1]-1] != 1  and [cp[0],cp[1]-1] not in returned:
            if [cp[0],cp[1]-1] in path:
                while [cp[0],cp[1]-1]  in path:
                    path.pop()
            cp[1] -=1
            money-=600
            direction = "horizontal"
            returned.append([cp[0],cp[1]])
            money = bfs_recursive(board,cp,path,direction, money, visited)
        #안가본곳이 왼쪽오른쪽아래 다없을떄 오른쪽으로 돌아가기(위나 왼쪽돌아가려하는데 벽일때)
        elif cp[1]+1 <len(board) and board[cp[0]][cp[1]+1] != 1 and [cp[0],cp[1]+1] not in returned:
            if [cp[0],cp[1]+1] in path:
                while [cp[0],cp[1]+1]  in path:
                    path.pop()
            cp[1] +=1
            money-=100
            direction = "horizontal"
            returned.append([cp[0],cp[1]])
            money = bfs_recursive(board,cp,path,direction, money, visited)
    return money

            


        
    


def solution(board):
    money=0
    
    
    dfs_cost = (dfs_recursive(board,[0,0],[],'vertical',money)) 
    bfs_cost =(bfs_recursive(board,[0,0],[],'horizontal',money))
    return min(dfs_cost,bfs_cost)
    
    

    
print(solution([[0,0,0,0],
                [0,0,0,0],
                [0,1,0,1],
                [1,0,0,0]]))

    
print(solution([[0,0,0,0],
                [0,0,0,0],
                [0,1,0,1],
                [1,0,0,0]]))



