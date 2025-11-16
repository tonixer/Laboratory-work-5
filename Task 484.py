n = int(input())

matrix = [[0] * n for _ in range(n)]

current_num = 1
top = 0
bottom = n - 1
left = 0
right = n - 1

while left <= right and top <= bottom:

    for i in range(left, right + 1):
        matrix[top][i] = current_num
        current_num += 1
    top += 1

    for i in range(top, bottom + 1):
        matrix[i][right] = current_num
        current_num += 1
    right -= 1


    if top <= bottom:
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = current_num
            current_num += 1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = current_num
            current_num += 1
        left += 1

for row in matrix:
    row_str = [str(num) for num in row]
    print(" ".join(row_str))