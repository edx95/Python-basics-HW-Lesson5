# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('salary hw5.3.txt', encoding='utf-8') as f:
    text = f.readlines()
    total = 0
    for el in text:
        average = float((el.split()[1]))
        total = total + average
        if float(el.split()[1]) < 20000:
            print(el.split()[0], el.split()[1])
    print(f'Средняя величина дохода сотрудников: {total / len(text):.2f}')