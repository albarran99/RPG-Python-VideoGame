import random
import sys

from pojos.Animal import Monsters
from pojos.Non_organic import Bionicle
from pojos.Person import Humans

character_1 = Humans('salary-man', 1, 0, 20, 4)
character_2 = Bionicle('vezon', 1, 0, 20, 4)
character_3 = Monsters('rathalos', 1, 0, 20, 4)
character_4 = Monsters('zinogre', 1, 0, 20, 4)
character_5 = Bionicle('vezok', 1, 0, 20, 4)

user_choose_character = character_1

computer_character = None

number_not_repeat = [1, 2, 3, 4]
ran_command = random.sample(number_not_repeat, 1)

you_random_heal = [1, 2, 3]
ran_heal = random.sample(you_random_heal, 1)


def desglose_number(num_list: list):
    global num

    for num in num_list:
        return num


def chose_character_computer():
    global ran_command
    global user_choose_character
    global computer_character

    if desglose_number(ran_command) == 1:
        computer_character = character_2
        if computer_character == user_choose_character:
            print('personaje ya elejido')
            computer_character = character_3

        else:
            computer_character = character_2

    if desglose_number(ran_command) == 2:
        computer_character = character_3
        if computer_character == user_choose_character:
            print("personaje ya elejido")
            computer_character = character_2

        else:
            computer_character = character_3

    if desglose_number(ran_command) == 3:
        computer_character = character_4
        if computer_character == user_choose_character:
            print("personaje ya elejido")
            computer_character = character_5

        else:
            computer_character = character_4

    if desglose_number(ran_command) == 4:
        computer_character = character_5
        if computer_character == user_choose_character:
            print("personaje ya elejido")
            computer_character = character_4

        else:
            computer_character = character_5

    return computer_character


def computer_player():
    global computer_character
    computer_character = chose_character_computer()
    print('Tu rival sera: ' + computer_character.name)


def enemy_dodge():
    global ran_command
    global user_choose_character
    global computer_character

    if desglose_number(ran_command) == 1:
        computer_character.pv = computer_character.pv - user_choose_character.dmg

        if computer_character.pv <= 0:
            print(
                computer_character.name + ' Ha sido derrotado' + f'(tu vida actual: {user_choose_character.pv}) \n')
            user_choose_character.xp = user_choose_character.xp + 30
            print("Has ganado " + str(30) + f' de experiencia, experiencia actual es: {user_choose_character.xp}')
            ran_command = random.sample(number_not_repeat, 1)
            chose_character_computer()
            user_choose_character.pv = user_choose_character.pv + 10
            sys.exit(0)

        print('Uff!, eso dolió ahora ' + computer_character.name + ' le queda de vida ' + str(
            computer_character.pv) + f'(tu vida actual: {user_choose_character.pv})\n')

        ran_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()

    elif desglose_number(ran_command) == 2:
        print('vaya! esquivo tú ataque')
        ran_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()

    elif desglose_number(ran_command) == 3:
        print('Parece que ' + computer_character.name + " esta a muy distraido y recive un golpe critico")
        user_choose_character.dmg = user_choose_character.dmg + 2
        computer_character.pv = computer_character.pv - user_choose_character.dmg
        user_choose_character.dmg = user_choose_character.dmg - 2

        if computer_character.pv <= 0:
            print(
                computer_character.name + ' Ha sido derrotado' + f'(tu vida actual: {user_choose_character.pv}) \n')
            user_choose_character.xp = user_choose_character.xp + 30
            print("Has ganado " + str(30) + f' de experiencia, experiencia actual es: {user_choose_character.xp}')
            ran_command = random.sample(number_not_repeat, 1)
            chose_character_computer()
            user_choose_character.pv = user_choose_character.pv + 10
            sys.exit(0)

        print(
            "dios mio, eso a sido un terrible golpe a " + computer_character.name + f" le queda de vida {computer_character.pv} " + '\n')
        ran_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()

    elif desglose_number(ran_command) == 4:
        print('tu ataque se perdio!')
        ran_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()

    else:
        print("los dos adversarios se miran fijamente")


def heal_user_player():
    global ran_heal
    print(user_choose_character.name + ' se va a curar la vida' + f'(tu vida actual: {user_choose_character.pv})')
    ran_heal = random.sample(you_random_heal, 1)
    if user_choose_character.pv == 20:
        print('no te puedes curar, ya tienes la vida hasta arriba')
    else:
        if desglose_number(ran_heal) == 1:
            user_choose_character.pv = user_choose_character.pv + 5
            print('te has curado 5 de vida' + f'(tu vida actual: {user_choose_character.pv})')

        elif desglose_number(ran_heal) == 2:
            print(f"fallaste la curacion (tu vida actual: {user_choose_character.pv})")

        elif desglose_number(ran_heal) == 3:
            user_choose_character.pv = user_choose_character.pv + 5
            print('haces un hechizo perfecto y te curas 10 de vida' + f'(tu vida actual: {user_choose_character.pv})')


def enemy_ia():
    global ran_command
    global user_choose_character
    global computer_character

    if desglose_number(ran_command) == 1:
        print('genial!, a fallado el ataque' + f'(tu vida actual: {user_choose_character.pv})')

    elif desglose_number(ran_command) == 2:
        print('Oh no! va a atacar ')

        user_choose_character.pv = user_choose_character.pv - computer_character.dmg

        if user_choose_character.pv <= 0:
            user_choose_character.xp = user_choose_character.xp / 2
            print(
                user_choose_character.name + f' Has Muerto (y has perdido la mitad de la xp (tu xp actual: {user_choose_character.xp}))')
            user_choose_character.pv = user_choose_character.pv + 10
            sys.exit(0)

        print(f'(tu vida actual: {user_choose_character.pv}) \n')

    elif desglose_number(ran_command) == 3:
        print('Oh no! va a atacar ')
        print('parece que sera golpe critico!')

        computer_character.dmg = computer_character.dmg + 2
        user_choose_character.pv = user_choose_character.pv - computer_character.dmg
        computer_character.dmg = computer_character.dmg - 2

        if user_choose_character.pv <= 0:
            user_choose_character.xp = user_choose_character.xp / 2
            print(
                user_choose_character.name + f' Has Muerto (y has perdido la mitad de la xp (tu xp actual: {user_choose_character.xp}))')
            user_choose_character.pv = user_choose_character.pv + 10
            sys.exit(0)

        print('uf! como dolio ese golpe critico ' + f'(tu vida actual: {user_choose_character.pv})')

    elif desglose_number(ran_command) == 4:
        print('parece que esta distraido')

    else:
        print(f"{computer_character.name} se esta replanteando su vida y como ha acabdo peleando con tigo")


def user_player_flee():
    global user_choose_character
    global computer_character
    global ran_heal
    ran_heal = random.sample(you_random_heal, 1)
    print("decides huir...")

    if desglose_number(ran_heal) == 1:
        print("escapaste exitosamente")
        sys.exit(0)

    elif desglose_number(ran_heal) == 2:
        user_choose_character.pv = user_choose_character.pv - computer_character.dmg
        print("consigues uir pero te llevas un golpe antes de escapar " + f'(tu vida actual: {user_choose_character.pv})')
        sys.exit(0)

    elif desglose_number(ran_heal) == 3:
        print(f"no has conseguido huir, y {computer_character.name} va atacar")
        enemy_ia()


computer_player()
