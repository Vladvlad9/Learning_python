import os
import pprint

#print(os.name)# определение ОС
#print(os.environ)# служать что бы положить секретные ключи\токены
#print(os.uname())#более детальное описание OC
#print(os.getcwd())#где находиться исполняеммый файл

#os.chdir('../папка')
#print(os.getcwd())

#print(os.listdir('.'))#выводит содержимое папки ('../любая папка')


#os.mkdir('folder')#создать папку, создать можно только 1 раз
#os.makedirs('folder_0/folder/folder')#создает иерархию папки
#os.remove('файл')#удаление файла
#os.rename('index.txt', 'index1.txt')#переименование файла
#os.renames('index1.txt', 'folders/input.txt')#переименование файла
#os.replace('lesson1.py','lesen2.py')#замена файла
#os.rmdir('folder')#удаляет ПУСПУЮ папку
#os.removedirs('folders')#удалят максимальнкю глубокую папку пока не зайдет любой файл

#print(list(os.walk('.')))#проверяет все что есть в папках
#print(os.path.exists(('task3.py')))#Проверяет существует ли файл,(в любой папке)
