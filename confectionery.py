goods = {'торт': ['мука, яйца, сахар, сметана', 0.025, 1000],
         'пирожное' : ['мука, сахар, сливки', 0.021, 500],
         'маффин' : ['мука, сахар, масло', 0.019, 500]}
while True:
    description = input('Добро пожаловать! Что Вас интересует? Введите с клавиатуры необходимое: описание/ цена/ количество/ вся информация/ приступить к покупке ')
    for key, value in goods.items():
        if description == 'описание':
            print(f'{key}: {value[0]}')
            continue
        elif description == 'цена':
            print(f'{key}: {value[1]} р./100гр.')
            continue
        elif description == 'количество':
            print(f'{key}: {value[2]} гр.')
            continue
        elif description == 'вся информация':
            print(f'{key}: {value[0]}; {value[1]} р./100гр.; {value[2]} гр.')
            continue
    if description == 'приступить к покупке':
        break
cost = 0
while True:
    good = input('Введите название товара или введите n для выхода: ')
    if good == 'n' or good not in goods:
        break
    qty = int(input('Сколько Вы хотите купить? '))
    if qty > goods[good][2]:
        print('Столько нет в наличии, выберите другое количество или товар ')
        continue
    cost += qty * goods[good][1]
    goods[good][2] -= qty
print(f'Сумма к оплате {cost} р.')
for key, value in goods.items():
    print(key, '-', value[1], '-', value[2])
print('До свидания.')
