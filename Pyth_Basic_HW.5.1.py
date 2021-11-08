# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.



with open('hw5.1 testfile.txt', 'w', encoding='utf-8') as f:
    while True:
        user_text = input('Введите данные (для завершения ввода - пустая строка): ')
        if user_text == '':
            break
        f.writelines((user_text, '\n'))

with open('hw5.1 testfile.txt', encoding='utf-8') as f:
    print(f'Следующие данные будут добавлены в файл hw5.1 testfile.txt'':\n', f.read())

'''# V2
testfile = open('hw5.1 testfile.txt', 'w')

while 1 == 1:
    any_data = input('Введите данные (для завершения ввода - пустая строка): ')
    if len(any_data) == 0:
        break
    testfile.write(f'{any_data}\n')

testfile.close()'''