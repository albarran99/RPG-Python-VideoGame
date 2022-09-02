import os
import random
import sys

from pojos.character import say_hello, Character, level_up

application_path = os.path.dirname(sys.executable)

attack_list = ['arañazo',
               'placaje',
               'corte afilado',
               'barrido']

character_1 = Character('salary-man', 1, 0, 100, 40, attack_list)
character_2 = Character('vezon', 1, 0, 100, 40, attack_list)
character_3 = Character('rathalos', 1, 0, 100, 40, attack_list)
character_4 = Character('zinogre', 1, 0, 100, 40, attack_list)
character_5 = Character('vezok', 1, 0, 100, 40, attack_list)

number_not_repeat = [1, 2, 3, 4]
you_random_heal = [1, 2, 3]
ran_command = random.sample(number_not_repeat, 1)
ran_heal = random.sample(you_random_heal, 1)

user_choose_character = None

character_found = None

user_character = None

real_chara = None

computer_character = None

is_computer_character = None


def characters_info():
    say_hello(character_1)
    print("\n")
    say_hello(character_2)
    print("\n")
    say_hello(character_3)
    print("\n")
    say_hello(character_4)
    print("\n")
    say_hello(character_5)
    print("\n")


def save_game(character_info):
    global user_choose_character
    save_path = os.path.dirname(os.path.realpath(__file__)) + '/saves/'
    print("cargando espera un momento por favor...")
    user_text = input("Escribe el nombre de la partida...\n")
    path = save_path + user_text
    file_to_write = open(path, 'w')
    character_info = f'{user_choose_character.name}\n'\
                    f'{user_choose_character.lvl}\n'\
                    f'{user_choose_character.xp}\n'\
                    f'{user_choose_character.pv}\n'\
                    f'{user_choose_character.dmg}\n'\
                    f'{user_choose_character.attack_list[0]}\n'\
                    f'{user_choose_character.attack_list[1]}\n'\
                    f'{user_choose_character.attack_list[2]}\n'\
                    f'{user_choose_character.attack_list[3]}\n'\
                                                                                                                                                                                            f'{user_choose_character.attack_list}'
    print("guardando espere por favor")
    file_to_write.write(character_info)
    file_to_write.close()
    print("guardado con exito")


def show_saves():
    path = os.path.dirname(os.path.realpath(__file__)) + '/saves/'
    list_saves = os.listdir(path)
    print("tus partidas: ")
    for save_name in list_saves:
        print(f'{save_name}')


def load_file():
    global real_chara
    list_attk = []
    path = os.path.dirname(os.path.realpath(__file__)) + '/saves/'
    stats = None
    show_saves()
    try:
        user_save = input('-Elige partida-\n')
        real_path = path + user_save
        stats = open(real_path, 'r')
    except FileNotFoundError:
        print("ese nombre de archivo de guardado no existe")
        user_save = input('-Elige partida-\n')

    inf_name = stats.readline(-1)

    lvl_num = stats.readline(-2).strip('\n')

    px_num = stats.readline(-3).strip('\n')

    pv_num = stats.readline(-4).strip('\n')

    dmg_num = stats.readline(-5).strip('\n')

    attack_one = stats.readline(-6).strip('\n')

    attack_two = stats.readline(-7).strip('\n')

    attack_three = stats.readline(-8).strip('\n')

    attack_four = stats.readline(-9).strip('\n')

    list_attk.append(attack_one)

    list_attk.append(attack_two)

    list_attk.append(attack_three)

    list_attk.append(attack_four)

    load_chara = find_a_character(inf_name.strip('\n'))
    real_chara = load_chara.__init__(inf_name, int(lvl_num), int(px_num), int(pv_num), int(dmg_num), list_attk)
    computer_player()

    return real_chara == user_choose_character


def find_a_character(name):
    global character_found, user_choose_character

    if name == 'salary-man':
        character_found = character_1
        user_choose_character = character_1

    elif name == 'vezon':
        character_found = character_2
        user_choose_character = character_2

    elif name == 'rathalos':
        character_found = character_3
        user_choose_character = character_3

    elif name == 'zinogre':
        character_found = character_4
        user_choose_character = character_4

    elif name == 'vezok':
        character_found = character_5
        user_choose_character = character_5

    return character_found


def computer_player():
    global is_computer_character
    is_computer_character = chose_character_computer()
    print('Tu rival sera: ' + is_computer_character.name)


