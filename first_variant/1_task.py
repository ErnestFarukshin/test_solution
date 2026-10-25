"""
Программа получает с клавиатуры строку — показание часов в формате ЧЧ:ММ.
а) Проверьте корректность введенного времени:
Если нарушений несколько — выведите все, каждое с новой строки.
б) Если время корректно — выведите показание часов через одну минуту (с ведущими
нулями) и больше ничего.
"""

time = input()

errors = []

if len(time) < 5:
    errors.append("Строка меньше 5 вимволов")
elif len(time) > 5:
    errors.append("Строка больше 5 символов")
else:
    hh = time[:2]
    mm = time[-2:]
    if not hh.isdigit():
        errors.append("Часы должны быть двумя цифрами")
    if time[2] != ':':
        errors.append("Время должно быть записано в формате ЧЧ:ММ")
    if not mm.isdigit():
        errors.append("Минуты должны быть двумя цифрами")
    if hh.isdigit():
        if not (0 <= int(hh) <= 23):
            errors.append("Часы от 0 до 23")
    if mm.isdigit() and not (0 <= int(mm) <= 59): # работает потому что and - ленивый
        errors.append("Минуты от 0 до 59")

if errors:
    for error in errors:
        print(error)
else:
    hh = int(time[:2])
    mm = int(time[-2:]) + 1

    if mm == 60:
        mm = 0
        hh += 1
        if hh == 24:
            hh = 0

    if hh < 10:
        hours = '0' + str(hh)
    else:
        hours = str(hh)

    if mm < 10:
        minutes = '0' + str(mm)
    else:
        minutes = str(mm)

    print(f"{hours}:{minutes}")