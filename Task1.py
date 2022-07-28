'''
Задача 1.
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) (доп) Подумайте как наделить бота ""интеллектом""
'''
def play_game(total_candies, players, candies_per_round):                                                 
    count = 0
    while total_candies > 0:
        print(f'{players[count % 2]}, введите количество конфет, которое хотите взять: ')
        take_candy = int(input())
        if take_candy > candies_per_round or take_candy > total_candies:
            print(f'Всего осталось конфет: {total_candies}. Конфет больше {candies_per_round} брать нельзя!')
        else: 
            total_candies = total_candies - take_candy
            print(f'Всего осталось конфет: {total_candies}')
        count +=1
    return players[not count % 2]

player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')
players = [player_1, player_2]
total_candies = int(input('Введите начальное количество конфет: '))
candies_per_round = int(input('Введите количество конфет, которое можно взять игроку за один ход: '))

winner = play_game(total_candies, players, candies_per_round)
print(f'Победил игрок - {winner}')