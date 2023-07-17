def countdown(n):
    if n <= 0:
        print('Odpalenie!')
    else:
        print(n)
        countdown(n-1)
countdown(4) #TAK SIĘ WYWOŁUJE FUNKCJĘ!! PAMIĘTAJ O TYM!!!!!!!! NAZWA FUNKCJI I W NAWIASIE ARGUMENT PARAMATRU (JAKAŚ WARTOŚĆ). W TYM PRZYPADKU N = 4