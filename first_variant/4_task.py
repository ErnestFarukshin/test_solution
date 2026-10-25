"""
Дан словарь с прайсом покупок и список продуктов которые требуется купить:
prices = {"хлеб": 50, "молоко": 90, "сыр": 400, "кофе": 600}
order = ["хлеб", "сыр", "хлеб", "чай", "молоко", "молоко", "кофе"]
Требуется вывести список вида продукт – требуемое количество, вывести список продуктов которых нет
в прайсе, вывести итоговую сумму закупки (продукты которых нет в прайсе - 0), в конце вывести самый
часто встречающийся продукт.
Ожидаемый вывод:
хлеб — 3
сыр — 2
чай — 1
молоко — 2
кофе — 1
Нет в прайсе: ['чай']
Итого: 1730
Чаще всего: хлеб (3 шт.)
"""

prices = {"хлеб": 50, "молоко": 90, "сыр": 400, "кофе": 600}
order = ["хлеб", "сыр", "хлеб", "чай", "молоко", "молоко", "кофе"]

counts = {}
for item in order:
    if item not in counts:
        counts[item]= 1
    else:
        counts[item] += 1

for item, cnt in counts.items():
    print(f"{item} - {cnt}")

missing = []
for item in counts:
    if item not in prices:
        prices[item] = 0
        missing.append(item)

print(f"Нет в прайсе: {missing}")

total = 0
for item, cnt in counts.items():
    total += prices[item] * cnt
print(f"Итого {total}")

max_item = sorted(counts.items(), key=lambda x: x[1], reverse=True)[0]
print(f"Чаще всего: {max_item[0]} {max_item[1]} штук")