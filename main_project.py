from proj_characters import *
from enemies import *
from project_cards import *
from datetime import datetime
import random
import time

win_loss_record = open('winloss.txt', 'a')
character_choice = ''

def intro():
    print('Welcome to Card Casters!')
    time.sleep(1)
    print('Venture into deep and dark dungeons to gather your strength and face the dragon.')
    print('Pick from a brave Knight, a sly Assassin, or a briliant Mage to play in your journey.')
    time.sleep(0.5)
    print('Would you like to hear more about any of the characters? (y/n)')
    more_info = input().strip().lower()
    while more_info != 'y' and more_info != 'n':
        print('Please enter y or n for yes or no.')
        time.sleep(0.5)
        print('Would you like to hear more about any of the characters? (y/n)')
        more_info = input().strip().lower()
    while more_info == 'y':
        print('Which character would you like to hear more about?')
        char_info_choice = input().strip().lower()
        while char_info_choice != 'knight' and char_info_choice != 'assassin' and char_info_choice != 'mage':
            print('Please enter one of the three character choices. Knight, Assassin, or Mage.')
            time.sleep(1)
            print('Which character would you like to hear more about?')
            char_info_choice = input().strip().lower()
        if char_info_choice == 'knight':
            print(knight.view_char_info())
        elif char_info_choice == 'assassin':
            print(assassin.view_char_info())
        elif char_info_choice == 'mage':
            print(mage.view_char_info())
        time.sleep(1)
        print('Would you like to view another character?')
        more_info = input().strip().lower()
        while more_info != 'y' and more_info != 'n':
            print('Please enter y or n for yes or no.')
            time.sleep(0.5)
            print('Would you like to hear more about any of the characters? (y/n)')
            more_info = input().strip().lower()
    
def character_picker(character):
    if character == 'knight':
        return knight, 'Knight'
    elif character == 'assassin':
        return assassin, 'Assassin'
    elif character == 'mage':
        return mage, 'Mage'
        
def make_start_deck(character):
    deck = Deck([])
    if character == 'Knight':
        for i in range(4):
            deck.add_card(Card('Slash', 5, 0, 'Attack', 'Knight', status='Bleed', status_num=1, status_type='DPS'))
        for i in range(3):
            deck.add_card(Card('Guard', 0, 8, 'Deffense', 'Knight'))
        for i in range(2):
            deck.add_card(Card('Punch', 2, 0, 'Attack', 'Knight', cost=0))
        deck.add_card(Card('Throw', 4, 3, 'Attack', 'Knight', cost=2, status='Strength', status_num=1, status_type='BUFF'))
    elif character == 'Assassin':
        for i in range(3):
            deck.add_card(Card('Parry', 1, 7, 'Deffense', 'Assassin', status='Poison', status_num=1, status_type='DPS'))
        for i in range(2):
            deck.add_card(Card('Backstab', 4, 2, 'Attack', 'Assassin', status='Dexterity', status_num=1, status_type='BUFF'))
        for i in range(3):
            deck.add_card(Card('Feint', 1, 6, 'Deffense', 'Assassin', status='Dexterity', status_num=3, status_type='BUFF'))
        for i in range(2):
            deck.add_card(Card('Shiv', 4, 0, 'Attack', 'Assassin', cost=0))
    elif character == 'Mage':
        for i in range(3):
            deck.add_card(Card('Magic Missile', 3, 0, 'Attack', 'Mage', cost=0))
            deck.add_card(Card('Firebolt', 3, 0, 'Attack', 'Mage', status='Burn', status_num=2, status_type='DPS'))
        for i in range(2):
            deck.add_card(Card('Study', 0, 4, 'Buff', 'Mage', status='Aura', status_num=3, status_type='BUFF'))
            deck.add_card(Card('Fireball', 7, 0, 'Attack', 'Mage', cost=2, status='Burn', status_num=5, status_type='DPS'))
    return deck

def player_turn(monster, player_cards, player_char, character_choice):
    player_energy = 3
    player_cards.draw()
    while player_energy != 0 and len(player_cards.get_hand()) != 0 and monster.get_health() > 0:
        print('Hand: ')
        print(player_cards.print_hand())
        print('\n' + 'Energy: ' + str(player_energy))
        print('Select a card to play, eneter 0 to end your turn. Input the number of the position it appears in your hand:')
        while True:
            try:
                card_choice = int(input().strip())
                if card_choice == 0:
                    break
                player_cards.get_hand()[card_choice - 1].get_title()
            except ValueError:
                print('Please enter a valid number.')
                card_choice = int(input().strip())
            except IndexError:
                print('Please enter a valid number.')
                card_choice = int(input().strip())
            print(player_cards.get_hand()[card_choice - 1].get_title())
            break
        if card_choice == 0:
            break
        print('Do you want to play this card (1) or learn more about it (2)?')
        play_learn = input().strip()
        while play_learn != '1' and play_learn != '2':
            print('Please enter a valid choice, 1 or 2.')
            play_learn = input().strip()
        if play_learn == '1':
            if player_cards.get_hand()[card_choice - 1].get_cost() > player_energy:
                print('That card is too expensive to play right now.')
                continue
            if character_choice == 'Knight' and player_cards.get_hand()[card_choice - 1].get_damage() != 0:
                monster.take_damage((player_cards.get_hand()[card_choice - 1].get_damage()) + (player_char.get_status()))
            else:
                monster.take_damage(player_cards.get_hand()[card_choice - 1].get_damage())
            if character_choice == 'Assassin' and player_cards.get_hand()[card_choice - 1].get_shield() != 0:
                player_char.gain_shield(player_cards.get_hand()[card_choice - 1].get_shield() + (player_char.get_status()))
            else:
                player_char.gain_shield(player_cards.get_hand()[card_choice - 1].get_shield())
            if player_cards.get_hand()[card_choice - 1].get_status_type() == 'DPS':
                if character_choice == 'Mage' and player_cards.get_hand()[card_choice - 1].get_status_num() != 0:
                    monster.change_status(player_cards.get_hand()[card_choice - 1].get_status_num() + (player_char.get_status()))
                else:
                    monster.change_status(player_cards.get_hand()[card_choice - 1].get_status_num())
            elif player_cards.get_hand()[card_choice - 1].get_status_type() == 'BUFF':
                player_char.gain_status(player_cards.get_hand()[card_choice - 1].get_status_num())
            player_energy -= player_cards.get_hand()[card_choice - 1].get_cost()
            player_cards.discard_card(card_choice - 1)
            print(monster.print_monster_info())
        else:
            print(player_cards.get_hand()[card_choice - 1].card_info())
    print(player_char.view_char_info_combat())
    for i in range(len(player_cards.get_hand())):
        player_cards.discard_card(0)
    if monster.get_health() <= 0:
        print(f'The {monster.get_name()} is slain.')
        return 'Win'
            
