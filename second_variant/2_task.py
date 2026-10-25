# Дана строка из строчных латинских букв и цифр:
# s = "a12bc345d6"
# Числом считается последовательность подряд идущих цифр (числа могут быть многозначными;
# ведущие нули в данных не встречаются). Выведите каждое число на отдельной строке, затем
# количество и сумму. Если цифр в строке нет вообще — выведите только Чисел нет.
# Ожидаемый вывод:
# 12
# 345
# 6
# Количество: 3
# Сумма: 363

input_string = input()
result = []
buf = ""

for ch in input_string:
    if ch.isdigit():
        buf += ch
    else:
        if buf != "":
            result.append(int(buf))
            buf = ""

if buf != "":
    result.append(int(buf))

if result:
    for n in result:
        print(n)
    print(f"Количество: {len(result)}")
    print(f"Сумма: {sum(result)}")
else:
    print("Чисел нет")


