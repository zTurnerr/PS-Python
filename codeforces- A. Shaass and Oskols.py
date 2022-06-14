
wires_number =int( input())

birds =  input()

birds = birds.split(' ')

for i in range(len(birds))  :
    birds[i] = int(birds[i])

shots_num = input()
shots = []
for i in range(int(shots_num)):
    temp = input()
    temp = temp.split(' ')
    shots.append([int(temp[0]), int(temp[1])])


for i in range(len(shots)):
    wire_order = shots[i][0]
    order_from_left = shots[i][1]

    if wires_number == 1:
        birds[0] = 0
    elif wire_order == wires_number :
        birds[-2] += order_from_left-1
        birds[-1] = 0
    elif wire_order == 1 :
        birds[1] += (birds[0]-order_from_left)
        birds[0] = 0
    else:
        current = wire_order - 1
        birds[current-1] += order_from_left-1
        birds[current+1] += (birds[current]-order_from_left)
        birds[current] = 0

    # print(birds)

for i in birds :
    print(i)
