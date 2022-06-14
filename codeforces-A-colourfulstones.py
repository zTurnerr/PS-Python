

main = input()
step = input()

pos = 0

for i in range(len(step)):
    if step[i] == main[pos]:
        pos += 1
print(pos+1)