class Monsters:
    def __init__(self, name: str, human_age: int, place: str, elemental_attack: str, pv: int, dmg: int):

        self.name = name
        self.human_age = human_age
        self.place = place
        self.elemental_attack = elemental_attack
        self.pv = pv
        self.dmg = dmg


def say_hello_animals(monster):
    print('Hola mi nombre es ' + monster.name)
    print('Tengo ' + str(monster.human_age) + ' años humanos')
    print('Soy de ' + monster.place)
    print('Mi ataque elemental es ' + monster.elemental_attack)
