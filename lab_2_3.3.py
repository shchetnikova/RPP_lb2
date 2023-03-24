#3.3
list = []
list1 = []
for _ in range(int(input())):
  list.append(int(input()))
print(list)
for i in list:
  if i % 2 != 0:
    list1.append(i)
print('Сумма чисел с нечетным индексом: ', list1)
m = 2
for i in range(len(list)):
   if list[i] < 15:
     list[i] *= m
     print('Удвоенное число: ', list[i])
     print(list)