# time = ""
# temperature = 19

# if time == "morning" or time == 'утро':
#     print('good mornig')
# elif time == 'day' or time == "день":
#     print("good afternoon")
# elif time == 'evening' or time == "вечер":
#     print('good evening')
# else:
#     print('hello. i dont"t know time!')
#     if temperature < 10 :
#         print('одевайся теплее')
#     elif temperature > 10 and temperature <20:
#         print("на улице прохладно")
#     else:
#         print("тепло")
# word = input('введите слово').lower()
# reversed_word = word[::-1]
# if word == reversed_word:
#     print(True)
# else:
#  print(
#     f'слова {word } не равно обратному слову {reversed_word}'
# )


# login = "isu"
# password = "2345"
#
# input_login = input("укажите логин: ")
#
# if input_login == login:
#     input_password = input(f"укажите пароль для :{input_login}:")
#     if input_password == password:
#         input_password2 = input('подвердите пороль ')
#         if input_password == input_password2:
#             print(F'уважаемый{input_login},вы успешно авторизовали! ')
#         else:
#             print("не верный пороль!")
#     else:
#         print("не верный порль")
# else:
#     print(f"логин не сушествует ")

# c = 0
# while c!=200:
#     c += 1
#     if c % 2 !=0:
#         print("вы пропустили не четное число:")
#         continue
#     print('hello', c)

# amount = int(input('сколько раз будем повторя код'))
# attemps = 3
# while attemps !=0:
#     time = input(f'введите время суток:\nосталось попыток  {attemps}')
#
#     if time == "morning" or time == "утро":
#         print("good morning")
#     elif time == "day" or time == "день":
#         print("good afternoon")
#     elif time == "evening" or time == 'вечер':
#         print("good evening")
#     else:
#         print("hello, i don't know time!")
#         attemps -=1
#         if attemps == 0:
#             seconds = 20
#             while seconds !=0:
#                 print(seconds)
#                 sleep(1)
#                 seconds -= 1
#             attemps = 3

# word = 'трактор синний'
# c=0



# while c != len(word):
#     print(word[c])
#     c+=1


 # rounds = 0
# while rounds !=5:
#     rounds += 1
#     if rounds == 3 :
#         break
#     print(f'круги: {rounds}')







    # amount -=1







# word = "123456789"
#
# first = int(word[:2])
# second =int( word[-2:])
# print(first + second)



# print(word[::-3])


# text = word[6:-2]
# print(text)
# print(word[0])
# print(word[6])




# print(word.startswith('4'))
# print(word.isalpha())
# print(word.isnumeric())


# print(bool(7))
# print(type(True))
# print(2==3)
# print(2!=4)
# print(2<4)
# print(2>2 or 2==2)
# print(2>1 and 2 > 3)
# print(4 > 2 >1)
# a = 10
# a +=  4
# print(a)
# word = 'geectech'
# for i in word:
#     if i == 't':
#         break
# #


# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)
# cash = 100
# years = 5
# perents = 0.05
#
#
#
# for years in range(years):
#     cash += cash * perents
#     print(f'год: {years}{cash}')

# eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
# rus = "йцукенгшщзхъфывапролджэячсмитьбю"
#
# while True:
#     word = input("\nвведите слово:").lower()
#     if word == "exit" or word == "выход":
#         break
#     for letter in word:
#         if letter in eng:
#             print(rus[eng.index(letter)],end='')
#         else:
#             print(eng[rus.index(letter)],end='')


# new = list(range(1,6))







# object = ['бегайым','арген','эльхан','азамат''куманжан']
# new = object.copy()
#
# print(id(object))
# print(id(new))
#
# print(object == new)
# print(object is new)
#
# print(object)
# print(new)

# new[0] = 'amir'
# new1 = sorted(object)
# print(object)
# print(new1)
# object[3],object[4] = object[4],object[3]
# object.reverse()
# object = object[::-1]
# object.clear()
# object[-3] += 3
# object[3:5] = ['php','c++']
# object[object.index(13)] = [23,45,6]
#object.sort(key=len,reverse=True)
# object.reverse()

