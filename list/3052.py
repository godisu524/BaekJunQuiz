num_list=[]
for a in range(10):
    num_list.append(int(input()))
diff_count=0
diff_last=[]
for a in num_list:
    if a %42 not in diff_last:
        diff_last.append(a%42)
print(len(diff_last))
