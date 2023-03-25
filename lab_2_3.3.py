#3.3
import sys

args_list = sys.argv
arr = [int(x) for x in sys.argv[1:]]
sum_elem = 0
for i in range (0, len(arr)):
  if i % 2 != 0:
    sum_elem = sum_elem + i
print('Сумма нечетных чисел: ', sum_elem)

m = 2
for i in range(0, len(arr)):
   if arr[i] < 15:
     arr[i] *= m
     print('Удвоенное число: ', arr[i])
print(arr)