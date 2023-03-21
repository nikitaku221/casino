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
    global game_money
    global play
    try:
        game_moneys=int(input("Введите ссуму которые вы нотовы поставит.\n\t"))
        game_money = game_moneys
        if game_money > money:
            print('Вы ввели ссуму больше чем у вас на банке.\nНапишите другую ссуму.')
            pl_ruletka()
        elif game_money < money:
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
    ggame=input("В рулетке вы можете поставить на 'цвет' и на 'цифру\n\t").title()
    if ggame == "Цвет":
        ruletka_svet()
    elif ggame == "Цифра" or ggame == "Цифру":
        print()

def ruletka_svet():
    stavka = input("Вы можете поставить свою ставку на зелённый цвет и крассный цвет\n\t").title()
    color = ["Крассный","Чёрный"]
    colors = random.choice(color)
    if stavka == colors:
        print("Вы выиграли!!")
    elif color is not None:
        print("Вы ввели не тот цвет")
        ruletka_svet()
    else:
        print(f"Вы проиграли. Выпал {colors} цвет\n")
        dd = input("Вы хотите дальше продолжить играть напишите Да или Нет")



hi()
