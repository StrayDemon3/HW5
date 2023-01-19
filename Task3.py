# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

with open('file1.txt', 'w', encoding = 'UTF-8') as data:
    data.write('5a3b4c7d8f')
    

with open('file1.txt', 'r', encoding = 'UTF-8') as data:
    file1 = data.read()

print(file1)
file2 = ''
try:
    int(file1[0])
    for i in range(0, len(file1)-1, 2):
        file2 += file1[i+1] * int(file1[i])
        print(file1[i])
    print(file2)
    with open('file2.txt', 'w', encoding = 'UTF-8') as data:
        data.write(file2)
except:
    count = 1
    for i in range(len(file1)-1):
        if file1[i] == file1[i+1]:
            count += 1
        if file1[i] != file1[i+1]:
            file2 += str(count) + file1[i]
            count = 1
    file2 += str(count) + file1[i]
    print(file2)
    with open('file2.txt', 'w', encoding = 'UTF-8') as data:
        data.write(file2)