# print(object)







# object.append(new)
# object.insert(4,new)
# object.extend(new)
# object+= new










# object.remove(24)
# object.remove('python')
# deleted = object.pop(1)
# print(deleted)

# del object[0]
# print(object)


# word  = (2,3,4,5,6)
# data.append
# data = [['fuel',2,2],['time',2,2]]
# for i in data:
#   print(f'word:{i[0]} cons: {i[1]} vow {i[2]}')

#numbers = ['gwe',23,'sdf', 45,2.5,True,8.5]

# numbers = [i for i in numbers if type (i) not in [int,float] ]
# numbers = [i*2 for i in numbers]
# print(numbers)
# for i in numbers:
#     print(type(i))




#
# print(weeckend_days)

# new = tuple('oop')
# new = (23,)
# print(new)
# new = tuple([int(i) for i in new])i
# weeckend_days = ('sunday', 'saturday','monday')
#
#
# for i in weeckend_days:
#     if i == 'moday':
#         break
#     print(i)
# else:
#     print('цикл завершен')
# numbers = ((1,2),(4,7))
#
#
# numbers += (3,)
# print(id(numbers))
# numbers = list(numbers)
# numbers.append(34)
#
# numbers = tuple(numbers)
# print(numbers)

# new = dict(enumerate('pyhon'))
# new = dict([['one ',1], ['two',2]])
# new = dict(name= 'donald',age= 19, contry='usa')
# print(new)
# student = {
#     'name':'jack',
#     'age': 20,
#     'weihgt':65.7,
#     'hobby':['chess','english','books'],
#     'sex':'male'
# }
# maleprint(student['nam'])
# print(student.get('name','нет такого ключа'))
# item = [f'{name}:{} x {price} = {sum_item}']
#
# data = {
#     'cola':42,
#     'snickers':55,
#     'bounty':60,
#     'lays':120
# }
# result = []
# bill = 0
# for name , price in data.items():
#     amount =int(input(f'укажите количество{name}({price}):'))
#     sum_item = price * amount
#     result.append(f'{name}:{amount} x {price} = {sum_item}')
#
# #



# regions = ['чуй','ош','нарын','ыссык-куль','джалал-абад','талас','баткен']
# data = {i: int(input(F'введите температуру в {i.title()}')) for i in regions}
# sum_temps = sum(data.values())
# amount = len(regions)
# print(round(sum_temps / amount, 2))
# print(data)

# student =
# for t ,v in student.items():
#     print(f'{t} {v}')
# for i in student:
#     print(f'{i}:{student[i]}')
# print(student.keys())
# print(student.values())
# print(student.items())
# # new[wei]
# del student['hobby'][-1]
# deleted = student.pop('weihgt')
# del student['hobby']
# student['sex'] = 'famele'
# student['hoby'][0] = 'football'
# student['age'] += 1
# student ['car'] = True
# student['hoby'].append('boxing')
# student.update(new)


# print(student)

# print(type(student))
# sum,min,max,abs,
#
# print(min([23,0.1,12,34,17,0.4]))
# print(max([23,0.1,12,34,17,0.4]))
# print(max(range(1,51)))
# sogl = 'цкнгшщзхфвпрлджячсмтб'
# gls = "йуеъыаиоэяюь"
# trt = 0
# rew = 0
# while True:
#     text = input("ввдеите цифру ")
#     if text == ("no") or text == ("нет"):
#         print('fack')
#         break
#
#     for i in text:
#         if i in sogl:
#             trt += 1
#         elif i in gls:
#             rew += 1
#
#     rer2 = trt / (trt + rew) * 100
#     rer2 = int(rer2)
#     rer1 = rew / (rew + trt) * 100
#     rer1 = int(rer1)
#     print(F'согласыне:{trt}\nгласные:{rew}\nоОбший количество букв{trt + rew}\nгласные:{rer2}\nсогланые{rer1} ')

