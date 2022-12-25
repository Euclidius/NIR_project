letters = 'йцукенгшщзхъфывапролджэячсмитьбюёЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
dirs = ['tolst', 'cheh']
source = '/home/evarist/Рабочий стол/python/project'
SYMBOLS_IN_FILE = 20000

for dir in dirs:
    identifier = dir[0]

    with open(f'{source}/{dir}/source.txt') as f:
        data = f.read()

    starter_index = 0
    counter = 0
    k = open(f'{source}/{dir}/{identifier}{starter_index}.txt', 'w')
    for i in data:
        if counter < SYMBOLS_IN_FILE and (i in letters or i in (' ', '\n', '!', '.', ',', '?', ':', '-')):
            k.write(i)
            counter += 1
        elif counter >= SYMBOLS_IN_FILE and (i in ('.', '!', '?')):
            k.write(i)
            k.close()
            starter_index += 1
            counter = 0
            k = open(f'{source}/{dir}/{identifier}{starter_index}.txt', 'w')
        else:
            k.write(i)
            counter += 1
        
