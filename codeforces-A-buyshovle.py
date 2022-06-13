

num_inputs = input()

counter = 1
base = 0
change = 0

temp = num_inputs.split(' ')
base = int(temp[0])
money = base
change = int(temp[1])

while True:
    if money % 10 == 0 or money % 10 == change :
        break
    counter += 1
    money += base
print(counter)
