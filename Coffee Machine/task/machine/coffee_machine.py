resource = [400, 540, 120, 9, 550]
espresso = [250, 0, 16, 1, 4]
latte = [350, 75, 20, 1, 7]
cappuccino = [200, 100, 12, 1, 6]
new_resource = [[], [], [], [], []]


def result(resource):
    print('The coffee machine has:')
    print(str(resource[0]) + ' of water')
    print(str(resource[1]) + ' of milk')
    print(str(resource[2]) + ' of coffee beans')
    print(str(resource[3]) + ' of disposable cups')
    if resource[4] == 0:
        print(str(resource[4]) + ' of money')
    else:
        print('$' + str(resource[4]) + ' of money')


def write_action():
    action = str(input('\n' + 'Write action (buy, fill, take, remaining, exit):' + '\n'))
    if action == 'exit':
        quit()
    elif action == 'remaining':
        print()
        result(resource)
        write_action()
    elif action == 'take':
        action_take()
    elif action == 'fill':
        action_fill()
    elif action == 'buy':
        action_buy()


def action_take():
    print()
    print('I gave you $' + str(resource[4]))
    resource[4] = 0
    write_action()


def action_fill():
    print()
    resource[0] += int(input('Write how many ml of water do you want to add:' + '\n'))
    resource[1] += int(input('Write how many ml of milk do you want to add:' + '\n'))
    resource[2] += int(input('Write how many grams of coffee beans do you want to add:' + '\n'))
    resource[3] += int(input('Write how many disposable cups of coffee do you want to add:' + '\n'))
    write_action()


def check_resource(coffee):
    for i in range(len(resource) - 1):
        if resource[i] - coffee[i] < 0:
            print('Sorry, not enough resource!')
            write_action()
        else:
            print('I have enough resources, making you a coffee!')
            resource_calculation(coffee)


def resource_calculation(coffee):
    global resource
    for i in range(len(resource) - 1):
        new_resource[i] = resource[i] - coffee[i]
    new_resource[4] = resource[4] + coffee[4]
    resource = new_resource
    write_action()


def action_buy():
    print()
    coffee = str(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:' + '\n'))
    if coffee == 'back':
        write_action()
    elif coffee == '1':
        check_resource(espresso)
    elif coffee == '2':
        check_resource(latte)
    elif coffee == '3':
        check_resource(cappuccino)


write_action()
