# 11 вариант
#1
print('Первое задание')
import math
m = float(input('Введите значение числа m '))
print(1 / (math.sqrt(m) + math.sqrt(2)))
#2
print('Второе задание')
n = float(input('Введите число на проверку '))
if n > 1:
    for i in range(2, int(n/2)+1):
         if (n % i) == 0:
            print("Число не является простым")
            break
    else:
        print("Это число простое")

else:
    print("Число не является простым")
#3
print('Третье задание')
mas = [2, 3, 6, -1, 7, 13, -7, -7.2, 13.2, 1, 4]
print(mas)
print('Найменше додатнє з поданих чисел дорівнює')
mas1 = mas.copy()
for j in range(len(mas1)-1):
  for k in range(j+1,len(mas1)):
    if mas1[j]>mas1[k]:
       mas1[j],mas1[k]=mas1[k],mas1[j]
print([x for x in mas1 if x > 0][0])
print('Сума парних чисел з поданих дорівнює')
s=0
for j in range(len(mas)):
    if mas[j]%2==0:
        s+=mas[j]
print(s)
print('Масив в обратном порядке: ' + str(list(reversed(mas))))