def mon_turn(monster, player_char):
    if isinstance(monster, Boss):
        attack_choice = random.randint(1, 3)
        if attack_choice == 1:
            monster.raise_shield(monster.attack1.get_block())
            player_char.take_dmg(monster.attack1.get_dmg())
        elif attack_choice == 2:
            monster.raise_shield(monster.attack2.get_block())
            player_char.take_dmg(monster.attack2.get_dmg())
        elif attack_choice == 3:
            monster.raise_shield(monster.attack3.get_block())
            player_char.take_dmg(monster.attack3.get_dmg())
    else:
        attack_choice = random.randint(1, 2)
        if attack_choice == 1:
            monster.raise_shield(monster.attack1.get_block())
            player_char.take_dmg(monster.attack1.get_dmg())
        elif attack_choice == 2:
            monster.raise_shield(monster.attack2.get_block())
            player_char.take_dmg(monster.attack2.get_dmg())
    if player_char.get_health() <= 0:
        print('You died!')
        return 'Loss'
    monster.take_damage(monster.get_status_num())
    monster.change_status(-1)
    print(player_char.view_char_info_combat())
    print(monster.print_monster_info())
    if monster.get_health() <= 0:
        print(f'The {monster.get_name()} is slain.')
        return 'Win'

def fight(monster, player_char, player_cards, character_choice):
    player_cards.reset()
    print(f'A {monster.get_name()} appears.')
    print(monster.print_monster_info())
    while True:
        if player_turn(monster, player_cards, player_char, character_choice) != None:
            break
        mon_result = mon_turn(monster, player_char)
        if mon_result == 'Win':
            break
        elif mon_result == 'Loss':
            loss_time = datetime.now()
            win_loss_record.write(f'You lost with the {player_char.get_name()} on {loss_time.strftime("%d/%m/%Y %H:%M:%S")} \n')
            print(f'You lost with the {player_char.get_name()} on {loss_time.strftime("%d/%m/%Y %H:%M:%S")}')
            print('We hope you adventure again soon.')
            win_loss_record.close()
            exit(1)

def gain_card(player_char, player_cards):
    card_option1 = player_char.cards.get_deck()[random.randint(0, len(player_char.cards.get_deck()) - 1)]
    card_option2 = player_char.cards.get_deck()[random.randint(0, len(player_char.cards.get_deck()) - 1)]
    card_option3 = player_char.cards.get_deck()[random.randint(0, len(player_char.cards.get_deck()) - 1)]
    print('Pick a card to add to your deck (1-3): ')
    print(card_option1.get_title() + ', ' + card_option2.get_title() + ', ' + card_option3.get_title())
    gain_choice = input().strip()
    while gain_choice != '1' and gain_choice != '2' and gain_choice != '3':
        print('Please enter a valid choice.')
        gain_choice = input().strip()
    if gain_choice == '1':
        print(card_option1.card_info())
        player_cards.get_deck().get_deck().append(card_option1)
    elif gain_choice == '2':
        print(card_option2.card_info())
        player_cards.get_deck().get_deck().append(card_option2)
    elif gain_choice == '3':
        print(card_option3.card_info())
        player_cards.get_deck().get_deck().append(card_option3)


def main():
    intro()
    print('Now it\'s time to pick your character.')
    time.sleep(0.25)
    print('Please pick a character to play.')
    char_choice = input().lower().strip()
    while char_choice != 'knight' and char_choice != 'assassin' and char_choice != 'mage':
        print('Please enter a valid character chocie from the three options.')
        char_choice = input().lower().strip()
    player_char, character_choice = character_picker(char_choice)
    player_deck = make_start_deck(character_choice)
    player_cards = Piles(player_deck, [], [])
    mon_list = [skeleton, specter, golem, beholder]
    for i in mon_list:
        fight(i, player_char, player_cards, character_choice)
        time.sleep(2)
        gain_card(player_char, player_cards)
        print('Get ready for the next fight!')
        time.sleep(1)
    print('You made it this far...')
    print('Now get ready for the final fight!')
    fight(dragon, player_char, player_cards, character_choice)
    print('You defeated the dragon!')
    print('You WIN!!!')
    win_time = datetime.now()
    win_loss_record.write(f'You won with the {player_char.get_name()} on {win_time.strftime("%d/%m/%Y %H:%M:%S")} \n')
    print(f'You won with the {player_char.get_name()} on {win_time.strftime("%d/%m/%Y %H:%M:%S")}')
    win_loss_record.close()

if __name__ == '__main__':
    main()