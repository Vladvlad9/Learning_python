import json

with open('input.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


#fileds = ('barcode', 'title', 'price', 'total')
#product = {}

#for fild in fileds:
#    product[fild] = input(f'{fild}')

#data.append(product)

print(data)



#with open('input.json', 'w') as f:
#    json.dump(data, f, indent=2, ensure_ascii=True)



