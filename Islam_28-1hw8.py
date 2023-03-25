# low = 0
# high = 100
# mid = (low + high) // 2
# i = 0
# with open('results.txt','w',encoding='UTF-8') as file:
#     file.write('угадай цифру\n')
#
# while True:
#     print(f'Вы загадали {mid}')
#     user_answer = input(" 'да' или 'меньше' или 'больше' ")
#     i += 1
#     if user_answer .lower() == 'да':
#         with open('results.txt','a',encoding="UTF-8") as file:
#             file.write(f'попытки: {i}\n')
#             file.write(f'Ваше число: {mid}\n')
#             file.write(f'програма завершила задачу:')
#             print('програма завершено!')
#             break
#     elif user_answer == 'больше':
#         low = mid
#         mid = (low + high) // 2
#         with open('results.txt','a',encoding='UTF-8') as file:
#             file.write(f'Пере продолжаем програмы:  {mid} меньше число \n')
#     elif user_answer == 'меньше':
#         high = mid
#         mid = (low + high) // 2
#         with open('results.txt','a',encoding='UTF-8') as file:
#             file.write(f'пере продолжаем програмы:{mid} больше \n')
#     else:
#         print('не верный действие, попробуйте ещe раз:\n')



low = 0
heih = 100
mid = (low + heih) // 2
counts = 0
with open('type.txt','w',encoding='UTF-8') as text:
    text.write('угадай цифру \n')
while True:
    print(f'вы загадали {mid} ')
    counts += 1
    user = input('да или больше или меньше')
    if user == 'да':
        with open('type.txt','a',encoding="UTF-8") as text:
            text.write(f"попытки: {counts}\n")
            text.write(f'ваше число: {mid}\n')
            text.write('програма завершила задачу:\n')
            print('проограма завершена')
            break
    elif user == 'больше':
        low = mid
        mid = (low + heih) // 2
        with open('type.txt','a',encoding='UTF-8') as text:
            text.write(f'пере пeрeпродалжаем програму {mid} меньше число \n')
    elif user == 'меньше':
        heih = mid
        mid = (low + heih) // 2
        with open('type.txt','a',encoding='UTF-8') as text:
            text.write(f'перепродалжем програму {mid} больше число \n')
    else:
        print('не верный действие, попробуйте еше раз !!!')




