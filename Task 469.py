numbers = [int(num) for num in input("Введіть числа через пробіл: ").split()]

reversed_numbers = numbers
reversed_numbers.reverse()

print("".join(str(num) for num in reversed_numbers))