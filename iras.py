from math import pi

file = open(file='elso.txt', mode='w', encoding='UTF-8')

file.write('Hello, my first file!\n')
file.write('My name is Zoltán.\n\n')

for x in range(10):
    file.write(f'{pi ** x}\n')

print('kész!')