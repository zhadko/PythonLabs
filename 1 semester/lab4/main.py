'''import random
n=int(input("Rількість елементів 1 списку  n="))
m=int(input("Кількість елементів 2 списку  m="))
if m>0 and n>0:
    def func(x): return "{0:.3f}".format(x)
    x=[]
    for i in range (n): x.append(random.uniform(-100,100))
    def func(y): return "{0:.3f}".format(y)
    y=[]
    for i in range (m): y.append(random.uniform(-100,100))
    z=x+y
    z.sort(reverse=False)
    def func(z): return "{0:.3f}".format(z)
    print("%20s" % "Список1:",(list(map(func,x))))
    print("%20s" % "Список2:",(list(map(func,y))))
    print("%32s" % "Результуючий список:",(list(map(func,z ))))
    if 0 in z : print("%50s" % "Число 0 є елементом результуючого списку")
    else :  print("%55s" % "Число 0 не є елементом результуючого списку")
else: print("Числа m та n мають бути натуральними")'''



import random
n=int(input("Введіть кількість рядків n :"))
m=int(input("Введіть кількість стовпців m :"))
if m==n and m>0 and m>0:
    a=[]
    for i in range (n):
        a.append([]*m)
        for j in range(m):
            a[i].append(random.randint(-99,99))
    print("%15s" %"Матриця:")
    for i in range (len(a)):
        for j in range (len(a[i])):
            print("{0:5}".format(a[i][j]), end='  ')
        print()
    b=[]
    for i in range (n): b.append(a[i][i])
    print("%50s" % "Найменший елемент головної діагоналі:", min(b))
    c=[]
    for j in range (n): c.append(a[-j][j-1])
    print("%50s" % "Найменший елемент побічної діагоналі:", min(c))
else: print("Матриця не квадратна або кількість рядків/стовпців не є натуральним числом ")