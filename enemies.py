class Enemies():
    def __init__(self, name, health, attack1, attack2, status_num):
        self.name = name
        self.health = health
        self.attack1 = attack1
        self.attack2 = attack2
        self.shield = 0
        self.status_num = status_num

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def raise_shield(self, block):
        self.shield += block

    def take_damage(self, dmg):
        if self.shield <= dmg:
            dmg -= self.shield
            self.shield = 0
        else:
            self.shield -= dmg
            dmg = 0
        self.health -= dmg
        return self.health
    
    def change_status(self, mod):
        self.status_num += mod

    def get_status_num(self):
        return self.status_num
    
    def print_monster_info(self):
        mon_str = ''
        mon_str += (self.name.upper()).center(30) + '\n'
        mon_str += ('Health: ' + str(self.health) + ' Shield: ' + str(self.shield)).center(30) + '\n'
        mon_str += ('ATTACKS').center(30) + '\n'
        mon_str += self.attack1.print_attack()
        mon_str += '----------'.center(30) + '\n'
        mon_str += self.attack2.print_attack()
        return mon_str


class Boss(Enemies):
    def __init__(self, name, health, attack1, attack2, attack3, status_num):
        Enemies.__init__(self, name, health, attack1, attack2, status_num)
        self.attack3 = attack3

    def print_monster_info(self):
        mon_str = super().print_monster_info()
        mon_str += '----------'.center(30) + '\n'
        mon_str += self.attack3.print_attack()
        return mon_str

class Attack():
    def __init__(self, dmg, block):
        self.dmg = dmg
        self.block = block

    def get_dmg(self):
        return self.dmg
    
    def get_block(self):
        return self.block
    
    def print_attack(self):
        att_str = ''
        if self.dmg != 0:
            att_str += ('Deal ' + str(self.dmg) + ' damage.').center(30) + '\n'
        if self.block != 0:
            att_str += ('Gain ' + str(self.block) + ' shield.').center(30) + '\n'
        return att_str

    
dragon_attack1 = Attack(10, 0)
dragon_attack2 = Attack(5, 10)
dragon_attack3 = Attack(0, 25)
dragon = Boss('Dragon', 50, dragon_attack1, dragon_attack2, dragon_attack3, 0)
#print(dragon.print_monster_info())
skele_attack1 = Attack(5, 0)
skele_attack2 = Attack(8, 0)
skeleton = Enemies('Skeleton', 15, skele_attack1, skele_attack2, 0)
gol_attack1 = Attack(12, 5)
gol_attack2 = Attack(0, 0)
golem = Enemies('Golem', 35, gol_attack1, gol_attack2, 0)
spec_attack1 = Attack(5, 0)
spec_attack2 = Attack(4, 5)
specter = Enemies('Specter', 20, spec_attack1, spec_attack2, 0)
behold_attack1 = Attack(8, 0)
behold_attack2 = Attack(5, 20)
beholder = Enemies('Beholder', 25, behold_attack1, behold_attack2, 0)
