from random import randint
from functools import reduce

def opt():
    print ("Выберите список: 1 Произвольный список, 2 Случайный список")
    option = str (input ())
    if option == '1':
        e=int(input("Введите размер списка: "))
        print ("Введите элементы списка: ")
        A = []
        for i in range (e):
            A.append(int(input()))
        return list(A)
    elif option == '2':
        A = []
        for h in range(10):
            A.append(randint(-100, 100))
        return list(A)
    else:
        print ("Выберите валидный список")
spisok = opt()

def sortd():
    return sorted(spisok)
sortdlist = sortd()

def sortdrev():
    srev = spisok
    return list(sorted(srev, reverse = True))
sortdrev = sortdrev()

def search():
    search = int (input ("Введите значение для поиска: "))
    s_check = search in spisok
    if s_check == True:
        print (" ", "Элемент есть в списке")
        print (" ", "Номер элемента в первоначальном списке:", spisok.index (search)+1)
        print (" ", "Номер элемента в отсортированном списке:", sortdlist.index (search)+1)
    else:
        print (" ", "Элемента нет в списке")

def sequence():
    elseq = str(input("Введите последовательность элементов (через запятую и пробел): "))
    listspis = str(spisok)
    listspisrev = str(sortdlist)
    if elseq in listspis:
        print (" ", "Последовательность", elseq, "найдена в изначальном списке")
    elif elseq in listspisrev:
        print ("Последовательность ", elseq," не найдена в изначальном списке, но найдена в сортированном списке")
    else:
        print (" ", "Последовательность не найдена")

def fiveminel():
    for i in range (0, 5):
        print (sortdlist[i])

def fivemaxel ():
    for x in range (0, 5):
        print (sortdrev[x])

def arith_mean():
        return float (sum(spisok)) / max(len(spisok), 1)

def unique():
        doplist = []
        for a in spisok:
            if a not in doplist:
                doplist.append(a)
                yield a

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(spisok):
    return reduce(lcm, spisok)

def duplicate():
    dupl = {}
    for i in set(spisok):
        dupl[i] = spisok.count(i)
    return dupl

def shift():
    shift = int(input("Введите на сколько элементов нужно сместить список: "))
    lst = spisok[-shift:] + spisok[:-shift]
    return lst
