Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
delited = Geeks.pop('bag')
Geeks['address'] = 'ибраимова,103'
Geeks['Tel'] = '996507052018'
Geeks['ins'] = 'geeks_edu'
new_couress = ['IOS','UX/UI','Android','Fronted','Backend']
Geeks['courses'] = set(Geeks['courses'] + new_couress)
Geeks['Дата оснвание'] = ("2018 года")
for k,v in Geeks.items():
    print(f'{k}:  {v}')





