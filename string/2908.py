Number= input()
numa= Number.split(' ')[0]
numb= Number.split(' ')[1]

new_numa= numa[2]+numa[1]+numa[0]
new_numb= numb[2]+numb[1]+numb[0]

if new_numa>new_numb:
    print(new_numa)
else:
    print(new_numb)
