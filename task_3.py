# Дано натуральное число N. Напишите функцию int MinDigit (int n) (C/C++), function MinDigit (n:longint):integer (Pascal) и int MaxDigit (int n) (C/C++), function MaxDigit (n:longint):integer (Pascal), определяющую наименьшую и наибольшую цифры данного числа.

input_int = int(input())

def MinDigit(input_int):
    separate_input = [int(x) for x in list(str(input_int))]
    lowest_number = separate_input[0]
    for number in separate_input:
        if number < lowest_number:
            lowest_number = number
    return str(lowest_number)

def MaxDigit(input_int):
    separate_input = [int(x) for x in list(str(input_int))]
    highest_number = separate_input[0]
    for number in separate_input:
        if number > highest_number:
            highest_number = number
    return str(highest_number)

print(MinDigit(input_int) + ' ' + MaxDigit(input_int))