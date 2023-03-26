a = ''
b = ' '
c = 'abc'
d = b.strip(' ')
e = 'A A A'
f = e.replace(' ', '')
print('e = ', e)
print('f = ', f)

print('a = ', a)
print('b = ', b)
print('b = ', c)

if a == '':
    print('a vazia')

if b == '':
    print('b vazia')
else:
    print('b cheio')

if c == '':
    print('c vazia')
else:
    print('c cheio')

if d == '':
    print('d vazia')
else:
    print('d cheio')
