import json
import configparser
from dotenv import load_dotenv
import  os

#with open('input.json', 'r', encoding='utf-8') as file:
#    data = json.load(file)


#data['city'] = 'Минск'
#with open('input.json', 'w', encoding='utf-8') as file:
#    json.dump(data, file, indent=4, ensure_ascii = False)

#s = '{"fname":"ivan", "lname":"Inanov"}'
#data = json.loads(s)

#data['city'] = 'Минск'

#test = json.dumps(data, ensure_ascii = False)
#print(test)


config = configparser.ConfigParser()
with open('setings.ini', 'r', encoding='utf-8') as file:
    config.read_file(file)

print(config['SETTINGS']['age'])
print(config.sections())
config.add_section('Two_SECTIONS')
print(config.sections())

print(config.has_section('TRIED'))

print(config.options('SETTINGS'))#

print(config.has_option('SETTINGS','city')) #нету такой секции

config.set('SETTINGS', 'city', 'Minsk')

print(config.options('SETTINGS'))
print(config['SETTINGS']['city'])

with open('setings.ini', 'w', encoding='utf-8') as file:
    config.write(file)