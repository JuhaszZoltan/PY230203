file = open(file='adatok.csv', mode='r', encoding='UTF-8')

for sor in file:
    darabok:list[str] = sor.strip().split(';')
    print(f'a(z) {darabok[0]}-nak/nek {darabok[1]} lába van')