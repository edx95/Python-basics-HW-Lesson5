# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.


import json

companies = {}

with open("HW_5.7.txt") as f_obj:
    while True:
        line = f_obj.readline()
        if not line:
            break
        rows = line.split()
        name = rows[0]
        plus = float(rows[2])
        minus = float(rows[3])
        profit = round(plus - minus, 2)
        companies[name] = profit

average_profit = str(round(sum(companies.values()) / len(companies), 2))
print("Средняя прибыль:", average_profit)

write_data = (companies, {"average_profit": average_profit})

with open("HW_5.7.json", 'w', encoding='utf8') as f_obj:
    f_obj.write(str(write_data))