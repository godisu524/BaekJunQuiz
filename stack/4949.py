import sys
input=sys.stdin.readline

while(True):
    answer='yes'
    string=input().replace('\n',"")
    temp=[]
    if string==".":
        break
    else:
        strings_first=[]
        strings_second=[]
        temp=[]
        for a in string:
            if a in ['(','[']:
                strings_first.append(a)
            elif a in [')',']']:
                strings_second.append(a)
        if len(strings_first) == len(strings_second):
            for a in string:
                if a in ['(','[']:
                    temp.append(a)
                elif a in [')',']']:
                    if len(temp)!=0:
                        if a == ')':
                            if temp[-1] == '(':
                                temp.pop(-1)
                            else:
                                answer="no"
                        elif a ==']':
                            if temp[-1] == '[':
                                temp.pop(-1)
                            else:
                                answer="no"
                    else:
                        answer='no'
        else:
            answer='no'
        print(answer)
                

