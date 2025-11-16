numbers = [int(num) for num in input("Введіть числа через пробіл: ").split()]
odd_numbers = set()

for number in numbers:
    if not number % 2 == 0:
        odd_numbers.add(number)

print(list(odd_numbers))
