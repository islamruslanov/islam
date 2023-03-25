sogl = "qwrtypsdfghjklzxcvbnmйцкнгшщзхфвпрлджчсмтб"
gls =  "euioaуеыаоэяиюё"

while True:
    vowels = 0
    consonants = 0
    text = input("введите текст",)
    if text == "выход":
        break
    for i in text:
        if i in sogl:
            vowels += 1
        elif i in gls:
            consonants += 1
    percent = round(vowels / (vowels + consonants) *100,1)
    percent2 = round(consonants / (vowels + consonants) * 100,1)
    print(F' Слово:{text,}\n Количество букв:{consonants + vowels}\n Согласных букв:{vowels,}\n Гласных букв:{consonants}\n Гласные/Согланые:{percent}%/{percent2}%')