def options_menu():
    print('por favor escriba un comando valido:\n'
          '- atacar <==> hit\n'
          '- curarte <==> heal\n'
          '- habilidad <==> skill\n'
          '- magia <==> spell\n'
          '- guardar <==> save\n'
          '- menu de pausa <==> stats\n'
          '- salir del programa <==> q')

    user_command = input()
    user_options(user_command)

    return user_command


def show_different_attacks():
    print('-Tus ataques-\n')
    for attack in attack_list:
        print(f'{attack}')


def user_options(command):
    global ran_heal
    global user_damage

    while command != 'q':
        if command == 'hit':
            show_different_attacks()
            user_choice_attack = input('elige un ataque')

            if user_choice_attack == attack_list[0]:
                print(f"vas a hacer {user_choice_attack}")

            elif user_choice_attack == attack_list[1]:
                print(f"vas a hacer {user_choice_attack}")

            elif user_choice_attack == attack_list[2]:
                print(f"vas a hacer {user_choice_attack}")

            elif user_choice_attack == attack_list[3]:
                print(f"vas a hacer {user_choice_attack}")

            else:
                print("no te he entendido vuelve a escribir el ataque")
                user_choice_attack = input('elige un ataque')

            enemy_dodge()
            options_menu()
            command = input()

        elif command == 'heal':
            print(user_choose_character.name + ' se va a curar la vida' + f'(tu vida actual: {user_choose_character.pv})')
            ran_heal = random.sample(you_random_heal, 1)
            if user_choose_character.pv == 100:
                print('no te puedes curar, ya tienes la vida hasta arriba')
            else:
                if desglose_number(ran_heal) == 1:
                    user_choose_character.pv = user_choose_character.pv + 50
                    print('te has curado 50 de vida' + f'(tu vida actual: {user_choose_character.pv})')
                    if user_choose_character.pv > 100:
                        user_choose_character.pv = 100

                elif desglose_number(ran_heal) == 2:
                    print(f"fallaste la curacion (tu vida actual: {user_choose_character.pv})")

                elif desglose_number(ran_heal) == 3:
                    user_choose_character.pv = user_choose_character.pv + 80
                    print('haces un hechizo perfecto y te curas 80 de vida' + f'(tu vida actual: {user_choose_character.pv})')
                    if user_choose_character.pv > 100:
                        user_choose_character.pv = 100

            options_menu()
            command = input()

        elif command == 'save':
            player_character = how_are_you()
            save_game(player_character)
            options_menu()
            command = input()

        elif command == 'stats':
            say_hello(user_choose_character)
            options_menu()
            command = input()

    else:
        print('comando no valido')
        options_menu()
        command = input()


def run_game():
    tittle_menu()


def enemy_dodge():
    global ran_command
    global user_choose_character
    global is_computer_character

    if desglose_number(ran_command) == 1:
        is_computer_character.pv = is_computer_character.pv - user_choose_character.dmg

        if is_computer_character.pv <= 0:
            print(is_computer_character.name + ' Ha sido derrotado' + f'(tu vida actual: {user_choose_character.pv}) \n')
            user_choose_character.xp = user_choose_character.xp + 50
            print("Has ganado " + str(50) + f' de experiencia, experiencia actual es: {user_choose_character.xp}')
            level_up(user_choose_character)
            ran_command = random.sample(number_not_repeat, 1)
            chose_character_computer()
            user_choose_character.pv = user_choose_character.pv + 50
            if user_choose_character.pv > 100:
                user_choose_character.pv = 100
            options_menu()

        print('Uff!, eso dolió ahora ' + is_computer_character.name + ' le queda de vida ' + str(is_computer_character.pv) + f'(tu vida actual: {user_choose_character.pv})\n')

        ran_command = random.sample(number_not_repeat, 1)
        enemy_ia()

    elif desglose_number(ran_command) == 2:
        print('vaya! esquivo tú ataque')
        ran_command = random.sample(number_not_repeat, 1)
        enemy_ia()

    elif desglose_number(ran_command) == 3:
        print('Parece que ' + is_computer_character.name + " esta a muy distraido y recive un golpe critico")
        user_choose_character.dmg = user_choose_character.dmg + 2
        is_computer_character.pv = is_computer_character.pv - user_choose_character.dmg
        user_choose_character.dmg = user_choose_character.dmg - 2

        if is_computer_character.pv <= 0:
            print(is_computer_character.name + ' Ha sido derrotado' + f'(tu vida actual: {user_choose_character.pv}) \n')
            user_choose_character.xp = user_choose_character.xp + 50
            print("Has ganado " + str(50) + f' de experiencia, experiencia actual es: {user_choose_character.xp}')
            ran_command = random.sample(number_not_repeat, 1)
            level_up(user_choose_character)
            chose_character_computer()
            user_choose_character.pv = user_choose_character.pv + 50
            if user_choose_character.pv > 100:
                user_choose_character.pv = 100
            options_menu()

        print("dios mio, eso a sido un terrible golpe a " + is_computer_character.name + f" le queda de vida {is_computer_character.pv} " + '\n')
        ran_command = random.sample(number_not_repeat, 1)
        enemy_ia()

    elif desglose_number(ran_command) == 4:
        print('tu ataque se perdio!')
        ran_command = random.sample(number_not_repeat, 1)
        enemy_ia()

    else:
        print("los dos adversarios se miran fijamente")


