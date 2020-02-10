n=int(input())
count=0
for a in range(pow(2,n)):
    tile=str(bin(a)).replace('0b','')
    if len(tile) < n:
        while(len(tile)<n):
            tile='0'+tile

    if '000' not in tile:
        if '101' not in tile:
            if not (tile.endswith('10')):
                if not (tile.startswith('01')):
                    count+=1
#0000
print(count+1)