ten = list(range(1,11))
evens = list(filter(lambda t: not t % 2,ten))
evens1 = list(map(lambda t: t ** 2,evens))
print(evens1)
while True:

    try:
        def text(a):
            print(ten[a])
        text(int(input('введите индекс')))
    except ValueError:
        print('толька цифры!:')
    except IndexError:
        print("не верный индекс:")
