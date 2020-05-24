class Dealer():

    def __init__(self):
        self.hand = list()

    def add_hand(self,card):
        self.hand.append(card)
    
    def empty_hand(self):
        self.hand = list()
        print("Hand is empty now")

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