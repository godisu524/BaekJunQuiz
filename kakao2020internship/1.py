def solution(numbers, hand):
    answer = ''
    phone = [[1,2,3],[4,5,6],[7,8,9],[11,0,12]]
    last_used_L = 11
    last_used_R = 12
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            last_used_L = i
        elif i in [3,6,9]:
            answer +='R'
            last_used_R = i

#[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
        else:
            for n,a in enumerate(phone):
                for m,b in enumerate(a):
                    if b == last_used_L:
                        L_pos = [m,n]
                    if b == last_used_R:
                        R_pos = [m,n]
                    if b == i:
                        C_pos = [m,n]
            print(L_pos, R_pos, C_pos)
            if (abs(C_pos[0] - L_pos[0]) + abs(C_pos[1] - L_pos[1]))<(abs(C_pos[0] - R_pos[0]) + abs(C_pos[1] - R_pos[1])) :
                answer += "L"
                last_used_L = i
            elif (abs(C_pos[0] - L_pos[0]) + abs(C_pos[1] - L_pos[1]))>(abs(C_pos[0] - R_pos[0]) + abs(C_pos[1] - R_pos[1])) :
                answer += "R"
                last_used_R = i
            else :
                if hand == 'right':
                    answer += "R"
                    last_used_R = i
                else :
                    answer += "L"
                    last_used_L = i




    return answer






print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))