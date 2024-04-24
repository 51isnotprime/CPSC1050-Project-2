#This class is used by all enemies in order to create the monsters to fight.
class Enemies():
    #The monster class takes a name, a set of attacks, and the status and num and name from the character played
    def __init__(self, name, health, attack1, attack2, status_num, character):
        self.name = name
        self.health = health
        self.attack1 = attack1
        self.attack2 = attack2
        self.shield = 0
        self.status_num = status_num
        self.character = character

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def raise_shield(self, block):
        self.shield += block

    #Resuses the player take damage method to take damage to shields first
    def take_damage(self, dmg):
        if self.shield <= dmg:
            dmg -= self.shield
            self.shield = 0
        else:
            self.shield -= dmg
            dmg = 0
        self.health -= dmg
        if self.health < 0:
            self.health = 0
        return self.health
    
    #Allows status to be changed withoug going below 0
    def change_status(self, mod):
        self.status_num += mod
        if self.status_num < 0:
            self.status_num = 0

    def get_status_num(self):
        return self.status_num
    
    #Prints all monster info and formats and centers it.
    def print_monster_info(self):
        mon_str = ''
        mon_str += (self.name.upper()).center(30) + '\n'
        mon_str += ('Health: ' + str(self.health) + ' Shield: ' + str(self.shield)).center(30) + '\n'
        if self.character == 'Knight':
            mon_str += ('Bleed: ' + str(self.status_num)).center(30) + '\n'
        if self.character == 'Assassin':
            mon_str += ('Poison: ' + str(self.status_num)).center(30) + '\n'
        if self.character == 'Mage':
            mon_str += ('Burn: ' + str(self.status_num)).center(30) + '\n'
        mon_str += ('ATTACKS').center(30) + '\n'
        mon_str += self.attack1.print_attack()
        mon_str += '----------'.center(30) + '\n'
        mon_str += self.attack2.print_attack()
        return mon_str

#A subclass of Enemies, Boss allows for a 3rd attack to be made and makes that monster tougher by adding damage reduction
class Boss(Enemies):
    def __init__(self, name, health, attack1, attack2, attack3, status_num, character_choice):
        Enemies.__init__(self, name, health, attack1, attack2, status_num, character_choice)
        self.attack3 = attack3

    def take_damage(self, dmg):
        dmg = dmg // 2
        if self.shield <= dmg:
            dmg -= self.shield
            self.shield = 0
        else:
            self.shield -= dmg
            dmg = 0
        self.health -= dmg
        if self.health < 0:
            self.health = 0
        return self.health 

    def print_monster_info(self):
        mon_str = super().print_monster_info()
        mon_str += '----------'.center(30) + '\n'
        mon_str += self.attack3.print_attack()
        return mon_str

#Creats attacks for all monsters in the game, giving both attack and block and having a method to print them out
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

    
