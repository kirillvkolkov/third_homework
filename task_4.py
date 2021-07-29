# Дано натуральное число N. Напишите функцию int MinDigit (int n) (C/C++), function MinDigit (n:longint):integer (Pascal) и int MaxDigit (int n) (C/C++), function MaxDigit (n:longint):integer (Pascal), определяющую наименьшую и наибольшую цифры данного числа.

input_int = input()

def space_remover(x):
    return x.split(' ')

def filtered(x):
    filtered_list = []
    for i in x:
        if not i.startswith('-') and not i == '0':
            if int(i) <= 1000:
                filtered_list.append(int(i))

    return filtered_list


def MinDigit(x):
    lowest_number = x[0]
    for number in x:
        if number < lowest_number:
            lowest_number = number
    return str(lowest_number)


print(MinDigit(filtered(space_remover(input_int))))