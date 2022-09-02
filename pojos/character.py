from typing import Any


class Character:
    def __init__(self, name: str, lvl: int, xp: int, pv: int, dmg: int, attack_list: list) -> None:
        self.name = name
        self.lvl = lvl
        self.xp = xp
        self.pv = pv
        self.dmg = dmg
        self.attack_list = attack_list

    def set_pv(self, x):
        self.pv = x

    def set_xp(self, x):
        self.xp = x

    def set_dmg(self, x):
        self.dmg = x

    def __str__(self) -> str:
        return super().__str__()

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)


def xp_achieved(chara, xp):
    chara.xp = xp + chara.xp


def lvl_2(chara):
    if chara.xp >= 100:
        chara.lvl = chara.lvl + 1
        print("¡subida!" + '\n'
              f'sube +10 = {chara.pv}\n'
              f'sube +5 = {chara.dmg}')
        chara.xp = 0
        print(f"¡Bien, tu {chara.name} a subido de nivel!, ahora es {chara.lvl}")
    else:
        pass


def lvl_3(chara):
    if chara.xp >= 200:
        chara.lvl = chara.lvl + 1
        print("¡subida!" + '\n'
              f'sube +5 = {chara.pv}\n'
              f'sube +10 = {chara.dmg}')
        chara.xp = 0
        print(f"¡Bien, tu {chara.name} a subido de nivel!, ahora es {chara.lvl}")
    else:
        pass


def lvl_4(chara):
    if chara.xp >= 250:
        chara.lvl = chara.lvl + 1
        print("¡subida!" + '\n'
              f'sube +15 = {chara.pv}\n'
              f'sube +10 = {chara.dmg}')
        chara.xp = 0
        print(f"¡Bien, tu {chara.name} a subido de nivel!, ahora es {chara.lvl}")
    else:
        pass


def lvl_5(chara):
    if chara.xp >= 300:
        chara.lvl = chara.lvl + 1
        print("¡subida!" + '\n'
              f'sube +20 = {chara.pv}\n'
              f'sube +10 = {chara.dmg}')
        chara.xp = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_6(chara):
    if chara.xp >= 350:
        chara.lvl = chara.lvl + 1
        print("¡subida!" + '\n'
              f'sube +20 = {chara.pv}\n'
              f'sube +20 = {chara.dmg}')
        chara.xp = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_7(chara):
    if chara.xp >= 400:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +30 = {chara.pv}\n'
              f'sube +20 = {chara.dmg}')
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_8(chara):
    if chara.xp >= 450:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +20 = {chara.pv}\n'
              f'sube +30 = {chara.dmg}')
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_9(chara):
    if chara.xp >= 500:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +30 = {chara.pv}\n'
              f'sube +30 = {chara.dmg}')
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_10(chara):
    if chara.xp >= 555:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +55 = {chara.pv}\n'
              f'sube +55 = {chara.dmg}')
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_11(chara):
    if chara.xp >= 600:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +40 = {chara.pv}\n'
              f'sube +30 = {chara.dmg}')
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_12(chara):
    if chara.xp >= 650:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +40 = {chara.pv}\n'
              f'sube +40 = {chara.dmg}')
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_13(chara):
    if chara.xp >= 700:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +50 = {chara.pv}\n'
              f'sube +40 = {chara.dmg}')
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_14(chara):
    if chara.xp >= 727:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +50 = {chara.dmg}')
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_15(chara):
    if chara.xp >= 777:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 60
        chara.dmg = chara.dmg + 60
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_16(chara):
    if chara.xp >= 800:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 50
        chara.dmg = chara.dmg + 40
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_17(chara):
    if chara.xp >= 850:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 50
        chara.dmg = chara.dmg + 40
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_18(chara):
    if chara.xp >= 900:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 70
        chara.dmg = chara.dmg + 70
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_19(chara):
    if chara.xp >= 999:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 50
        chara.dmg = chara.dmg + 40
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_20(chara):
    if chara.xp >= 1080:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 90
        chara.dmg = chara.dmg + 80
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_21(chara):
    if chara.xp >= 1500:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 100
        chara.dmg = chara.dmg + 90
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_22(chara):
    if chara.xp >= 2000:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 70
        chara.dmg = chara.dmg + 80
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_23(chara):
    if chara.xp >= 2500:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 80
        chara.dmg = chara.dmg + 80
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_24(chara):
    if chara.xp >= 2500:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 60
        chara.dmg = chara.dmg + 70
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_25(chara):
    if chara.xp >= 3000:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 90
        chara.dmg = chara.dmg + 50
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_26(chara):
    if chara.xp >= 3500:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 89
        chara.dmg = chara.dmg + 69
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_27(chara):
    if chara.xp >= 4000:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 79
        chara.dmg = chara.dmg + 80
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_28(chara):
    if chara.xp >= 4500:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 90
        chara.dmg = chara.dmg + 80
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_29(chara):
    if chara.xp >= 5000:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 80
        chara.dmg = chara.dmg + 80
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_30(chara):
    if chara.xp >= 5500:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 70
        chara.dmg = chara.dmg + 70
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_31(chara):
    if chara.xp >= 6000:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 80
        chara.dmg = chara.dmg + 70
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_32(chara):
    if chara.xp >= 6500:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 50
        chara.dmg = chara.dmg + 70
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_33(chara):
    if chara.xp >= 7000:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 60
        chara.dmg = chara.dmg + 80
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def lvl_34(chara):
    if chara.xp >= 7500:
        chara.lvl = chara.lvl + 1
        print("¡Subida!\n"
              f'sube +60 = {chara.pv}\n'
              f'sube +60 = {chara.dmg}')
        chara.pv = chara.pv + 70
        chara.dmg = chara.dmg + 80
        chara.XP = 0
        print(f'¡Bien, ahora tu {chara.name} a subido de nivel!, su nivel actual es {chara.lvl}')
    else:
        pass


