Eaten_food = list()
while True:
    food = input('What do you want to eat?')
    if food == 'stop':
        break
    elif food == 'Cordonyellow' or food == 'cordonyellow':
        print('Do not eat the creator of this program!')
    else:
        Eaten_food.append(food)
    print('You have eaten', Eaten_food)