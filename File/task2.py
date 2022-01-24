"""В файле записано стихотворение. Выведите его на экран, а также укажите, каких слов в нем больше:
начинающихся на гласную или на согласную букву (регистр не учитывается)?"""

words = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
Vowels = 0
Consonants = 0

with open('task_2_txt.txt', 'r', encoding='utf-8') as txt_2:
    poem = txt_2.read()
    print(poem)

with open('task_2_txt.txt', 'r', encoding='utf-8') as txt_2:
    lst = [line.lower().strip().split() for line in txt_2]

    for j in lst:
        for k in j:
            if k[0] in words:
                Vowels += 1
            else: Consonants += 1

    print(f'Начинающихся на гласную букву слов в сихотворении: {str(Vowels)}, а согласную: {str(Consonants)}')