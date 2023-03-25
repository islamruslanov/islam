data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
del numbers[0]
letters.append(numbers.pop(0))
numbers.insert(1,2)
numbers = sorted(numbers)
letters = letters[::-1]
letters[1] = "G"
letters[7] = "c"
numbers = [i ** 2 for i in numbers]
numbers = tuple(numbers)
letters = tuple(letters)

print(letters)
print(numbers)
