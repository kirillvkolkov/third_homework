inp_str = input()

left_h = inp_str.find('h') + 1
right_h = inp_str.rfind('h')

reversed_between_left_and_right = inp_str[left_h: right_h][::-1]

final_string = inp_str[:left_h] + reversed_between_left_and_right + inp_str[right_h:]


print(final_string)
