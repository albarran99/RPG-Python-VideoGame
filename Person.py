class Humans:
    def __init__(self, name: str, age: int, place: str, pv: int, dmg: int) -> None:

        self.name = name
        self.age = age
        self.place = place
        self.pv = pv
        self.dmg = dmg


def say_hello(user):
    print('Hola mi nombre es ' + user.name)
    print('Tengo ' + str(user.age) + ' años humanos')
    print('Soy de ' + user.place)
