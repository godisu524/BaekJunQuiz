def solution(phone_book):
    answer = True
    for n,a in enumerate(phone_book):
        a = a.replace(" ","")
        phone_book[n]=a

    for n,a in enumerate(phone_book):
        for m,b in enumerate(phone_book):
            if n!=m:
                if a in b[:len(a)]:
                    answer = False
                    print(a,b)
                    return answer

    return answer

print(solution(["119", "97674223", "11 9 5 524421"]))
print(solution(["123", "456", "789"]))


