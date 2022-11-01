import random
books=['Python3', 'Грокаем алгоритмы', 'Python для чайников', 'Кровь, пот и пиксели', 'Миллионы миллиардов']
pages=dict.fromkeys(books)
for i in pages:
    pages[i]=random.randint(50,200)
a=list(pages.values())
b=list(pages.keys())
print('{}\n{} - {}'.format(pages, b[a.index(max(a))], max(a)))