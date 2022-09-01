import os
import random
from tkinter import Tk, PanedWindow, Button, BOTTOM, RAISED, ttk, TOP, LEFT, RIGHT, Label, VERTICAL, CENTER, END
import tkinter as tk

import battle_escene
from pojos.Animal import Monsters
from pojos.Non_organic import Bionicle
from pojos.Person import Humans

computer_character = None

real_chara = None

character_found = None

user_choose_character = None

window = None

loads_files = None

win_2 = None

number_not_repeat = [1, 2, 3, 4]
ran_command = random.sample(number_not_repeat, 1)

character_1 = Humans('salary-man', 1, 0, 20, 4)
character_2 = Bionicle('vezon', 1, 0, 20, 4)
character_3 = Monsters('rathalos', 1, 0, 20, 4)
character_4 = Monsters('zinogre', 1, 0, 20, 4)
character_5 = Bionicle('vezok', 1, 0, 20, 4)


def main():
    global window
    window = Tk()
    window.title("Fantastica y los multiples reinos")

    bg = tk.PhotoImage(file='background.png')

    window.geometry('400x300')

    window.configure(bg='grey')

    background_label = Label(window, image=bg)
    background_label.place(x=0, y=0)

    ico = tk.PhotoImage(file='./doge.png')
    window.wm_iconphoto(True, ico)

    title_option = PanedWindow(orient=VERTICAL)
    title_option.pack(side=BOTTOM, pady=50)

    title_text = Label(text='Bienvenido a Fantasia. \ny los multiples reinos', background='#a5d6a7')
    title_text.pack(side=TOP)

    btn_start = Button(text='comenzar', background='#a5d6a7', command=create_new_game)
    btn_start.pack(pady=50)

    btn_continue = Button(text='continuar', background='#a5d6a7', command=load_game)
    btn_continue.pack(pady=50)

    btn_exit = Button(text='salir a windows', background='#a5d6a7', command=user_close_windows)
    btn_exit.pack(pady=50)

    title_option.add(btn_start)
    title_option.add(btn_continue)
    title_option.add(btn_exit)

    window.eval('tk::PlaceWindow . center')

    window.mainloop()


def create_new_game():
    global window
    win_3 = tk.Toplevel(window)
    win_3.geometry('400x300')

    choose_character_1 = Button(win_3, text=f'{character_1.name}', command=choose_chara_1)
    choose_character_1.grid(row=5, column=1)

    info_chararcter_1 = Label(win_3, text=f'{character_1.name}\n{character_1.pv}\n{character_1.xp}\n{character_1.lvl}')
    info_chararcter_1.grid(row=4, column=1)

    choose_character_2 = Button(win_3, text=f'{character_2.name}', command=choose_chara_2)
    choose_character_2.grid(row=5, column=2)

    info_chararcter_2 = Label(win_3, text=f'{character_2.name}\n{character_2.pv}\n{character_2.xp}\n{character_2.lvl}')
    info_chararcter_2.grid(row=4, column=2)

    choose_character_3 = Button(win_3, text=f'{character_3.name}', command=choose_chara_3)
    choose_character_3.grid(row=5, column=3)

    info_chararcter_3 = Label(win_3, text=f'{character_3.name}\n{character_3.pv}\n{character_3.xp}\n{character_3.lvl}')
    info_chararcter_3.grid(row=4, column=3)

    choose_character_4 = Button(win_3, text=f'{character_4.name}', command=choose_chara_4)
    choose_character_4.grid(row=5, column=4)

    info_chararcter_4 = Label(win_3, text=f'{character_4.name}\n{character_4.pv}\n{character_4.xp}\n{character_4.lvl}')
    info_chararcter_4.grid(row=4, column=4)

    choose_character_5 = Button(win_3, text=f'{character_5.name}', command=choose_chara_5)
    choose_character_5.grid(row=5, column=5)

    info_chararcter_5 = Label(win_3, text=f'{character_5.name}\n{character_5.pv}\n{character_5.xp}\n{character_5.lvl}')
    info_chararcter_5.grid(row=4, column=5)


def load_game():
    global window
    global loads_files
    global real_chara
    global win_2

    win_2 = Tk()
    bg = tk.PhotoImage(file='win2_bg.png')
    win_2.geometry('400x300')
    background_label = Label(win_2, image=bg)
    background_label.place(x=0, y=0)

    path = os.path.dirname(os.path.realpath(__file__)) + '/saves/'
    list_saves = os.listdir(path)
    for save_name in list_saves:
        print(f"tus partidas: {save_name}")
        loads_files = Button(win_2, text=save_name, command=download_game)
        loads_files.pack()
    win_2.mainloop()


def choose_chara_1():
    global real_chara
    real_chara = character_1


def choose_chara_2():
    global real_chara
    real_chara = character_2


def choose_chara_3():
    global real_chara
    real_chara = character_3


def choose_chara_4():
    global real_chara
    real_chara = character_4


def choose_chara_5():
    global real_chara
    real_chara = character_5


def user_close_windows():
    global win_2
    win_2.destroy()


def download_game():
    global real_chara
    global loads_files
    global window
    global win_2
    stats = None
    user_close_windows()
    try:
        path = os.path.dirname(os.path.realpath(__file__)) + '/saves/'
        real_path = path + loads_files['text']
        stats = open(real_path, 'r')
    except FileNotFoundError:
        print("ese nombre de archivo de guardado no existe")

    inf_name = stats.readline(-1)

    lvl_num = stats.readline(-2).strip('\n')

    px_num = stats.readline(-3).strip('\n')

    pv_num = stats.readline(-4).strip('\n')

    dmg_num = stats.readline(-5).strip('\n')
    load_chara = find_a_character(inf_name.strip('\n'))
    real_chara = load_chara.__init__(inf_name, int(lvl_num), int(px_num), int(pv_num), int(dmg_num))
    user_close_windows()
    battle_escene.main()


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


def user_close_windows():
    global window
    window.destroy()


if __name__ == '__main__':
    main()
