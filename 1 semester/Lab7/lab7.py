import re, os, shutil, pickle,shelve
from lab5 import books
import lab6
#1,2
try:
    os.mkdir('C:\\lab7')
    os.mkdir('C:\\lab7\\zhadko')
    print('Каталог lab7 успішно створено')
except FileExistsError:
    print('Каталог вже існує')
#3
shutil.copy(r"C:\Users\Admin\Downloads\for_lab_7\4.txt", r"C:\lab7\zhadko")
print('Файл завантажено в підкаталог')
#4
with open("lab5.txt", "wb") as f1:
    pickle.dump(books, f1)
try:
    os.mkdir('C:\\lab5')
    print('Каталог lab5 успішно створено')
except FileExistsError:
    print('Каталог вже існує')
try:
    shutil.move('lab5.txt', r'C:\\lab5\\')
    print('Файл переміщено в каталог lab5')
except:
    print('Файл вже існує в заданому каталозі')
with open(r"C:\lab5\lab5.txt", "rb") as f2:
    books = pickle.load(f2)
    books.append('Чистий код')
    print(books)
try:
    os.rename(r'C:\lab5\lab5.txt', r'C:\lab5\lab5rename.txt')
except OSError:
    print('Перейменувати файл не вдалося, або вже існує файл з заданим ім\'ям')
#5
try:
    os.mkdir('C:\\lab6')
    print('Каталог lab6 успішно створено')
except FileExistsError:
    print('Каталог вже існує')
try:
    db = shelve.open('C:\\lab6\\lab6.txt')
    print('Файл lab6.txt успішно створено')
except:
    print('Файл вже існує в заданому каталозі')
i=0
for book in lab6.allbooks:
    i+=1
    db["obj{}".format(str(i))]=book.name
    if i==2:
        db.update(obj2=book.author)
a=db.pop("obj1")
del db["obj3"]
m=list(db.items())
db.close()
print(a,m)
#7
with open(r"C:\Users\Admin\Downloads\for_lab_7\4.txt",'r') as f3:
    text=re.sub(r'\s+',' ',f3.read())
    text=text.replace('\n',' ')
    for x in ('йцукенгшщзхїфівапролджєячсмитьбю'):
        text=text.replace('{}. '.format(x), '{}.\n'.format(x))
    lines=text.split('.\n')
with open(r"C:\lab7\zhadko\4.txt",'w') as f4:
    f4.write(text)
    f4.close()
os.rename(r'C:\lab7\zhadko\4.txt', r'C:\lab7\zhadko\41.txt')
let=input('Введіть будь-яку літеру:')
with open(r'C:\lab7\zhadko\42.txt', 'w', encoding='utf-8') as f5:
    for i in lines:
        if let==i[0]:
            f5.write(i+'.\n')
print('Завдання успішно виконано')