import csv
import sys
cont = 'y'
while cont == 'y':
    print ("Выберите с какой группой студентов хотите работать: 1 группа, 2 группа, 3 группа: ")
    e = int(input())
    def studs():
        if e == 1:
            return 'stud1.txt'
        elif e == 2:
            return 'stud2.txt'
        elif e == 3:
            return 'stud3.txt'
    studs = studs()
    choice = int(input("Выберите действие: 1. Чтение, 2. Полная перезапись файла, 3. Дозапись в файл, 4. Поиск данных в файле, 5. Сортировка списка по среднему баллу "))
    if choice == 1:
        fd = open (studs, 'r', encoding = 'utf-8')
        reader = fd.read()
        print (reader)
        fd.close()
    elif choice == 2:
        fd = open (studs, 'w', encoding='utf-8')
        fd.write ('Полная перезапись')
        fd.close()
    elif choice == 3:
        f = open (studs, 'a', encoding = 'utf-8')
        newball = input ("Введите баллы зно: ")
        newstud = input ("Введите ФИО: ")
        f.write ('\n'+newball+" "+newstud)
        f.close()
    elif choice == 4:
        search = input("Введите что хотите найти: ")
        fd = open (studs, 'r', encoding = 'utf-8')
        reader = fd.read()
        if search in reader:
            print ("Найден")
        else:
            print ("Не найден")
        fd.close()
    elif choice == 5:
        fd = open (studs, 'r', encoding = 'utf-8')
        for l in sorted(fd):
            print(l, end = ' ')