def level_up(chara):
    if lvl_2(chara):
        chara.pv = chara.pv + 10
        chara.dmg = chara.dmg + 5

    if lvl_3(chara):
        chara.pv = chara.pv + 5
        chara.dmg = chara.dmg + 10

    if lvl_4(chara):
        chara.pv = chara.pv + 15
        chara.dmg = chara.dmg + 10

    if lvl_5(chara):
        chara.pv = chara.pv + 20
        chara.dmg = chara.dmg + 10

    if lvl_6(chara):
        chara.pv = chara.pv + 20
        chara.dmg = chara.dmg + 10

    if lvl_7(chara):
        chara.pv = chara.pv + 30
        chara.dmg = chara.dmg + 20

    if lvl_8(chara):
        chara.pv = chara.pv + 20
        chara.dmg = chara.dmg + 30

    if lvl_9(chara):
        chara.pv = chara.pv + 30
        chara.dmg = chara.dmg + 30

    if lvl_10(chara):
        chara.pv = chara.pv + 55
        chara.dmg = chara.dmg + 55

    if lvl_11(chara):
        chara.pv = chara.pv + 40
        chara.dmg = chara.dmg + 30

    if lvl_12(chara):
        chara.pv = chara.pv + 40
        chara.dmg = chara.dmg + 40

    if lvl_13(chara):
        chara.pv = chara.pv + 50
        chara.dmg = chara.dmg + 40

    if lvl_14(chara):
        chara.pv = chara.pv + 60
        chara.dmg = chara.dmg + 50

    if lvl_15(chara):
        chara.pv = chara.pv + 60
        chara.dmg = chara.dmg + 60

    if lvl_16(chara):
        chara.pv = chara.pv + 40
        chara.dmg = chara.dmg + 50

    if lvl_17(chara):
        chara.pv = chara.pv + 50
        chara.dmg = chara.dmg + 40

    if lvl_18(chara):
        chara.pv = chara.pv + 70
        chara.dmg = chara.dmg + 70

    if lvl_19(chara):
        chara.pv = chara.pv + 50
        chara.dmg = chara.dmg + 40

    if lvl_20(chara):
        chara.pv = chara.pv + 90
        chara.dmg = chara.dmg + 80

    if lvl_21(chara):
        chara.pv = chara.pv + 100
        chara.dmg = chara.dmg + 90

    if lvl_22(chara):
        chara.pv = chara.pv + 70
        chara.dmg = chara.dmg + 80

    if lvl_23(chara):
        chara.pv = chara.pv + 80
        chara.dmg = chara.dmg + 80

    if lvl_24(chara):
        chara.pv = chara.pv + 60
        chara.dmg = chara.dmg + 70

    if lvl_25(chara):
        chara.pv = chara.pv + 90
        chara.dmg = chara.dmg + 50

    if lvl_26(chara):
        chara.pv = chara.pv + 89
        chara.dmg = chara.dmg + 69

    if lvl_27(chara):
        chara.pv = chara.pv + 79
        chara.dmg = chara.dmg + 80

    if lvl_28(chara):
        chara.pv = chara.pv + 90
        chara.dmg = chara.dmg + 80

    if lvl_29(chara):
        chara.pv = chara.pv + 80
        chara.dmg = chara.dmg + 80

    if lvl_30(chara):
        chara.pv = chara.pv + 70
        chara.dmg = chara.dmg + 70

def say_hello(chara):
    print(
          f'Hola mi nombre es {chara.name}\n'
          f'Tengo {str(chara.lvl)} nivel\n'
          f'la experiencia acumulada es {str(chara.xp)}\n'
          f'mi vida actual es de {str(chara.pv)}\n'
          f'mi daño es de {str(chara.dmg)}\n'
          f'mis ataques son {str(format(chara.attack_list))}'
          )
