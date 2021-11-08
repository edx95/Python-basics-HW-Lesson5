# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('1234_hw5.4.txt', encoding='utf-8') as f:
    numbers = f.readlines()
    new_file = []
    for number in numbers:
        if number.split()[0] == 'One':
            new_file.append(number.replace('One', 'Один'))
        elif number.split()[0] == 'Two':
            new_file.append(number.replace('Two', 'Два'))
        elif number.split()[0] == 'Three':
            new_file.append(number.replace('Three', 'Три'))
        else:
            new_file.append(number.replace('Four', 'Четыре'))

with open('1234_hw5.4_ru.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_file)