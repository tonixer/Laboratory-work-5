START_CODE = int("1F600", 16)
END_CODE = int("1F64F", 16)
ALPHABET_SIZE = (END_CODE - START_CODE) + 1

try:
    shift = int(input())
    text = input()
except ValueError:
    print("Помилка: зсув має бути цілим числом.")
    exit()

encrypted_result = []

for char in text:
    code = ord(char)

    if START_CODE <= code <= END_CODE:
        current_index = code - START_CODE
        new_index = (current_index + shift) % ALPHABET_SIZE
        new_code = new_index + START_CODE
        encrypted_result.append(chr(new_code))
    else:
        encrypted_result.append(char)

print("".join(encrypted_result))