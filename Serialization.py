import random

from Person import say_hello, Humans
from Non_organic import say_hello_nonOrganic, Bionicle
from Animal import say_hello_animals, Monsters

character_1 = Humans('Saytama', 22, 'Japan', 20, 4)
character_2 = Bionicle('vezon', 16, 'Voya nui', 'teletransporte', 20, 4)
character_3 = Monsters('rathalos', 17, 'Japan', 'llamas', 20, 4)
character_4 = Monsters('zinogre', 12, 'Japan', 'truenos', 20, 4)
character_5 = Bionicle('vezok', 16, 'Japan', 'ladron de poder', 20, 4)

number_not_repeat = [1, 2, 3, 4]
ram_command = random.sample(number_not_repeat, 1)

user_choose_character = None

user_character = None

computer_character = None

is_computer_character = None

say_hello(character_1)
print("\n")
say_hello_nonOrganic(character_2)
print("\n")
say_hello_animals(character_3)
print("\n")
say_hello_animals(character_4)
print("\n")
say_hello_nonOrganic(character_5)
print("\n")


def mini_figth():
    global ram_command

    global user_choose_character

    characters_menu()

    user_choose_character = main_menu()

    global is_computer_character

    is_computer_character = chose_character_computer()

    print('Tu rival sera: ' + is_computer_character.name)

    user_command = options_menu()

    while user_command != 'q':
        if user_command == 'hit':
            # print(desglose_number(ram_command))
            # print(desglose_number(number_not_repeat))
            enemy_dodge()
            user_command = input()

        elif user_command == 'heal':
            print(user_choose_character.name + ' se va a curar 5 puntos de vida' + f'(tu vida actual: {user_choose_character.pv})')
            if user_choose_character.pv == 20:
                print('no te puedes curar, ya tienes la vida hasta arriba')
                user_command = input()

            else:
                user_choose_character.pv = user_choose_character.pv + 5
                ram_command = random.sample(number_not_repeat, 1)
                enemy_ia()
                user_command = input()

        else:
            print('comando no valido')

            user_command = input()


def enemy_dodge():
    global ram_command
    global user_choose_character
    global is_computer_character

    if desglose_number(ram_command) == 1:
        is_computer_character.pv = is_computer_character.pv - user_choose_character.dmg

        if is_computer_character.pv <= 0:
            print(is_computer_character.name + ' Ha sido derrotado' + f'(tu vida actual: {user_choose_character.pv}) \n')
            quit(0)

        print('Uff!, eso dolió ahora ' + is_computer_character.name + ' le queda de vida ' + str(
            is_computer_character.pv) + f'(tu vida actual: {user_choose_character.pv})\n')

        ram_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()

    elif desglose_number(ram_command) == 2:
        print('vaya! esquivo tú ataque')
        ram_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()

    elif desglose_number(ram_command) == 3:
        print('Parece que ' + is_computer_character.name + " esta a muy distraido y recive un golpe critico")
        user_choose_character.dmg = user_choose_character.dmg + 2
        is_computer_character.pv = is_computer_character.pv - user_choose_character.dmg

        if is_computer_character.pv <= 0:
            print(is_computer_character.name + ' Ha sido derrotado' + f'(tu vida actual: {user_choose_character.pv}) \n')
            quit(0)

        print("dios mio, eso a sido un terrible golpe a " + is_computer_character.name + " le queda de vida " + str(is_computer_character.pv) + '\n')
        ram_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()

    elif desglose_number(ram_command) == 4:
        print('tu ataque se perdio!')
        ram_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()


def enemy_ia():
    global ram_command
    global user_choose_character
    global computer_character

    if desglose_number(ram_command) == 1:
        print('genial!, a fallado el ataque' + f'(tu vida actual: {user_choose_character.pv})')

    elif desglose_number(ram_command) == 2:
        print('Oh no! va a atacar ')

        user_choose_character.pv = user_choose_character.pv - is_computer_character.dmg

        if user_choose_character.pv <= 0:
            print(user_choose_character.name + ' Has perdido')
            quit(0)

        print(f'(tu vida actual: {user_choose_character.pv}) \n')

    elif desglose_number(ram_command) == 3:
        print('Oh no! va a atacar ')
        print('parece que sera golpe critico!')

        is_computer_character.dmg = is_computer_character.dmg + 2

        user_choose_character.pv = user_choose_character.pv - is_computer_character.dmg

        if user_choose_character.pv <= 0:
            print(user_choose_character.name + ' Has perdido')
            quit(0)

        print('uf! como dolio ese golpe critico ' + f'(tu vida actual: {user_choose_character.pv})')

    elif desglose_number(ram_command) == 4:
        print('parece que esta distraido')


def chose_character_user():
    global user_choose_character
    global user_character

    if user_choose_character == "saytama" or user_choose_character == "Saytama":
        user_character = character_1

    elif user_choose_character == "vezon" or user_choose_character == "Vezon":
        user_character = character_2

    elif user_choose_character == "rathalos" or user_choose_character == 'Rathalos':
        user_character = character_3

    elif user_choose_character == "zinogre" or user_choose_character == 'Zinogre':
        user_character = character_4

    elif user_choose_character == "vezok" or user_choose_character == 'Vezok':
        user_character = character_5

    return user_character


def chose_character_computer():
    global ram_command
    global user_choose_character
    global computer_character

    if desglose_number(ram_command) == 1:
        computer_character = character_2
        if computer_character == character_2:
            print('personaje ya elejido')
            computer_character = character_3

        else:
            computer_character = character_2

    if desglose_number(ram_command) == 2:
        computer_character = character_3
        if computer_character == character_3:
            print("personaje ya elejido")
            computer_character = character_2

        else:
            computer_character = character_3

    if desglose_number(ram_command) == 3:
        computer_character = character_4
        if computer_character == character_4:
            print("personaje ya elejido")
            computer_character = character_5

        else:
            computer_character = character_4

    if desglose_number(ram_command) == 4:
        computer_character = character_5
        if computer_character == character_5:
            print("personaje ya elejido")
            computer_character = character_4

        else:
            computer_character = character_5

    return computer_character


def desglose_number(num_list: list):
    global num

    for num in num_list:

        return num


def main_menu():
    global user_choose_character

    print('Elije personaje')

    user_choose_character = input()

    print('has elejido a ' + user_choose_character)

    user_choose_character = chose_character_user()

    return user_choose_character


def options_menu():
    print('por favor escriba un comando valido:\n'
          '- atacar <==> hit\n'
          '- curarte <==> heal\n'
          '- habilidad <==> skill\n'
          '- magia <==> spell\n'
          '- salir del programa <==> q')

    user_command = input()

    return user_command


def characters_menu():

    print('elige un personaje: \n'
          '1.''no disponible''\'\n'
          '2.vezon\n'
          '3.rathalos\n'
          '4.zinogre\n'
          '5.vezok')


mini_figth()
