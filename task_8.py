inp_str = input()
inp_height = int(input())

inp_splitted = inp_str.split(' ')

list = sorted([int(x) for x in inp_splitted], reverse=True)


position = 0
for height in range(0, len(list) - 1):
    if list[height] < inp_height:
        list.insert(height, inp_height)
        position = height + 1
        break


print(position)