# Дано натуральное число N. Напишите функцию int NumberOfZeroes(int n) (C/C++/Java), function NumberOfZeroes(n: longint): integer (Pascal), определяющую количество нулей среди всех цифр числа N.

input_int = str(int(input()))

def NumberOfZeroes(n):
    counter = 0
    for number in n:
        if number == '0':
            counter += 1
    print(counter)

NumberOfZeroes(input_int)