def enemy_ia():
    global ran_command
    global user_choose_character
    global computer_character

    if desglose_number(ran_command) == 1:
        print('genial!, a fallado el ataque' + f'(tu vida actual: {user_choose_character.pv})')

    elif desglose_number(ran_command) == 2:
        print('Oh no! va a atacar ')

        user_choose_character.pv = user_choose_character.pv - is_computer_character.dmg

        if user_choose_character.pv <= 0:
            user_choose_character.xp = user_choose_character.xp / 2
            print(user_choose_character.name + f' Has Muerto (y has perdido la mitad de la xp (tu xp actual: {user_choose_character.xp}))')
            user_choose_character.pv = user_choose_character.pv + 50
            if user_choose_character.pv > 100:
                user_choose_character.pv = 100
            save_game(user_choose_character)
            tittle_menu()

        print(f'(tu vida actual: {user_choose_character.pv}) \n')

    elif desglose_number(ran_command) == 3:
        print('Oh no! va a atacar ')
        print('parece que sera golpe critico!')

        is_computer_character.dmg = is_computer_character.dmg + 2
        user_choose_character.pv = user_choose_character.pv - is_computer_character.dmg
        is_computer_character.dmg = is_computer_character.dmg - 2

        if user_choose_character.pv <= 0:
            user_choose_character.xp = user_choose_character.xp / 2
            print(user_choose_character.name + f' Has Muerto (y has perdido la mitad de la xp (tu xp actual: {user_choose_character.xp}))')
            user_choose_character.pv = user_choose_character.pv + 50
            if user_choose_character.pv > 100:
                user_choose_character.pv = 100
            save_game(user_choose_character)
            tittle_menu()

        print('uf! como dolio ese golpe critico ' + f'(tu vida actual: {user_choose_character.pv})')

    elif desglose_number(ran_command) == 4:
        print('parece que esta distraido')

    else:
        print(f"{is_computer_character.name} se esta replanteando su vida y como ha acabdo peleando con tigo")


def characters_menu():
    print('elige un personaje: \n'
          '1.''no disponible''\'\n'
          '2.vezon\n'
          '3.rathalos\n'
          '4.zinogre\n'
          '5.vezok')


def chose_character_user():
    global user_choose_character
    global user_character

    if user_choose_character == "salary-man" or user_choose_character == "Saytama":
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


def how_are_you():
    global user_choose_character
    global user_character

    if user_choose_character == "salary-man" or user_choose_character == "Salary-man":
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


def desglose_number(num_list: list):
    global num

    for num in num_list:
        return num


def new_game_menu():
    global user_choose_character

    characters_info()

    characters_menu()

    print('Elije personaje')

    user_choose_character = input()

    print('has elejido a ' + user_choose_character)

    user_choose_character = chose_character_user()

    return user_choose_character


def tittle_menu():
    print("Fantastica y los multiples reinos")
    print("Opciones: \n"
          "-Empezar-\n"
          "-continuar-\n"
          "-salir-")
    user_command = input()
    if user_command == 'Empezar':
        new_game_menu()
        command_user = options_menu()
        user_options(command_user)

    elif user_command == 'continuar':
        load_file()
        options_menu()

    elif user_command == 'salir':
        sys.exit()

    else:
        print("comando no valido")
        user_command = input()


if __name__ == '__main__':
    run_game()
