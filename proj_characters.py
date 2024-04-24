#Imports all classes related to the cards in the game.
from project_cards import *

#This class is used to create and manage the player characters in the game. 
class PlayerChar():
    #The class contains the name, all possible cards, the stating health, the type and ammount of buff.
    def __init__(self, name, possible_cards, health, buff_name, description):
        self.name = name
        self.cards = possible_cards
        self.health = health
        self.shield = 0
        self.status = 0
        self.buff_name = buff_name
        self.description = description

    def get_name(self):
        return self.name

    def get_cards(self):
        return self.cards

    def get_health(self):
        return self.health
    
    #This method allows damage taken to be dealt first to the shields then the rest goes to the health
    def take_dmg(self, dmg):
        if self.shield <= dmg:
            dmg -= self.shield
            self.shield = 0
        else:
            self.shield -= dmg
            dmg = 0
        self.health -= dmg
        return self.health

    def heal(self, heal):
        self.health += heal

    def gain_shield(self, block):
        self.shield += block

    def get_status(self):
        return self.status

    def gain_status(self, mod):
        self.status += mod

    def view_card_list(self):
        return self.cards.print_deck()
    
    #Prints all the character info. Used when picking a character at the start of the game.
    def view_char_info(self):
        char_info_str = ''
        char_info_str += ('Name: ' + self.get_name()).center(30) + '\n'
        char_info_str += ('Health: ' + str(self.get_health()) + ' Shield: ' + str(self.shield)).center(30) + '\n'
        char_info_str += (self.buff_name + ': ' + str(self.status)).center(30) + '\n'
        char_info_str += (self.description).center(30) + '\n'
        char_info_str += ('Card List').center(30) + '\n'
        char_info_str += ('-------------').center(30) + '\n'
        #Prints all cards in the character's possible deck.
        for i in self.cards.get_deck():
            char_info_str += str(i.card_info())
            char_info_str += '\n' + '\n'
        return char_info_str
    
    #Is nearly identical to the method above but removes the description and possible cards to remove clutter in combat.
    def view_char_info_combat(self):
        char_info_str = ''
        char_info_str += ('Name: ' + self.get_name()).center(30) + '\n'
        char_info_str += ('Health: ' + str(self.get_health()) + ' Shield: ' + str(self.shield)).center(30) + '\n'
        char_info_str += (self.buff_name + ': ' + str(self.status)).center(30) + '\n'
        return char_info_str

#All possible cards for the knight character.
slash = Card('Slash', 5, 0, 'Attack', 'Knight', status='Bleed', status_num=1, status_type='DPS')
guard = Card('Guard', 0, 8, 'Deffense', 'Knight')
punch = Card('Punch', 2, 0, 'Attack', 'Knight', cost=0)
throw = Card('Throw', 4, 3, 'Attack', 'Knight', cost=2, status='Strength', status_num=1, status_type='BUFF')
thrust = Card('Thrust', 3, 0, 'Attack', 'Knight', status='Bleed', status_num=4,status_type='DPS')
grit = Card('Grit', 0, 10, 'Deffense', 'Knight', cost=2)
toughen = Card('Toughen', 0, 2, 'Buff', 'Knight', status='Strength', status_num=2, status_type='BUFF')
live_with_honor = Card('Live With Honor', 0, 15, 'Deffense', 'Knight', cost=3, status='Strength', status_num=3, status_type='BUFF')
die_with_glory = Card('Die With Glory', 15, -10, 'Attack', 'Knight', cost=3, status='Bleed', status_num=5, status_type='DPS')
flex = Card('Flex', 0, 0, 'Buff', 'Knight', cost=0, status='Strength', status_num=1, status_type='BUFF')

#Cards are added to a deck that is used below.
knight_cards = Deck([])
knight_cards.add_card(slash)
knight_cards.add_card(guard)
knight_cards.add_card(punch)
knight_cards.add_card(throw)
knight_cards.add_card(thrust)
knight_cards.add_card(grit)
knight_cards.add_card(toughen)
knight_cards.add_card(live_with_honor)
knight_cards.add_card(die_with_glory)
knight_cards.add_card(flex)

#The base character used if the player selects the Knight to view info.
knight = PlayerChar('Knight', knight_cards, 50, 'Strength', 'The Knight uses a combination of its high health and block to tank damage from all sources. \n Its strength cards can buff its own attack while bleed provides the DPS it needs to make up for its slower attacks.')

