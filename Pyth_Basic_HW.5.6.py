# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
# учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.

# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

'''my_file = open("HW_5.6.txt", encoding='utf-8')
my_dict = {}

lines = my_file.readlines()

for line in lines:
    data = line.replace('(', ' ').split()
    my_dict[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())

print(my_dict)

my_file.close()'''

study_plan = {}
total_hours = []
with open('HW_5.6.txt', encoding='utf-8') as f:
    for line in (f.readlines()):
        hours = []
        study_plan[line.split()[0].strip(':')] = []
        new_number = ''
        for el in line:
            if el.isdigit():
                new_number = new_number + el
            if not el.isdigit() and new_number != '':
                hours.append(int(new_number))
                new_number = ''
        total = 0
        for hour in hours:
            total = total + hour
        total_hours.append(total)
        for num, key in enumerate(study_plan):
            study_plan[key] = (total_hours[num])
    print(study_plan)