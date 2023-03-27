def bubble_sort(number):
    n = len(number)
    for i in range(n-1):
        for b in range(n -1):
            if number[b] > number[b + 1]:
                number[b],number[b+1] = number[b+1],number[b]
    print(number)
bubble_sort([1,3,2,3,443,443,43,54,90,8])


a = [1,2,3,4,5,6,7,8,9]
def  binary_search(n,Val):
    ResultOk = False
    first = 0
    last = len(n) -1
    while first <= last:
        middle = (first + last) //2
        if Val == n[middle]:
            first = middle
            last = first
            ResultOk = True
            Pos = middle
        if Val > n[middle]:
            first=middle + 1
        else:
            last=middle-1
    if ResultOk == True:
        print(f'Элемент найден: {Pos} ')
    else:
        print('элемент не найден')


print(binary_search(a,4))




