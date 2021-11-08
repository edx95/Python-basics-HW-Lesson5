# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('hw5.1 testfile.txt', encoding='utf-8') as f:
    lines = f.readlines()
    print(f'В файле {len(lines)} строк')
    for num, word in enumerate(lines, 1):
        print(f'В {num} строке {len(word.split())} слов')