#Завдання 1
'''import math
x=float(input())
y=float(input())
if x >= 0 and y >= 0 and math.log(y+3.5, math.e) + math.sqrt(y)!=0:
    r = (9.33*x*x*x + math.sqrt(x))/(math.log(y+3.5, math.e) + math.sqrt(y))
    print('x=' + str(x) + '\ny=' + str(y) + '\nR=' + str(r))
else:
    print('x,або y не задовільняє умові(x>=0, y>=0)')'''

#Завдання 2
'''a=float(input())
b=float(input())
c=float(input())
if a*a+b*b==c*c:
    print('Данний трикутник - прямокутний')
    print('гіпутенуза: c=' + str(c), '\nкатети: a=' + str(a) + ', b=' + str(b))
elif a*a+c*c==b*b:
    print('Данний трикутник - прямокутний')
    print('гіпутенуза: b=' + str(b), '\nкатети: a=' + str(a) + ', c=' + str(c))
elif c*c+b*b==a*a:
    print('Данний трикутник - прямокутний')
    print('гіпутенуза: a=' + str(a), '\nкатети: b=' + str(b) + ', c=' + str(c))
else:
    if a == b == c:
        print('Данний трикутник - рівносторонній, a=b=c=' + str(a))
    else:
        if a==b:
            print('Данний трикутник - рівнобедрений, a=b=' + str(a) + ', c=' + str(c))
        elif b==c:
            print('Данний трикутник - рівнобедрений, b=c=' + str(b) + ', a=' + str(a))
        elif a==c:
            print('Данний трикутник - рівнобедрений, a=c=' + str(c) + ', b=' + str(b))
        else:
            print('Данний трикутник - різносторонній: a=' +
                  str(a) + ', b=' + str(b) + ', c=' + str(c))'''

#Завдання 3
a=float(input())
n=int(input())
if n>0:
    for i in range(0, n):
        i+=1
        if a**i<=n:
            print(i, a**i)
    print('перше число = n - степінь, друге число = а^n')
else:
    print('N не задовільняє умові(N>0)')