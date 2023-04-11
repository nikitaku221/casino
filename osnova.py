import random

money = 0
game_money = 0
play =""

def hi():
    print("Здравствуйте, уважаемый пользователь нашего казино!\n")
    set_monney()

def set_monney():
    global money
    try:
        moneys = int(input("Укажите сумму которую вы готовы положить на ваш банк(Сумму нужно указать цифрами)\n\t"))
        money = moneys
        print(money)
        game()
    except:
        print("Вам нужно указать сумму цифрами\n")
        set_monney()

def game():
    global play
    play = input("Здраствуйте. Какую игру вы хотите сыгрть?\nУ нас есть 'Рулетка','Джекпот'и'Блекджек'.\nВы можете выйти  вам просто нужно написать 'выход'.\nТакже вы можете в любой момент пополнить баланс и снять денги с баланса, вам нужно написать 'баланс'\n\t").title()
    if play == 'Рулетка':
        print("Отличный выбор!")
        pl_ruletka()
    elif play == 'Джекпот':
        print("Отличный выбор!")

    elif play == 'Блекджек':
        print("Отличный выбор!")

    elif play == 'Баланс':
        print()
    elif play == 'Выход':
        return
    
    else:
        print("Вы ввели не правильно название игры. название игры нужно вводить без ковычер и без лишних символов.")
        game()


def pl_ruletka():
    global money
    global game_money
    global play
    try:
        game_moneys=int(input("Введите ссуму которые вы нотовы поставит.\n\t"))
        game_money = game_moneys
        if game_money > money:
            print('Вы ввели ссуму больше чем у вас на банке.\nНапишите другую ссуму.')
            pl_ruletka()
        elif game_money <= money:
            money = money - game_money
            print(f"Отлично! ваша ссума {game_money}")
            print('Время выбрать на что вы будите ставить.')
            if play == "Рулетка":
                play_ruletka()
            elif play == 'Джекпот':
                print("всё рубит)")
            elif play == 'Блекджек':
                print("норм")
    except:
        print("Нужно вести ссуму без лишних знаков")
        pl_ruletka()

def play_ruletka():
    ggame=input("В рулетке вы можете поставить на 'цвет' и на 'цифру'\n\t").title()
    if ggame == "Цвет":
        ruletka_svet()
    elif ggame == "Цифра" or ggame == "Цифру":
        print()

def ruletka_svet():
    global money
    global game_money
    stavka = input("Вы можете поставить свою ставку на зелённый цвет и крассный цвет.\nЕсли вы хотите вернуться назад напишите: Назад\n\t").title()
    color = ["Крассный","Чёрный"]
    colors = random.choice(color)
    if stavka == colors:
        print("Вы выиграли!!")
        game_money= game_money * 2
        money = money + game_money
        print(money)
    elif color is not None:
        print("Вы ввели не тот цвет")
        ruletka_svet()
    elif stavka == "Назад":
        game()
    else:
        print(f"Вы проиграли. Выпал {colors} цвет\n")
        ruletka_svet()

def ruletka_chislo():
    global money
    global game_money
    try:
        vibr_chisla=int(input("Напишите числа на которую вы поставить ставку от 1 до 36 (нельзя будет поменять число)\n\t"))
        chislo = random.randint(1, 36)
        if vibr_chisla == chislo:
            print("Вы выиграли!!")
            game_money= game_money * 3
            money = money + game_money
        else:
            print(f"Вы проиграли. Выпало число {chislo}\n")
            ruletka_svet()
    except:
        print("вам просто нужно ввести сумму")
        ruletka_chislo()

def balans():
    global money
    
    bal=input("Вы хотите 'пополнить' балан или 'снять' денги?").lower()
    if bal== 'пополнить':
        PL_balans()
    elif bal == 'снять':
        SN_balans()

def PL_balans():
    global money
    try:
         popol=int(input("ведите число которые вы хотите поставить на баланс"))
         money+= popol
    except:
        print("ВЫ ДОЛЖНЫ ВВЕСТИ ЧИСЛО!!!")
        PL_balans()

def SN_balans():
    print()
hi()
