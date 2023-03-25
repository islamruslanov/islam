data = int(input("введите день рождение:"))
month = int(input("введите месяц рождение:"))
if (data >= 21 and data <=31 and month == 3) or (data >1 and data <= 20 and month == 4):
    print("Овень")
elif (data >= 21 and data <= 31 and month == 4 ) or (data >1 and data <= 21 and month == 5):
    print('телец')
elif (data >= 22 and data <= 31 and month == 5 ) or (data >1 and data <= 21 and month == 6):
    print("близнецы")
elif (data >= 22 and data <= 30 and month == 6  ) or (data >1 and data <= 22 and month == 7):
    print("Рак")
elif (data >= 23 and data <=31 and month == 7 ) or (data >1 and data <=21 and month == 8):
    print("Лев")
elif (data >= 22 and data <= 31 and month == 8 ) or (data >1 and data <= 23 and month == 9):
    print('Дева')
elif (data >= 24 and data <= 30 and month == 9) or (data >1 and data <= 23 and month == 10):
    print('весы')
elif (data >= 24 and data <= 31 and month == 10) or (data >1 and data <= 22 and month == 11):
    print('скорпион')
elif (data >= 23 and data <= 30 and month == 11) or (data >1 and data <= 22 and month == 12):
    print('стрелец')
elif (data >= 23 and data <= 31 and month == 12) or (data >1 and data <= 20 and month == 1):
    print('Козерог')
elif (data >= 21 and data <= 31 and month == 1 ) or (data >1 and data <= 19 and month == 2):
    print('водолей')
elif (data >= 20 and data <= 31 and month == 2) or (data >1 and data <= 20 and month == 3):
    print("рыба")
else:
    print('ERROR!!')