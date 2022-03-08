import json


with open('storage.json', 'r', encoding='utf-8') as file:
    storage = json.load(file)

# fields = ('barcode', 'title', 'price', 'total', 'weight', 'description')
# product = {}
# for field in fields:
#     # value = input(f'{field}: ')
#     product[field] = input(f'{field}: ')
# storage.append(product)
# with open('storage.json', 'w', encoding='utf-8') as file:
#     json.dump(storage, file, indent=2, ensure_ascii=False)

for product in storage:
    print(product['title'])

choice = input('Введи название товара: ').lower()
for i in range(len(storage)):
    if choice in storage[i].values():
        for field in storage[i]:
            print(field)
        choice_field: str
        while (choice_field := input('Выбери поле: ')) not in storage[i]:
            pass
        value = input('Введи новое значение для этого поля: ')
        storage[i][choice_field] = value
        break
else:
    print('Are you stupid man?')

with open('storage.json', 'w', encoding='utf-8') as file:
    json.dump(storage, file, indent=2, ensure_ascii=False)