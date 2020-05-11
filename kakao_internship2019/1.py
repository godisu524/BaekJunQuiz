from collections import deque
block = [[0,0,0,0,0]
,[0,0,1,0,3]
,[0,2,5,0,1]
,[4,2,4,4,2]
,[3,5,1,3,1]]



moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    moved_block = deque()
    answer = 0

    for a in moves:
        for b in board:
            if b[a-1] != 0:
                moved_block.append(b[a-1])
                while len(moved_block) > 1:
                    org_moved_block = moved_block.copy()
                    if moved_block[-1] == moved_block[-2]:
                        moved_block.pop()
                        moved_block.pop()
                        answer += 2
                    if org_moved_block == moved_block :
                        break
                b[a-1] = 0
                break
                    
           
        
    
 
    return answer
print(solution(block,moves))

