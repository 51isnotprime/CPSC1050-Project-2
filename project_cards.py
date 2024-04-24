#The random import allows for random drawing of cards from the deck later in the code.
import random

#This class is the set up for all cards the player can play, with all stats they need.
class Card():
    def __init__(self, title, damage, shield, card_type, character, cost=1, status=None, status_num=0, status_type=None):
        self.cost = cost
        self.title = title
        self.damage = damage
        self.shield = shield
        self.card_type = card_type
        self.character = character
        self.status = status
        self.status_num = status_num
        self.status_type = status_type

    #These functions return all of the card info when necessary.
    def get_cost(self):
        return self.cost

    def get_status(self):
        return self.status
    
    def get_title(self):
        return self.title

    def get_damage(self):
        return self.damage
    
    def get_shield(self):
        return self.shield

    def get_type(self):
        return self.card_type
    
    def get_character(self):
        return self.character

    def get_status_num(self):
        return self.status_num

    def get_status_type(self):
        return self.status_type

    #This class method allows for the easy and formated printing of cards whenever neccessary.
    def card_info(self):
        card_str = ''
        card_str += ('Cost: ' + str(self.get_cost())).center(30) + '\n'
        card_str += self.get_title().upper().center(30) + '\n'
        card_str += ('') + '\n'
        card_str += ('Deal ' + str(self.get_damage()) + ' damage').center(30) + '\n'
        card_str += ('Gain ' + str(self.get_shield()) + ' shield').center(30) + '\n'
        if self.get_status() != None and self.get_status_type() == 'DPS':
            card_str += ('Inflict ' + str(self.get_status_num()) + ' ' + (self.get_status()).upper() + ' on target').center(30) + '\n'
        elif self.get_status() != None and self.get_status_type() == 'BUFF':
            card_str += ('Gain ' + str(self.get_status_num()) + ' ' + (self.get_status()).upper()).center(30) + '\n'
        card_str += ('') + '\n'
        card_str += (self.get_type() + ' Card').center(30) + '\n'
        card_str += (self.get_character()).center(28) + '\n'

        return card_str

#Establishes the deck object, a multipurpouse list that is used to store and retrieve cards.
class Deck():
    def __init__(self, deck=[]):
        self.deck = deck
    
    def add_card(self, card):
        self.deck.append(card)

    def get_deck(self):
        return self.deck
    
    def print_deck_shuffled(self):
        random.shuffle(self.deck)
        deck_str = ''
        for i in self.deck:
            deck_str += (str(i.get_title()) + '\n')
        return deck_str

    def print_deck(self):
        deck_str = ''
        for i in self.deck:
            deck_str += (str(i.get_title()) + '\n')
        return deck_str

class Piles():
    def __init__(self, deck, hand=[], discard=[]):
        self.hand = hand
        self.deck = deck
        self.discard = discard
    
    def draw(self):
        for i in range(5):
            if len(self.deck.get_deck()) == 0:
                self.deck.deck = self.discard
                self.discard = []
            picker = random.randint(0, len(self.deck.get_deck()) - 1)
            self.hand.append(self.deck.get_deck()[picker])
            self.deck.get_deck().pop(picker)
    
    def reset(self):
        if len(self.hand) != 0:
            for i in range(len(self.hand)):
                self.deck.get_deck().append(self.hand[0])
                self.get_hand().pop(0)
            self.hand = []
        if len(self.discard) != 0:
            for i in range(len(self.discard)):
                self.deck.get_deck().append(self.discard[0])
                self.get_discard().pop(0)
            self.discard = []

    def get_hand(self):
        return self.hand

    def get_deck(self):
        return self.deck
    
    def discard_card(self, card_pos):
        self.discard.append(self.hand[card_pos])
        self.hand.pop(card_pos)
    
    def get_discard(self):
        return self.discard

    def print_hand(self):
        hand_str = ''
        for card in self.get_hand():
            hand_str += (card.get_title() + '\n')
        return hand_str

    def print_discard(self):
        disc_str = ''
        for i in self.discard:
            disc_str += str(i.get_title()) + '\n'
        return disc_str
