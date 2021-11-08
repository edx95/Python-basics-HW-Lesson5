# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.


input_num = input("Введите набор чисел, разделенных пробелами:   ")
numbers = [int(i) for i in input_num.split()]

with open("HW_5.5.txt", "w") as f_obj:
    f_obj.write(input_num)

print("Сумма чисел: " + str(sum(numbers)))

# v2
'''with open('HW_5.5.txt', 'w+') as f:
    numbers = '\n'.join(number for number in input('Вводите числа через пробел (enter для завершения ввода): ').split())
    f.writelines(numbers)
    f.seek(0)
    value = f.readlines()
    total = 0
    for el in value:
        total = total + float(el)
print('Сумма чисел:', total)'''