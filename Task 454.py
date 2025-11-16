numbers = [int(num) for num in input("Введіть числа через пробіл: ").split()]
odd_numbers = []

for number in numbers:
    if not number % 2 == 0:
        odd_numbers.append(number)

print(odd_numbers)
