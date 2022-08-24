class Monsters:
    def __init__(self, name: str, lvl: int, xp: int, pv: int, dmg: int):

        self.name = name
        self.lvl = lvl
        self.xp = xp
        self.pv = pv
        self.dmg = dmg


def say_hello(monster):
    print('Hola mi nombre es ' + monster.name)
    print('Tengo ' + str(monster.lvl) + ' nivel')
    print('la experiencia acumulada es ' + str(monster.xp))
    print('mi vida actual es de ' + str(monster.pv))
    print('mi daño es de ' + str(monster.dmg))
