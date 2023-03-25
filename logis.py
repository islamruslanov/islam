import random
from decouple import config


def cosino():
    my_money = config('MY_MONEY', cast=int)
    balance = my_money
    while True:
        my_number = input('угодайте число от 1 до 30:')
        try:
            my_number = int(my_number)
            if my_number not in range(1,31):
                print('Вы ввели неподходящий номер:')
                continue
        except ValueError:
            print('Пожалуйста, вводите только целые числа:')
        try:
            my_bet = input('Выберите свою ставку:')
            my_bet = int(my_bet)
            if my_bet > balance:
                print(f'Ваша ставка больше доступного баланса:{balance}')
                continue
        except ValueError:
            print('Неверный действие')
            continue
        slot = random.randint(1,30)
        if slot == my_number:
            my_number += my_bet * 2
        else:
            balance -= my_bet
        play_again = input('Вы хотите продолжать? да или нет ? ')
        if play_again == "да":
            continue
        if play_again == "нет":
            print(f'ваш баланс {balance}')
            break
if __name__  == "__main__":
    cosino()










