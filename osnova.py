money = 0
game_money = 0
def hi():
    print("Здравствуйте, уважаемый пользователь нашего казино!\n")
    set_monney()

def set_monney():
    global money
    try:
        moneys = int(input("Укажите сумму которую вы готовы положить на ваш банк(Сумму нужно указать цифрами)\n"))
        money = moneys
        print(money)
        game()
    except:
        print("Вам нужно указать сумму цифрами")
        set_monney()

def game():
    play = input("Здраствуйте. Какую игру вы хотите сыгрть?\nУ нас есть 'Рулетка','Джекпот'и'Блекджек'.").title()
    if play == 'Рулетка':
        print("Отличный выбор!")
        play_ruletka()
    elif play == 'Джекпот':
        print("Отличный выбор!")

    elif play == 'Блекджек':
        print("Отличный выбор!")
    
    else:
        print("Вы ввели не правильно название игры. название игры нужно вводить без ковычер и без лишних символов.")
        return


def pl_ruletka():
    global game_money
    try:
        game_moneys=int(input("Введите ссуму которые вы нотовы поставит.\n"))
        game_money = game_moneys
        if game_money > money:
            print('Вы ввели ссуму больше чем у вас на банке.\nНапишите другую ссуму.')
        elif game_money < money:
            print(f"Отлично! ваша ссума {game_money}")
            print('Время выбрать на что вы будите ставить.')
    except:
        print("Нужно вести ссуму без лишних знаков")
        pl_ruletka()

def play_ruletka():
    ggame=input("В рулетке вы можете поставить на 'цвет' и на 'цифру").title()
    if ggame == "Цвет":
        print()
    elif ggame == "Цифра" or ggame == "Цифру":
        print()


hi()
