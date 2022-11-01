#завдання1
'''str=str(input('Input your text:'))
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
       'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in str:
    for j in arr:
        if i==j:
            str=str.replace(i, '')
print('Transformed text: {}'.format(str))'''

#завдання2
sequence=bytes(input('Input the sequence of symbols:'),"cp1251")
x=sequence.decode("cp1251")
y=len(sequence)
a=x[:y//2]
b=x[y//2:]
result=a.replace(':', '.') + b.replace('!', '.')
print('Result:', result)

