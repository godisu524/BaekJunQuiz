S=input()
result=""
for a in range(ord('a'),ord('z')+1):
    if chr(a) in S:
        result+=" "+str((S.index(chr(a))))

    else:
        result+=" -1"
print(result.strip())