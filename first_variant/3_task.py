# # Дан список пар «студент — оценка за работу» (один студент встречается несколько
# # раз, оценки целые от 2 до 5):
# # grades = [("Аня" , 5), ("Борис", 5), ("Аня", 4), ("Гоша", 4), ("Аня", 2)
# # ("Борис", 3), ("Вика", 5)]
# # Выведите:
# # 1. Для каждого студента в алфавитном порядке — средний балл.
# # 2. Лучшего студента по среднему баллу; если таких несколько — того, кто раньше
# # по алфавиту.

grades = [("Аня" , 5), ("Борис", 5), ("Аня", 4), ("Гоша", 4), ("Аня", 2), ("Борис", 3), ("Вика", 5)]

marks = {}
for name, grade in grades:
    if name not in marks:
        marks[name] = []
    marks[name].append(grade)

for name in sorted(marks):
    avg = sum(marks[name]) / len(marks[name])
    print(f'{name}: {avg}')

best_name = ''
best_avg = -1

for name in sorted(marks):
    avg = sum(marks[name]) / len(marks[name])
    if avg > best_avg:
        best_avg = avg
        best_name = name
print(f'Лучший {best_name}: {best_avg}')
