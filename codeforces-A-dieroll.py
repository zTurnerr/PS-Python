

rolls = input()

rolls = rolls.split(' ')

first = int(rolls[0])
second = int(rolls[1])
bigest = 0
pointer = 0
dies = [1,2,3,4,5,6]

if first>=second:
    bigest = first
else :
    bigest = second
for i in range(len(dies)):
    if dies[i] >= bigest:
        pointer = i
        break
base = 6 

pointer = 6 - pointer   

while True:
    if pointer % 2 == 0 and base % 2 == 0 :
        pointer = pointer / 2
        base = base / 2
    elif pointer % 3 == 0 and base % 3 == 0 :
        pointer = pointer / 3
        base = base / 3
    else :
        break
print(str(int(pointer))+'/'+str(int(base)))
