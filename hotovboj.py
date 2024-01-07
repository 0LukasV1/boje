class Warrior:
    def __init__(self):
        self.ziv=50
        self.utok=5
    @property
    def is_alive(self):
        return self.ziv>0
class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.utok=7
def fight(modr, cerv):
    while True:
        cerv.ziv-=modr.utok
        if not cerv.is_alive:
            return True
        modr.ziv-=cerv.utok
        if not modr.is_alive:
            return False
class Army:
    def __init__(self):
        self.vojaci=[]
    def add_units(self, druhvoj, count):
        for _ in range(count):
            self.vojaci.append(druhvoj())
class Battle:
    def fight(self, army_1, army_2):
        while len(army_1.vojaci)>0 and len(army_2.vojaci)>0:
            if fight(army_1.vojaci[0], army_2.vojaci[0]):
                army_2.vojaci.pop(0)
            else:
                army_1.vojaci.pop(0)
        return len(army_1.vojaci)>0
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

print(fight(chuck, bruce))
print(fight(dave, carl))
print(chuck.is_alive)
print(bruce.is_alive)
print(carl.is_alive)
print(dave.is_alive)
print(fight(carl, mark))
print(carl.is_alive)

my_army=Army()
my_army.add_units(Knight,3)
enemy_army=Army()
enemy_army.add_units(Warrior,3)
army_3=Army()
army_3.add_units(Warrior,20)
army_3.add_units(Knight,5)
army_4=Army()
army_4.add_units(Warrior,30)
battle=Battle()

print(battle.fight(my_army,enemy_army))
print(battle.fight(army_3,army_4))
