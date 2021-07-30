finish_input = True

count = 1
num = '0'
max_counter = 0
num_to_compare = str()

while finish_input == True:
    input_value = input()
    if input_value == '0':
        if count > max_counter:
            max_counter = count
        finish_input = False
    else:
        if input_value == num:
            num = input_value
            count += 1
        else:
            if count > max_counter:
                num_to_compare = num
                max_counter = count
                num = input_value
                count = 1
            else:
                num = input_value
                count = 1

print(max_counter)
