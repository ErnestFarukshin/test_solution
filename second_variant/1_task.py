# Программа получает с клавиатуры строку — дату в формате ДД.ММ.
# а) Проверьте корректность. Если нарушений несколько — выведите все,
# каждое с новой строки, ровно такими текстами
# б) Если дата корректна — выведите дату следующего дня
# (с ведущими нулями) и больше ничего.
# Справка: год невисокосный, високосность не учитывать.

DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31,
}

date = input()

errors = []

if len(date) < 5:
    errors.append("Строка меньше 5 вимволов")
elif len(date) > 5:
    errors.append("болше")

if errors:
    for error in errors:
        print(error)
else:
    dd = date[:2]
    mm = date[-2:]
    if not dd.isdigit():
        errors.append("Дни должны быть двумя цифрами")
    if date[2] != '.':
        errors.append("Дата должно быть записано в формате ДД:ММ")
    if not mm.isdigit():
        errors.append("Месяц должны быть двумя цифрами")
    if mm.isdigit() and not (1 <= int(mm) <= 12):
        errors.append("Месяц от 1 до 12")
    if mm.isdigit() and (1 <= int(mm) <= 12):
        if not (1 <= int(dd) <= DAYS_IN_MONTH[int(mm)]):
            errors.append(f"В месяце {int(mm)} нет дня {int(dd)}")
if errors:
    for error in errors:
        print(error)
else:
    dd = int(date[:2])
    mm = int(date[-2:])
    max_dey = DAYS_IN_MONTH[mm]
    if dd < max_dey:
        next_day = dd + 1
        next_month = mm
    else:
        if mm < 12:
            next_day = 1
            next_month = mm + 1
        else:
            next_day = 1
            next_month = 1


    if next_month < 10:
        next_month_str = '0' + str(next_month)
    else:
        next_month_str = str(next_month)

    if next_day < 10:
        next_day_str = '0' + str(next_day)
    else:
        next_day_str = str(next_day)

    print(f"{next_day_str}.{next_month_str}")