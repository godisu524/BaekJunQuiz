from itertools import permutations
#eval 사용하기
#("100-200*300-500+20")
def my_expression(expression) :
    answers=[]
    #1 * > + > -
    m_temp = expression.split("-")
    for n,a in enumerate(m_temp):
        p_temp = a.split("+")
        for m,b in enumerate(p_temp):
            p_temp[m]= str(eval(b))
        m_temp[n] = str(eval("+".join(p_temp)))
    m_late = (eval("-".join(m_temp)))
    answers.append(abs(m_late))

    #2 * > - > +
    m_temp = expression.split("+")
    for n,a in enumerate(m_temp):
        p_temp = a.split("-")
        for m,b in enumerate(p_temp):
            p_temp[m]= str(eval(b))
        m_temp[n] = str(eval("-".join(p_temp)))
    m_late = (eval("+".join(m_temp)))
    answers.append(abs(m_late))
    

    #3 + > * > -
    m_temp = expression.split("-")
    for n,a in enumerate(m_temp):
        p_temp = a.split("*")
        for m,b in enumerate(p_temp):
            p_temp[m]= str(eval(b))
        m_temp[n] = str(eval("*".join(p_temp)))
    m_late = (eval("-".join(m_temp)))
    answers.append(abs(m_late))

    #4 +> - > *
    m_temp = expression.split("*")
    for n,a in enumerate(m_temp):
        p_temp = a.split("-")
        for m,b in enumerate(p_temp):
            p_temp[m]= str(eval(b))
        m_temp[n] = str(eval("-".join(p_temp)))
    m_late = (eval("*".join(m_temp)))
    answers.append(abs(m_late))

    #5  -> * > +
    m_temp = expression.split("+")
    for n,a in enumerate(m_temp):
        p_temp = a.split("*")
        for m,b in enumerate(p_temp):
            p_temp[m]= str(eval(b))
        m_temp[n] = str(eval("*".join(p_temp)))
    m_late = (eval("+".join(m_temp)))
    answers.append(abs(m_late))

    #5  -> * > +
    m_temp = expression.split("*")
    for n,a in enumerate(m_temp):
        p_temp = a.split("+")
        for m,b in enumerate(p_temp):
            p_temp[m]= str(eval(b))
        m_temp[n] = str(eval("+".join(p_temp)))
    m_late = (eval("*".join(m_temp)))
    answers.append(abs(m_late))




    return max(answers)
#   for a in expression:
#     if a == "-"
def solution(expression):
    answer = 0
    used_operater= []
    
    return my_expression(expression)
    
    

        


            



print(solution("100-200*300-500+20"))