# regions = ['чуй','ош','нарын','ыссык-куль','джалал-абад','талас','баткен']
# data = {i: int(input(f'введите температуру в {i.title()}'))
#         for i in regions}
# sum_temps = sum(data.values())
# amount = len(regions)
# print(round(sum_temps / amount,2))
# print(min([23,0.1,12,34,17,0.4]))
# print(max([23,0.1,12,34,17,0.4]))
# print(sum(range(1,78)))
# from datetime import datetime
# data = {
#     'cola':42,
#     'snikers':55,
#     'bounty':60,
#     'lays':120
#
# }
# resuit = []
# bill = 0
# for name,price in data.items():
#     amount = int(input(f"укажите количество{name} ({price}):"))
#     sum_items = price * amount
#     resuit.append(f'{name}: {price} * {amount} = {sum_items}')
#     bill = int(resuit[-1].split()[-1])
# resuit.extend([bill,str(datetime.now())])
#
# for i in resuit:
#     print(i)

# data = ['cola','lays','cola','pepsi','lays''lays''lays''lays','cola']
#
# res = {i:data.count(i) for i in data}
# oftern = max(res.values())
#
# for i in data:
#     if data.count(i) == oftern:
#         oftern = i
#         print(oftern)
# numbers1 = [1,2,3,2,1,4,3]
# numbers2 = {1,2,3,2,1,4,3}
# numbers2.add(2)
# numbers2.remove(4)

# print(numbers1)
# print(numbers2)
# print(type(numbers2))
# print(max(res.values()))
# print(data[max(res.values())])
# print(res)
# print(oftern)
# lagman = {"лапша",'мясо','перец'}
# manty ={'мясо','тесто','лук'}
# print(lagman.union(manty))
# print(lagman.intersection(manty))
# print(lagman.difference(manty))
# print(lagman.symmetric_difference(manty))
# def is_palindrome(string, hello='hello'):
#     if string == string[::-1]:
#         return True
#     elif string == hello:
#         return "This is 'hello'"
#     else:
#         return False
#
# print(is_palindrome('racecar')) # True
# print(is_palindrome('hello')) # This is 'hello'
# print(is_palindrome('world')) # False

# w
#     pop = input('введите техт ')
#  if pop == pop[::-1]:
#     print(True)


# k = [1,2,3,4]
#

#
# a = int(input(F'введите число:'))
# oper = input(f'выберите щператора:')
# b = int(input(f"введите второе число :"))
# if oper == "+":
#     print(a + b)
# elif oper == "-":
#     print(a - b)
# elif oper == '*':
#     print(a*b)
# else:
#     print("error")


# while True:
#     pop = input(f'введите логин')
#     if pop == ('isu'):
#         print(input(f'введите пороль'))
#     elif pop == ('2607'):
#         print("можете выходит")
#     else:
#        print("не доступо")




# sogl = ("йуеъыаоэяиью")


# gls = ("цкнгшщзхфвпрлджчсмтб")
# sogl1 = 0
# gls2 = 0
#
# while True:
#     poit = input(f"введите число")
#     if poit == 'выход':
#         print('конец')
#         break
#
#
#     for i in poit:
#         if i in sogl:
#             sogl1 += 1
#         elif i in gls:
#             gls2 += 1
#         else:
#           print("error")
#     tip = sogl1 + gls2
#     ret = int(sogl1 / (sogl1 + gls2 )* 100)
#     ter = int(gls2 / (sogl1 + gls2) * 100)
#     print(f"соглассные букв:{sogl1}\nглассные букв:{gls2} \n обший :{tip}\n глс:{ret}\nсгл:{ter}")

# if poit == sogl:
#     print(sogl1 + 1)
# elif poit == gls:
#     print(gls2 + 1)
# else:
#     print(f"ангиский не поойдет")
# text = sogl1 + gls2
# # print(f"согласные: {sogl1} \n гласные: {gls2} \n обший букв")
# rus = ("йцукенгшщзхъфывапролджэячсмитьбю.")
# eng = ("qwertyuiop[]asdfghjkl;'zxcvbnm,./")
# cons = 0
# text = input('введите слово')
# for i in text:
#     if i in rus:
#         cons += 1
#     elif i in text:
#         cons += 1
# print(f'обший количество слов                          {cons}')



