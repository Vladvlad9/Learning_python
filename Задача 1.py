with open('index.txt', 'r', encoding='utf-8') as txt:
    line = [i.strip().strip() for i in txt]
    a = line[-2]
    print(a)