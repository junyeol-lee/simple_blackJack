from Deck import Deck
class Player():
    def __init__(self,name, balance = 0):
        self.name = name
        self.balance = balance
        self.hand = list()
        self.currentCardSum = 0
    
    def change_name(self, new_name):
        old_name = self.name
        self.name = new_name
        print(f'Name has changed from {old_name} to {self.name}')

    def increase_balance(self, amount):
        self.balance  = self.balance + amount
        print(f'Balance increased, your current balance is {self.balance}')
    
    def decrease_balance(self, amount):
        self.balance = self.balance - amount
        print(f"Balance decreased, your current balance is {self.balance}")
    
    def add_hand(self,card):
        self.hand.append(card)
    
    def empty_hand(self):
        self.hand = list()
        #print("Hand is empty now")
    
    def show_hand(self):
        hand_list = list()
        for item in self.hand:
            if item.isFaceUp:
                hand_list.append([item.shape,item.number])
            else:
                hand_list.append(['FaceDown'])
        return hand_list

    def faceUp_all_cards(self):
        for card in self.hand:
            card.isFaceUp = True

    def is_black_jack(self):
        valueList = [self.hand[0].value, self.hand[1].value]

        if 1 in valueList and 10 in valueList:
           return True
        else:
            return False

    def calc_hand(self):
        hand_list = list()
        for card in self.hand:
            hand_list.append(card.value)

        while 11 in hand_list and sum(hand_list) > 21:
            for item in range(0,len(hand_list)):
                if hand_list[item] == 11:
                    hand_list[item] = 1
                    break

        return sum(hand_list)

    



if __name__ == '__main__':
    deck = Deck()
    deck.generate_deck()
    deck.shuffle_deck()
    deck.print_deck()

    player = Player('jun',200)
    player.add_hand(deck.get_card(True))
    player.add_hand(deck.get_card(False))
    print(player.show_hand())
    player.faceUp_all_cards()
    print(player.show_hand())