#All cards for the assassin class
parry = Card('Parry', 1, 7, 'Deffense', 'Assassin', status='Poison', status_num=2, status_type='DPS')
backstab = Card('Backstab', 5, 2, 'Attack', 'Assassin', status='Dexterity', status_num=1, status_type='BUFF')
poison_gas = Card('Poison Gas', 0, 0, 'Debuff', 'Assassin', status='Poison', status_num=8, status_type='DPS')
sneak = Card('Sneak', 0, 5, 'Deffense', 'Assassin', cost=0)
shiv = Card('Shiv', 5, 0, 'Attack', 'Assassin', cost=0)
cloudkill = Card('Cloudkill', 6, 2, 'Attack', 'Assassin', cost=2, status='Poison', status_num=8, status_type='DPS')
feint = Card('Feint', 3, 6, 'Deffense', 'Assassin', status='Dexterity', status_num=3, status_type='BUFF')
the_dragon = Card('The Dragon Becomes Me', 12, 5, 'Attack', 'Assassin', cost=2, status='Dexterity', status_num=4, status_type='BUFF')
reckless_strike = Card('Reckless Strike', 10, 0, 'Attack', 'Assassin', status='Dexterity', status_num=-2, status_type='BUFF')
sickening_radience = Card('Sickening Radience', 2, 1, 'Debuff', 'Assassin', cost=2, status='Poison', status_num=8, status_type='DPS')

#All the above cards are added to a deck
assassin_cards = Deck([])
assassin_cards.add_card(parry)
assassin_cards.add_card(backstab)
assassin_cards.add_card(poison_gas)
assassin_cards.add_card(sneak)
assassin_cards.add_card(shiv)
assassin_cards.add_card(cloudkill)
assassin_cards.add_card(feint)
assassin_cards.add_card(the_dragon)
assassin_cards.add_card(reckless_strike)
assassin_cards.add_card(sickening_radience)

#The base class used if the player selects to view the Assassin
assassin = PlayerChar('Assassin', assassin_cards, 40, 'Dexterity', 'The Assassin may not have the most health, but its dexterity allows it to increase its shield faster and faster over time. \n It also relies on poison and fast, small attacks to whittle down enemies.')

#All cards for the mage
magic_missile = Card('Magic Missile', 3, 0, 'Attack', 'Mage', cost=0)
misty_step = Card('Misty Step', 0, 5, 'Deffense', 'Mage', status='Aura', status_num=1, status_type='BUFF')
firebolt = Card('Firebolt', 3, 0, 'Attack', 'Mage', status='Burn', status_num=2, status_type='DPS')
fireball = Card('Fireball', 7, 0, 'Attack', 'Mage', cost=2, status='Burn', status_num=5, status_type='DPS')
inferno = Card('Inferno', 2, 2, 'Debuff', 'Mage', status='Burn', status_num=6, status_type='DPS')
study = Card('Study', 0, 4, 'Buff', 'Mage', status='Aura', status_num=3, status_type='BUFF')
life_drain = Card('Life Drain', 10, 0, 'Attack', 'Mage', cost=2, status='Aura', status_num=4, status_type='BUFF')
barrier = Card('Barrier', 0, 7, 'Deffense', 'Mage')
wall_of_fire = Card('Wall of Fire', 3, 5, 'Deffense', 'Mage', status='Burn', status_num=2, status_type='DPS')
eldritch_blast = Card('Eldritch Blast', 12, 0, 'Attack', 'Mage', cost=2)

#All above cards are added to a deck
mage_cards = Deck([])
mage_cards.add_card(magic_missile)
mage_cards.add_card(misty_step)
mage_cards.add_card(firebolt)
mage_cards.add_card(fireball)
mage_cards.add_card(inferno)
mage_cards.add_card(study)
mage_cards.add_card(life_drain)
mage_cards.add_card(barrier)
mage_cards.add_card(wall_of_fire)
mage_cards.add_card(eldritch_blast)

#The base class used if the player wants to view the Mage
mage = PlayerChar('Mage', mage_cards, 25, 'Aura', 'The Mage is constantly studying and increasing the ammount of burn it can throw onto its enemeies. \n Its low health and block makes it a bit of a glass cannon, but it can dish out more damage than any other class.')