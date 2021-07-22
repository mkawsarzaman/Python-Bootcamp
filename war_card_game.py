from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
                'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
# class for Cards
class Cards():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

#class for Decks
class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Cards(suit,rank))
    
    def shuffle_deck(self):
        shuffle(self.all_cards)
        
    def deal_card(self):
        return self.all_cards.pop(0)
    
#player class
class Player():
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    def remove_card(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            return self.all_cards.extend(new_cards)
        else:
            return self.all_cards.append(new_cards)
    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards'
    

#Game logic

new_deck = Deck()
new_deck.shuffle_deck()
player1 = Player('one')
player2 = Player('two')

for card in range(26):
    player1.add_cards(new_deck.deal_card())
    player2.add_cards(new_deck.deal_card())

round = 0
game_on = True

while game_on == True:
    round += 1
    print(f'Round: {round}')
    
    if len(player1.all_cards) == 0:
        print('Player 1 has lost, Player 2 won!')
        break
    if len(player2.all_cards) == 0:
        print('Player 2 has lost, Player 1 won!')
        break
    
    player1_cards_played = []
    player1_cards_played.append(player1.remove_card())
    
    player2_cards_played = []
    player2_cards_played.append(player2.remove_card())
    
    at_war = True
    while at_war == True:
        if player1_cards_played[-1].value > player2_cards_played[-1].value:
            player1.add_cards(player1_cards_played)
            player1.add_cards(player2_cards_played)
            break
        elif player2_cards_played[-1].value > player1_cards_played[-1].value:
            player2.add_cards(player2_cards_played)
            player2.add_cards(player1_cards_played)
            break
        else:
            print('at war!!')
            
            if len(player1.all_cards) < 5:
                print('Player 1 does not have enough cards')
                print('Player 1 has lost, Player 2 won!')
                game_on = False
                break
                
            elif len(player2.all_cards) < 5:
                print('Player 2 does not have enough cards')
                print('Player 2 has lost, Player 1 won!')
                game_on = False
                break
                
            else:
                for i in range(5):
                    player1_cards_played.append(player1.remove_card())
                    player2_cards_played.append(player2.remove_card())
