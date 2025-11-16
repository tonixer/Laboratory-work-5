numbers = [int(num) for num in input("Введіть числа через пробіл: ").split()]
counts = {}
pairs = 0

for number in numbers:
    if number in counts:
        pairs += counts[number]
        counts[number] += 1
    else:
        counts[number] = 1

print(pairs)

