inp_str = input()
inp_splitted = inp_str.split(' ')
list = [int(x) for x in inp_splitted]

min_num = min(list)
max_num = max(list)
min_num_pos = -1
max_num_pos = -1
temp = -1

for number in range(0, len(list)):
    if list[number] == min_num:
        min_num_pos = number
    elif list[number] == max_num:
        max_num_pos = number
    else:
        continue

temp = list[min_num_pos]
list[min_num_pos] = list[max_num_pos]
list[max_num_pos] = temp

out = str()
for number in list:
    out += (str(number) + ' ')

print(out)