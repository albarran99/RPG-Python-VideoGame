import random
import sys
import time
from tkinter import Tk, PanedWindow, Button, BOTTOM, RAISED, ttk, TOP, LEFT, RIGHT, Label
import tkinter as tk

from pojos.character import Character
from title_main import real_chara

attack_list = {
                'arañazo': 4,
                'placaje': 4,
                'corte afilado': 4,
                'barrido': 4,
              }

character_1 = Character('salary-man', 1, 0, 20, 4, attack_list)
character_2 = Character('vezon', 1, 0, 20, 4, attack_list)
character_3 = Character('rathalos', 1, 0, 20, 4, attack_list)
character_4 = Character('zinogre', 1, 0, 20, 4, attack_list)
character_5 = Character('vezok', 1, 0, 20, 4, attack_list)

window = None
player_live = None
enemy_live = None
battle_dialogs = None
commands_panel = None

user_choose_character = real_chara

computer_character = None

number_not_repeat = [1, 2, 3, 4]
ran_command = random.sample(number_not_repeat, 1)

you_random_heal = [1, 2, 3]
ran_heal = random.sample(you_random_heal, 1)


def battle_main():
    global window
    global player_live
    global enemy_live
    global computer_character
    global battle_dialogs
    global commands_panel

    window = Tk()
    window.title("Fantastica y los multiples reinos")
    window.geometry('620x125')

    window.configure(bg='lightgray')

    ico = tk.PhotoImage(file='./doge.png')
    window.wm_iconphoto(True, ico)

    window.eval('tk::PlaceWindow . center')

    enemy_bar_live = PanedWindow()
    enemy_bar_live.grid(row=2, column=2)

    player_bar_live = PanedWindow()
    player_bar_live.grid(row=2, column=0)
    # spritres_panel = PanedWindow()
    # spritres_panel.grid(row=1, column=2)

    commands_panel = PanedWindow()

    player_name = Label(text=f'lvl:{user_choose_character.lvl} {user_choose_character.name}', bg='lightgray')
    player_name.grid(row=1, column=0)

    player_live = ttk.Progressbar(player_bar_live)
    value_player_live = 20
    player_live['value'] = 20

    player_style_bar = ttk.Style()
    player_style_bar.configure("green.Horizontal.TProgressbar", foreground='green', background='green')

    enemy_style_bar = ttk.Style()
    enemy_style_bar.configure("red.Horizontal.TProgressbar", foreground='red', background='red')

    enemy_style_bar = ttk.Style()
    enemy_style_bar.configure("yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')

    player_live.configure(maximum=value_player_live)
    player_live.grid(rows=1, column=2)

    enemy_name = Label(text=f'lvl:{computer_character.lvl} {computer_character.name}', bg='lightgray')
    enemy_name.grid(row=1, column=2)

    enemy_live = ttk.Progressbar(enemy_bar_live)
    enemy_live.grid(row=1, column=2)

    value_enemy_live = 20
    enemy_live['value'] = 20

    enemy_live.configure(maximum=value_enemy_live)

    enemy_bar_live.add(enemy_live)
    player_bar_live.add(player_live)

    enemy_bar_live.configure(relief=RAISED)
    player_bar_live.configure(relief=RAISED)

    commands_panel.configure(relief=RAISED)
    commands_panel.grid(row=5, column=1)

    frame_text_panel = PanedWindow()
    battle_dialogs = Label(frame_text_panel, text=f'Te has topado con un {computer_character.name} salvaje',
                           bg='lightgray')

    battle_dialogs.configure(width=50, height=3, font=("Courier", 10))

    frame_text_panel.add(battle_dialogs)
    frame_text_panel.grid(row=4, column=1)

    figth_button = Button(commands_panel, text="Luchar", command=enemy_dodge)
    figth_button.grid(row=0, column=1)

    heal_button = Button(commands_panel, text="Curar", command=heal_user_player)
    heal_button.grid(row=0, column=2)

    flee_button = Button(commands_panel, text="Huir", command=user_player_flee)
    flee_button.grid(row=0, column=3)

    commands_panel.add(figth_button)
    commands_panel.add(heal_button)
    commands_panel.add(flee_button)

    window.mainloop()


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
    global enemy_live
    global battle_dialogs
    global commands_panel

    commands_panel.grid_forget()

    ran_command = random.sample(number_not_repeat, 1)

    if desglose_number(ran_command) == 1:
        print(f"{user_choose_character.name} ataca!")

        time.sleep(2)
        battle_dialogs.config(text=f'{user_choose_character.name} ataca!!')
        battle_dialogs.update()

        computer_character.pv = computer_character.pv - user_choose_character.dmg

        if computer_character.pv <= 0:
            print(computer_character.name + ' Ha sido derrotado' + f'(tu vida actual: {user_choose_character.pv}) \n')

            time.sleep(2)
            battle_dialogs.config(text=f'{computer_character.name} Ha sido derrotado')
            battle_dialogs.update()

            user_choose_character.xp = user_choose_character.xp + 30
            print("Has ganado " + str(30) + f' de experiencia, experiencia actual es: {user_choose_character.xp}')

            time.sleep(2)
            battle_dialogs.config(text=f'Has ganado {str(30)} de experiencia')
            battle_dialogs.update()

            ran_command = random.sample(number_not_repeat, 1)
            chose_character_computer()
            user_choose_character.pv = user_choose_character.pv + 10

            time.sleep(10)
            sys.exit(0)

        print('Uff!, eso dolió ahora ' + computer_character.name + ' le queda de vida ' + str(
            computer_character.pv) + f'(tu vida actual: {user_choose_character.pv})\n')

        battle_dialogs.config(text=f'Uff!, eso le dolio a {computer_character.name}')
        battle_dialogs.update()

        enemy_live['value'] -= user_choose_character.dmg
        enemy_live.update()

        ran_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()

    elif desglose_number(ran_command) == 2:
        print('vaya! esquivo tú ataque\n')

        battle_dialogs.config(text='vaya! esquivo tú ataque')
        battle_dialogs.update()
        ran_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()

    elif desglose_number(ran_command) == 3:
        print('Parece que ' + computer_character.name + " esta a muy distraido y recive un golpe critico\n")

        time.sleep(2)
        battle_dialogs.config(
            text=f'Parece que {computer_character.name} \nesta a muy distraido y recive un golpe critico')
        battle_dialogs.update()

        user_choose_character.dmg = user_choose_character.dmg + 2

        computer_character.pv = computer_character.pv - user_choose_character.dmg

        if computer_character.pv <= 0:
            print(computer_character.name + ' Ha sido derrotado' + f'(tu vida actual: {user_choose_character.pv}) \n')

            time.sleep(2)
            battle_dialogs.config(text=f'{computer_character.name} Ha sido derrotado')
            battle_dialogs.update()

            user_choose_character.xp = user_choose_character.xp + 30
            print("Has ganado " + str(30) + f' de experiencia, experiencia actual es: {user_choose_character.xp}\n')

            time.sleep(2)
            battle_dialogs.config(text=f"Has ganado {str(30)}")
            battle_dialogs.update()

            time.sleep(2)
            battle_dialogs.config(text=f'de experiencia, experiencia actual es: {user_choose_character.xp}')
            battle_dialogs.update()

            ran_command = random.sample(number_not_repeat, 1)
            chose_character_computer()
            user_choose_character.pv = user_choose_character.pv + 10

            time.sleep(10)
            sys.exit(0)

        print(
            "dios mio, eso a sido un terrible golpe a " + computer_character.name + f" le queda de vida {computer_character.pv} " + '\n')

        time.sleep(2)
        battle_dialogs.config(text=f"dios mio, eso a sido un \nterrible golpe para {computer_character.name}")
        battle_dialogs.update()

        enemy_live['value'] -= user_choose_character.dmg
        enemy_live.update()

        user_choose_character.dmg = user_choose_character.dmg - 2

        ran_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()

    elif desglose_number(ran_command) == 4:
        print('tu ataque se perdio!')
        battle_dialogs.config(text='tu ataque se perdio!')
        battle_dialogs.update()

        ran_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()


def enemy_ia():
    global ran_command
    global user_choose_character
    global computer_character
    global player_live
    global battle_dialogs
    global commands_panel

    ran_command = random.sample(number_not_repeat, 1)

    if desglose_number(ran_command) == 1:
        time.sleep(4)
        print('genial!, a fallado al atacar' + f'(tu vida actual: {user_choose_character.pv})\n')

        time.sleep(2)
        battle_dialogs.config(text='genial!, a fallado al atacar')
        battle_dialogs.update()

        commands_panel.grid(row=5, column=1)

    elif desglose_number(ran_command) == 2:
        time.sleep(4)
        print('Oh no! va a atacar\n')

        battle_dialogs.config(text='Oh no! va a atacar')
        battle_dialogs.update()

        user_choose_character.pv = user_choose_character.pv - computer_character.dmg

        if user_choose_character.pv <= 0:
            time.sleep(4)

            player_live['value'] -= computer_character.dmg
            player_live.update()

            user_choose_character.xp = user_choose_character.xp / 2
            print(
                user_choose_character.name + f' Has Muerto (y has perdido la mitad de la xp (tu xp actual: \n{user_choose_character.xp}))')

            battle_dialogs.config(text=f'{user_choose_character.name} Has Muerto')
            battle_dialogs.update()

            battle_dialogs.config(text=f'y has perdido la mitad de la xp (tu xp actual: {user_choose_character.xp})')
            battle_dialogs.update()

            user_choose_character.pv = user_choose_character.pv + 10
            time.sleep(10)
            battle_dialogs.bind('<Button-3>', user_close_windows)

        print(f'(tu vida actual: {user_choose_character.pv}) \n')

        time.sleep(2)
        battle_dialogs.config(text='ay eso dolio!!')
        battle_dialogs.update()

        player_live['value'] -= computer_character.dmg
        player_live.update()

        commands_panel.grid(row=5, column=1)

    elif desglose_number(ran_command) == 3:
        time.sleep(4)
        print('Oh no! va a atacar')

        time.sleep(2)
        battle_dialogs.config(text='Oh no! va a atacar')
        battle_dialogs.update()

        print('parece que sera golpe critico!')

        time.sleep(2)
        battle_dialogs.config(text='parece que sera golpe critico!')
        battle_dialogs.update()

        computer_character.dmg = computer_character.dmg + 2

        user_choose_character.pv = user_choose_character.pv - computer_character.dmg

        if user_choose_character.pv <= 0:
            time.sleep(4)

            player_live['value'] -= computer_character.dmg
            player_live.update()

            user_choose_character.xp = user_choose_character.xp / 2
            print(
                user_choose_character.name + f' Has Muerto (y has perdido la mitad de la xp \n(tu xp actual: {user_choose_character.xp}))')

            time.sleep(2)
            battle_dialogs.config(text=user_choose_character.name + f' Has Muerto')
            battle_dialogs.update()

            time.sleep(2)
            battle_dialogs.config(text=f'y has perdido la mitad de la xp (tu xp actual: {user_choose_character.xp})')
            battle_dialogs.update()

            user_choose_character.pv = user_choose_character.pv + 10
            time.sleep(10)
            sys.exit(0)

        print('uf! como dolio ese golpe critico ' + f'(tu vida actual: {user_choose_character.pv})\n')

        time.sleep(2)
        battle_dialogs.config(text='uf! como dolio ese golpe critico')
        battle_dialogs.update()

        player_live['value'] -= computer_character.dmg
        player_live.update()

        computer_character.dmg = computer_character.dmg - 2

        commands_panel.grid(row=5, column=1)

    elif desglose_number(ran_command) == 4:
        time.sleep(4)
        print('parece que esta distraido\n')

        time.sleep(2)
        battle_dialogs.config(text='parece que esta distraido')
        battle_dialogs.update()

        commands_panel.grid(row=5, column=1)


def user_player_flee():
    global user_choose_character
    global computer_character
    global ran_heal
    global battle_dialogs
    ran_heal = random.sample(you_random_heal, 1)
    print("decides huir...")
    battle_dialogs.config(text="decides huir...")
    battle_dialogs.update()

    if desglose_number(ran_heal) == 1:
        print("escapaste exitosamente")

        time.sleep(2)
        battle_dialogs.config(text="escapaste exitosamente")
        battle_dialogs.update()

        sys.exit(0)

    elif desglose_number(ran_heal) == 2:
        user_choose_character.pv = user_choose_character.pv - computer_character.dmg
        print(
            "consigues uir pero te llevas un golpe antes de escapar " + f'(tu vida actual: {user_choose_character.pv})')

        time.sleep(2)
        battle_dialogs.config(text="consigues uir pero te llevas un golpe antes de escapar ")
        battle_dialogs.update()

        time.sleep(2)
        sys.exit(0)

    elif desglose_number(ran_heal) == 3:
        print(f"no has conseguido huir, y {computer_character.name} va atacar")

        time.sleep(2)
        battle_dialogs.config(text=f"no has conseguido huir, y {computer_character.name} va atacar")
        battle_dialogs.update()

        time.sleep(2)
        enemy_ia()


def heal_user_player():
    global ran_heal
    global player_live
    global battle_dialogs
    global ran_command
    global commands_panel

    commands_panel.grid_forget()

    ran_command = random.sample(number_not_repeat, 1)

    print(user_choose_character.name + ' se va a curar la vida' + f'(tu vida actual: {user_choose_character.pv})')

    battle_dialogs.config(text=f'{user_choose_character.name} se va a curar la vida')
    battle_dialogs.update()

    ran_heal = random.sample(you_random_heal, 1)

    if user_choose_character.pv == 20:
        print('no te puedes curar, ya tienes la vida hasta arriba')

        battle_dialogs.config(text='no te puedes curar, ya tienes la vida hasta arriba')
        battle_dialogs.update()

        ran_command = random.sample(number_not_repeat, 1)
        enemy_ia()

    else:
        if desglose_number(ran_heal) == 1:
            user_choose_character.pv = user_choose_character.pv + 5
            print('te has curado 6 de vida' + f'(tu vida actual: {user_choose_character.pv})')

            battle_dialogs.config(text='te has curado 6 de vida, genial!')
            battle_dialogs.update()

            player_live['value'] += 6

            ran_command = random.sample(number_not_repeat, 1)
            enemy_ia()

        elif desglose_number(ran_heal) == 2:
            print(f"fallaste la curacion (tu vida actual: {user_choose_character.pv})")

            battle_dialogs.config(text="fallaste la curacion")
            battle_dialogs.update()

            ran_command = random.sample(number_not_repeat, 1)
            enemy_ia()

        elif desglose_number(ran_heal) == 3:
            user_choose_character.pv = user_choose_character.pv + 10
            print('haces un hechizo perfecto y te curas 10 de vida' + f'(tu vida actual: {user_choose_character.pv})')

            battle_dialogs.config(text='haces un hechizo perfecto y te curas 10 de vida')
            battle_dialogs.update()

            player_live['value'] += 10

            if user_choose_character.pv > 20:
                player_live['value'] = 20

            ran_command = random.sample(number_not_repeat, 1)
            enemy_ia()


def user_close_windows():
    global window
    window.destroy()


if __name__ == '__main__':
    computer_player()
    battle_main()
