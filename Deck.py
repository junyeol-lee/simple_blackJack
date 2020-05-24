import random
from Card import Card
class Deck():
    '''
    Generate a new deck for user.
    '''
    def __init__(self):
        self.deck = list()

    def generate_deck(self):
        '''
        Heart = u2661 spade = u2664 diamond = u2662 clover = u2667
        '''
        shapes = ['u2661','u2664','u2662','u2667']
        shapes = ['Heart','Spade','Diamond','Clover']
        jqk = ['J','Q','K']
        isFaceUp = False
        jqkValue = 10

        for item in shapes:
            for number in range(1,11):
                value = number
                if number == 1:
                    value = 11
                    number = 'A'
                self.deck.append(Card(item,number,isFaceUp,value))
            for jqkItem in jqk:
                self.deck.append(Card(item,jqkItem,isFaceUp,jqkValue))


    def shuffle_deck(self):
        '''
        Shuffle the deck.
        '''
        random.shuffle(self.deck)
        print('Deck has been shuffled.')

    def print_deck(self):
        for item in self.deck:
            print(item.shape,item.number,item.value)
        print('Number of cards in a deck : ',len(self.deck))

    def get_card(self,isFaceUp):
        popedCard = self.deck.pop()
        if isFaceUp:
            popedCard.isFaceUp = True
        else:
            popedCard.isFaceUp = False
        return popedCard

    
if __name__ == '__main__':
    temp = Deck()
    temp.generate_deck()
    temp.shuffle_deck()
    temp.print_deck()
    temp.get_card(True)
    temp.print_deck()
