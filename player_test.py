import unittest
from Player import Player
from Card import Card

class test_player(unittest.TestCase):

    def test_init(self):
        name = 'Jun'
        balance = 200
        player = Player(name,balance)

        self.assertEqual(player.name,name)
        self.assertEqual(player.balance,balance)

    def test_change_name(self):
        name = 'Jun'
        balance = 200
        player = Player(name,balance)

        newName = "Junyeol"
        player.change_name(newName)
        self.assertEqual(player.name, newName)

    def test_increase_balance(self):
        name = 'Jun'
        balance = 200
        player = Player(name,balance)

        player.increase_balance(500)
        expected_balance = 200+500
        self.assertEqual(player.balance,expected_balance)

    def test_decrease_balance(self):
        name = 'Jun'
        balance = 200
        player = Player(name,balance)

        player.decrease_balance(100)
        expected_balance = 200-100
        self.assertEqual(player.balance,expected_balance)

    def test_add_hand(self):
        name = 'Jun'
        balance = 200
        player = Player(name,balance)

        card1 = Card('Heart',1,True,1)
        card2 = Card('Spade',5,True,5)

        player.add_hand(card1)
        player.add_hand(card2)

        self.assertEqual(player.hand[0],card1)
        self.assertEqual(player.hand[1],card2)
    
    def test_empty_hand(self):
        name = 'Jun'
        balance = 200
        player = Player(name,balance)

        card1 = Card('Heart',1,True,1)
        card2 = Card('Spade',5,True,5)

        player.add_hand(card1)
        player.add_hand(card2)

        self.assertEqual(player.hand[0],card1)
        self.assertEqual(player.hand[1],card2)

        player.empty_hand()
        emtpy_list = list()
        self.assertEqual(player.hand,emtpy_list)

    def test_show_hand(self):
        name = 'Jun'
        balance = 200
        player = Player(name,balance)

        card1 = Card('Heart',1,True,1)
        card2 = Card('Spade',5,True,5)

        player.add_hand(card1)
        player.add_hand(card2)

        expected_hand=[['Heart',1],['Spade',5]]
        self.assertEqual(player.show_hand(),expected_hand)

    def test_faceUp_all_cards_When_Face_Down(self):
        name = 'Jun'
        balance = 200
        player = Player(name,balance)

        card1 = Card('Heart',1,False,1)
        card2 = Card('Spade',5,False,5)

        player.add_hand(card1)
        player.add_hand(card2)

        expected_hand=[['FaceDown'],['FaceDown']]
        self.assertEqual(player.show_hand(),expected_hand)


    def test_faceUp_all_cards(self):
        name = 'Jun'
        balance = 200
        player = Player(name,balance)

        card1 = Card('Heart',1,False,1)
        card2 = Card('Spade',5,False,5)

        player.add_hand(card1)
        player.add_hand(card2)

        expected_hand=[['FaceDown'],['FaceDown']]
        self.assertEqual(player.show_hand(),expected_hand)

        player.faceUp_all_cards()

        expected_hand=[['Heart',1],['Spade',5]]
        self.assertEqual(player.show_hand(),expected_hand)

    def test_is_black_jack_when_black_jack(self):
        name = 'Jun'
        balance = 200
        player = Player(name,balance)

        card1 = Card('Heart',1,False,1)
        card2 = Card('Spade',10,False,10)

        player.add_hand(card1)
        player.add_hand(card2)
        
        self.assertEqual(player.is_black_jack(),True)
    
    def test_is_black_jack_when_NOT_black_jack(self):
        name = 'Jun'
        balance = 200
        player = Player(name,balance)

        card1 = Card('Heart',1,False,1)
        card2 = Card('Spade',9,False,9)

        player.add_hand(card1)
        player.add_hand(card2)
        
        self.assertEqual(player.is_black_jack(),False)

    def test_calc_hand_Two_A_Test(self):
        name = 'Jun'
        balance = 200
        player = Player(name,balance)

        card1 = Card('Heart',"A",False,11)
        card2 = Card('Spade',"A",False,11)
        card3 = Card('Diamond',"A",False,11)

        player.add_hand(card1)
        player.add_hand(card2)
        player.add_hand(card3)

        actual_result = player.calc_hand()
        expected_result = 13

        self.assertEqual(actual_result,expected_result)

    def test_calc_hand_No_A_Test(self):
        name = 'Jun'
        balance = 200
        player = Player(name,balance)

        card1 = Card('Heart',"10",False,10)
        card2 = Card('Spade',"10",False,10)
        card3 = Card('Diamond',"10",False,10)
        card4 = Card('Clover',"10",False,10)

        player.add_hand(card1)
        player.add_hand(card2)
        player.add_hand(card3)
        player.add_hand(card4)

        actual_result = player.calc_hand()
        expected_result = 40

        self.assertEqual(actual_result,expected_result)
    
    def test_calc_hand_A_should_be_value_11_test(self):
        name = 'Jun'
        balance = 200
        player = Player(name,balance)

        card1 = Card('Heart',"A",False,11)
        card2 = Card('Spade',"2",False,2)

        player.add_hand(card1)
        player.add_hand(card2)

        actual_result = player.calc_hand()
        expected_result = 13

        self.assertEqual(actual_result,expected_result)


if __name__ == '__main__':
    unittest.main()