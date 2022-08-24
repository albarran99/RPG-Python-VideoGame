from typing import Any


class Humans:
    def __init__(self, name: str, lvl: int, xp: int, pv: int, dmg: int) -> None:
        self.name = name
        self.lvl = lvl
        self.xp = xp
        self.pv = pv
        self.dmg = dmg

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


def xp_achieved(human, xp):
    human.xp = xp + human.xp


def lvl_2(human):
    if human.xp == 100:
        human.lvl = human.lvl + 1
        print(f"¡Bien, tu {human.name} a subido de nivel!, ahora es {human.lvl}")
        print("¡subida!" + '\n'
              + 'sube +2 =' + f'{human.pv}' + '\n'
              + 'sube +4 =' + f'{human.dmg}')
        human.xp = 0
    else:
        pass


def lvl_3(human):
    if human.xp == 200:
        human.lvl = human.lvl + 1
        print(f"¡Bien, tu {human.name} a subido de nivel!, ahora es {human.lvl}")
        print("¡subida!" + '\n'
              + 'sube +5 =' + f'{human.pv}' + '\n'
              + 'sube +2 =' + f'{human.dmg}')
        human.xp = 0
    else:
        pass


def lvl_4(human):
    if human.xp == 250:
        human.lvl = human.lvl + 1
        print(f"¡Bien, tu {human.name} a subido de nivel!, ahora es {human.lvl}")
        print("¡subida!" + '\n'
              + 'sube +3 =' + f'{human.pv}' + '\n'
              + 'sube +4 =' + f'{human.dmg}')
        human.xp = 0
    else:
        pass


def lvl_5(human):
    if human.xp == 300:
        human.lvl = human.lvl + 1
        print(f"¡Bien, tu {human.name} a subido de nivel!, ahora es {human.lvl}")
        print("¡subida!" + '\n'
              + 'sube +6 =' + f'{human.pv}' + '\n'
              + 'sube +5 =' + f'{human.dmg}')
        human.xp = 0
    else:
        pass


def level_up(human):
    if lvl_2(human):
        human.pv = human.pv + 2
        human.pv = human.dmg + 4

    if lvl_3(human):
        human.pv = human.pv + 5
        human.pv = human.dmg + 2

    if lvl_4(human):
        human.pv = human.pv + 3
        human.pv = human.dmg + 4

    if lvl_5(human):
        human.pv = human.pv + 6
        human.pv = human.dmg + 5


def say_hello(human):
    print('Hola mi nombre es ' + human.name)
    print('Tengo ' + str(human.lvl) + ' nivel')
    print('la experiencia acumulada es ' + str(human.xp))
    print('mi vida actual es de ' + str(human.pv))
    print('mi daño es de ' + str(human.dmg))
