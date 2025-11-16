numbers = [1, 2, 2, 3, 2, 3, 4]
counts = {}
pairs = 0

for number in numbers:
    if number in counts:
        pairs += counts[number]
        print(number)
        counts[number] += 1
    else:
        counts[number] = 1

print(pairs)

