file = open(file='diakok.txt', mode='r', encoding='UTF-8')

legmagasabb:int = -1
lgm_neve:str = ''

for sor in file:
    d:list[str] = sor.strip().split(' ')
    if int(d[2]) > legmagasabb:
        legmagasabb = int(d[2])
        lgm_neve = f'{d[0]} {d[1]}'

print(f'a legmagasabb diák: {lgm_neve} ({legmagasabb} cm)')