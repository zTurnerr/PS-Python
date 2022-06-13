


num_inputs = input()
arr_inputs = []
counter = 0
for i in range(int(num_inputs)):
    temp_input = input()
    temp_input = temp_input.split(' ')
    arr_inputs.append(temp_input)

for i in range (len(arr_inputs)):
    for j in range(len(arr_inputs)):
        if i != j :
            if arr_inputs[i][0] == arr_inputs[j][1]:
                counter += 1


print(counter)