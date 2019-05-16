import pyCardDeck
from typing import List
import random
from pyCardDeck.cards import PokerCard


def generate_Card():
    suit_name = ['clue','diamonds','hearts','spades']
    rank_name = ['none','ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    cards = []
    for suit in range(4):
        for rank in range(1,14):
            card = (suit_name[suit],rank_name[rank])
            cards.append(card)
    print("Deck of cards for the table is loaded")
    return cards
class Player:
    def __init__(self,name:str):
        self.hand = []
        self.name = name
    def __str__(self):
        return self.name

    
class five_cards_draw:
    def __init__(self,players:List[Player]):
        self.deck = pyCardDeck.Deck(cards=generate_Card(),name = "five cards draw")
        self.players = players
        self.deck.shuffle()
        print("Created a table with {} players".format(len(self.players)))
                    
    def distribute_cards(self):
        """distrubute cards to each user"""
        for p in self.players:
            for i in range(5):
                newcard = self.deck.draw()
                p.hand.append(newcard)
            print(p.hand)
        print("distribution finished")
        self.user_decision()
        
    def user_decision(self):
        for p in self.players:
            decision=input("%s ,do u wannna countinue? Y/N" % p)
            if decision == 'N':
                self.players.remove(p)
            elif decision == 'Y':
                self.user_follow(p)  
            else:
                print("please enter valid characters!")
                self.user_decision()
                
    def user_follow(self,p):
        print('your hand cards are:',p.hand)
        dec = input("%s, do u wanna change your card?" % p)
        if dec == 'Y':
            discard_lst = input("which one you wanna change?").split(',')
        for i in range(6):
            if str(i) in discard_lst:
                del p.hand[i-1]
            else:
                pass
        for i in range(5-len(p.hand)):
            newcard = self.deck.draw()
            p.hand.append(newcard)
        print("your new hand cards",p.hand)

    def winner(self):
        lst_rank=[]
        self.count = 0
        winner={}
        for p in self.players:
            for i in range(5):
                lst_rank.append(p.hand[i][1])
                self.straight(p)
                self.flush(p,lst_rank)
                self.pairs(p)
                winner[p] = self.count
        value = max(winner,key=winner.get)
        print(get_key(winner,value))
        
    def get_key(dict, value):
               return [k for k, v in dict.items() if v == value]    

    def straight(self,p):    
        if p.hand[i][0] == 'clue':
            self.count += 10 #clue_straight is ten points
        elif p.hand[i][0] == 'diamonds':
            self.count += 11
        elif p.hand[i][0] == 'hearts':
            self.count += 12
        elif p.hand[i][0] == 'spades':
            self.count += 13
        return self.count
    
    def flush(self,p,lst_rank):
        lst_rank.sort()
        maxnum = max(lst_rank)
        minnum = min(lst_rank)
        flush_lst= [i for i in range(minnum,maxnum+1)]
        if flush_lst == lst_rank:
            self.count = self.count + 6 # flush gets 6 points
        else:
            pass
        return self.count
        
    def pairs(self,p):
        hist = {}
        for key in p.hand:
            if key[1] not in hist:
                hist[key[1]] = 1
            else:
                hist[key[1]] = hist[key[1]] + 1
        num_pairs = hist.values()
        max_pairts = max(num_pairs)
        if max_pairs == 4:
            self.count += 15
        elif max_pairs == 3 and min(num_pairs) == 2:
            self.count += 14
        elif max_pairs == 3:
            self.count += 5
        elif max_pairs == 2 and min(num_pairs) == 2:
            self.count += 4
        elif max_pairs == 2:
            self.count += 3
        else:
            self.count += 1
        return self.count
        

if __name__ == '__main__':
    table = five_cards_draw([Player("Jack"), Player("John"), Player("Peter")])
    table.distribute_cards()
    
