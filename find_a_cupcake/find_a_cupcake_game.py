from math import sqrt
from random import randint

game_width = 15
game_height = 10

cupcake_a = randint(0, game_width)
cupcake_b = randint(0, game_height)
player_a = 0
player_b = 0
player_found_key = False
steps = 0

distance_before_move = sqrt((cupcake_a - player_a) ** 2 + (cupcake_b - player_b) ** 2) #odległość gracza od babeczki na początku gry

while not player_found_key:
    steps += 1
    print()
    print('W tym pomieszczeniu znajduje się babeczka, znajdź ją i ciesz się smakowitym zwycięstwem! Możesz poruszać się w kierunkach określonych jako [W/A/S/D]: ')

    move = input('Dokąd idziesz?:  ')
    move_low = move.lower()
    if move_low == 'w':
        player_b += 1
        if player_b > game_height:
            print('Uderzasz w ścianę. To boli!')
            player_b = game_height
    elif move_low == 's':
        player_b -= 1
        if player_b < 0:
            print('Uderzasz w ścianę. To boli!')
            player_b = 0
    elif move_low == 'a':
        player_a -= 1
        if player_a < 0:
            print('Uderzasz w ścianę. To boli!')
            player_b = 0
    elif move_low == 'd':
        player_a += 1
        if player_a > game_width:
            print('Uderzasz w ścianę. To boli!')
            player_a = game_width
    elif move_low == 'q':
        print('Koniec gry.')
        quit()
    else: 
        print('Nie wiem dokąd zmierzasz. Podaj określony wyraz oznaczający kierunek poruszania.')
        continue

    if player_a == cupcake_a and player_b == cupcake_b:
        print('Brawo! Zdobył*ś babeczkę, smacznego!')
        print(f'Wykonał*ś {steps} ruchów, aby odnaleźć babeczkę. Gra zakończona.')
        quit()

    distance_after_move = sqrt((cupcake_a - player_a) ** 2 + (cupcake_b - player_b) ** 2) #odległość gracza od babeczki w trakcie gry

    if distance_before_move > distance_after_move:
        print('Super! Jesteś bliżej babeczki!')
    else:
        print('O nie! Oddalasz się od babeczki!')

    distance_before_move = distance_after_move
