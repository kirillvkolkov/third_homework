seq = input()

modified_input = [int(x) for x in seq if x != ' ']

final_array = []
score = 0
for elem in modified_input:
    if elem not in final_array:
        final_array.append(elem)
    else:
        final_array.remove(elem)
        score += 1

print(score)