from random import randint
import math

class book:
    '''Детальний опис книги'''

    def __init__(self, name, author, pages, illustrations, editor, profpages, profillustr, profed):
        self.name = name
        self.author = author
        self.pages = pages
        self.illustrations = illustrations
        self.editor = editor
        self.fullprice = math.ceil(((profpages / 10) * pages) + (profillustr * illustrations) + profed)

    def price(self):
        print('Ціна книги \"{}\" = {} грн'.format(name, x.fullprice))

    def midprice_for_author(self):
        print('Середня ціна книг заданого автора = {} грн'.format(int(sum1 / len(b))))

    def midprice_for_editor(self):
        print('Середня ціна книг заданого видавництва = {} грн'.format(int(sum2 / len(c))))


allbooks = {
    book('Маруся Чурай', 'Костенко', 224, 12, 'А-ба-ба-га-ла-ма-га', randint(4, 10), randint(1, 5), randint(100, 200)),
    book('Триста поезій', 'Костенко', 416, 0, 'А-ба-ба-га-ла-ма-га', randint(4, 10), randint(1, 5), randint(100, 200)),
    book('Листи до сина', 'Стус', 280, 46, 'Ранок', randint(4, 10), randint(1, 5), randint(100, 200)),
    book('Палімпсести', 'Стус', 352, 0, 'А-ба-ба-га-ла-ма-га', randint(4, 10), randint(1, 5), randint(100, 200)),
    book('Тарас Бульба', 'Гоголь', 110, 12, 'Ранок', randint(4, 10), randint(1, 5), randint(100, 200)),
    book('Ніч перед Різдвом', 'Гоголь', 28, 14, 'А-ба-ба-га-ла-ма-га', randint(4, 10), randint(1, 5), randint(100, 200)),
    book('Зачарована Десна', 'Довженко', 219, 0, 'Фоліо', randint(4, 10), randint(1, 5), randint(100, 200)),
    book('Україна в огні', 'Довженко', 351, 7, 'Фоліо', randint(4, 10), randint(1, 5), randint(100, 200)),
    book('Мартин Боруля', 'Карпенко-Карий', 64, 0, 'Фоліо', randint(4, 10), randint(1, 5), randint(100, 200)),
    book('Сто тисяч. Хазяїн', 'Карпенко-Карий', 144, 17, 'Фоліо', randint(4, 10), randint(1, 5), randint(100, 200))
}
for book in allbooks:
    print('\"' + book.name + '\" -',book.author,'-\"' + book.editor + '\"')
name,u = str(input('Введіть назву книги із заданого списку: ')),0
for book in allbooks:
    if name==book.name:
        a,u=list(filter(lambda x: x.name == name, allbooks)),1
        for x in a:
            x.price()
if u==0:
    print('Данної книги немає в списку')

author,u = str(input('Введіть прізвище автора із заданого списку: ')), 0
for book in allbooks:
    if author==book.author:
        b,u,sum1=list(filter(lambda y: y.author == author, allbooks)),1,0
        for y in b:
            sum1+=y.fullprice
        y.midprice_for_author()
        break
if u==0:
    print('Данного автора немає в списку')

editor,u = str(input('Введіть назву видавництва із заданого списку: ')), 0
for book in allbooks:
    if editor==book.editor:
        c,u,sum2=list(filter(lambda z: z.editor == editor, allbooks)),1,0
        for z in c:
            sum2+=z.fullprice
        z.midprice_for_editor()
        break
if u==0:
    print('Данного видавництва немає в списку')