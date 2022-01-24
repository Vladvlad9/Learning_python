"""№1 в файле хранятся числа, каждое на своей строке, и не только числа, необходимо просуммировать все числа,
игнорируя строки где не числа или не только числа"""

numbers = 0
with open('index.txt', 'r', encoding='utf-8') as file:
    lst = [line.strip() for line in file]

    for j in lst:
        if j.isnumeric():
            numbers += int(j)

    print('Сумма всех чисел равна: ' + str(numbers))