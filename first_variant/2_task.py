# Дана сжатая строка в формате символ - число повторений данного
# символа, требуется восстановить исходную строку
# (Пример a3b2h5 – aaabbhhhhh). В итоговой строке могут
# быть любые символы, не являющиеся цифрами. Написанная программа должна
# принимать любую валидную строку, например a3b2h5, a3b22h5, a1f4.
# Строка ab10 не является валидной (т.к. после a нет количества
# повторений), требуется вывести ошибку.

compressed_str = input()

result = []
error = None
i = 0

if len(compressed_str) == 0:
    error = "The string is empty"

while i < len(compressed_str) and error is None:
    ch = compressed_str[i]
    if ch.isdigit():
        error = "Строка не может начинаться с числа"
    else:
        j = i + 1
        num = ""
        while j < len(compressed_str) and compressed_str[j].isdigit():
            num += compressed_str[j]
            j += 1
        if not num:
            error = "После символа должно идти число его повторений"
        else:
            result.append(int(num) * ch)
            i = j

if error:
    print(error)
else:
    print("".join(result))