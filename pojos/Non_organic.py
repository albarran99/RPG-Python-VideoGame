class Bionicle:
    def __init__(self, name: str, lvl: int, xp: int, pv: int, dmg: int) -> None:

        self.name = name
        self.lvl = lvl
        self.xp = xp
        self.pv = pv
        self.dmg = dmg


def say_hello(bionicle):
    print('Hola mi nombre es ' + bionicle.name)
    print('Tengo ' + str(bionicle.lvl) + ' nivel')
    print('la experiencia acumulada es ' + str(bionicle.xp))
    print('mi vida actual es de ' + str(bionicle.pv))
    print('mi daño es de ' + str(bionicle.dmg))
