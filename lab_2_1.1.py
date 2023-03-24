a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
print('минимальным является: ', end='')
if b>= a <=c:
    print(a)
elif a >= b <= c:
    print(b)
elif a >= c <= b:
    print(c)