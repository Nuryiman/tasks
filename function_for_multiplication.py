def calculate_numbers_multiplication(*numbers):
    i = 1
    for item in numbers:
        i = item * i
    return i


print(calculate_numbers_multiplication(2, 3))
print(calculate_numbers_multiplication(2, 3, 2))
print(calculate_numbers_multiplication(2, 3, 2, 2))
