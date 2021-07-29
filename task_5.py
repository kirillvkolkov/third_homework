# Дано натуральное число N. Напишите функцию int MinDigit (int n) (C/C++), function MinDigit (n:longint):integer (Pascal) и int MaxDigit (int n) (C/C++), function MaxDigit (n:longint):integer (Pascal), определяющую наименьшую и наибольшую цифры данного числа.

input_str = str()
finish_input = True

while finish_input == True:
    input_value = input()
    if input_value == '0':
        finish_input = False
    else:
        input_str += input_value
