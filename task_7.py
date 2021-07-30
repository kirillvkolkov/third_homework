inp_str = input()

list = [int(x) for x in inp_str if x != ' ']
counter = 0
for number in range(1, len(list) - 1):

    if list[number] > list[number - 1] and list[number] > list[number + 1]:
        counter += 1

print(counter)


