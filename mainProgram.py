from Deck import Deck
from Player import Player
from Dealer import Dealer
import os

class MainProgram():

    def __init__(self):
        self.clear = lambda: os.system('cls')

    def start_game(self):

        #Get players infomation
        user_name = input("Enter player name : ")
        balance = int(input("Enter your start balance : "))
        player = Player(user_name,balance)

        #Set Dealer
        dealer = Dealer()

        #Set deck
        deck = Deck()
        deck.generate_deck()
        deck.shuffle_deck()
        
        #Ask for shuffling again
        print("your deck is shuffled and ready")
        answer_set = [['y','yes'],['n','no']]
        while True:
            player.empty_hand()
            dealer.empty_hand()
            self.clear()
            want_shuffle_again = str(input("Do you want shuffle the deck again (y or n)?"))
            if want_shuffle_again.lower() in answer_set[0] :
                deck.shuffle_deck()
                print("Your deck is shuffled again.")
            elif want_shuffle_again.lower() in answer_set[1] :
                print("Not shuffled again!")
            else:
                print("Invalid input.")
        
        #############################
        # Player and Deck are ready.#
        #############################

            # Beting part.
            while True:
                betting_amount = int(input("How much do you want to bet? : "))
                if betting_amount > player.balance:
                    print("Your balance is not enough.")
                else:
                    print(f"Your betting money : {betting_amount}")
                    break
            
            #Distribute card
            print("Distributing card....")
            player.add_hand(deck.get_card(True))
            dealer.add_hand(deck.get_card(True))
            player.add_hand(deck.get_card(True))
            dealer.add_hand(deck.get_card(False))
            
            # print(f'Dealer\'s hand is {dealer.show_hand()}')
            # print(f'Player\'s hand is {player.show_hand()}')

            #card distribution end.
            #Check player's card for Black jack
            if player.is_black_jack():
                player.increase_balance(betting_amount)                
                # Game Start from first up to player input logic
                if self.ask_player_continue():
                    continue
                else:
                    print(f"Ending Game. Your balance is {player.balance}")
                    break
            else:
                print(self.show_both_side_cards(dealer,player))

                #Ask your if player want to recive more card
                busted = False
                while True:
                    if self.get_more_card():
                        player.add_hand(deck.get_card(True))
                        player_card_sum = player.calc_hand()
                        if player_card_sum > 21:
                            busted = True
                            self.clear()
                            print(f"Your Betting money : {betting_amount}")
                            print(self.show_both_side_cards(dealer,player))
                            print("You are BUSTED!")
                            break
                        elif player_card_sum == 21:
                            break
                        self.clear()
                        print(f"Your Betting money : {betting_amount}")
                        print(self.show_both_side_cards(dealer,player))
                    else:
                        break

                #Dealer turn
                #IF player busted skip this part and End Game
                
                if not busted:
                    dealer.faceUp_all_cards()
                    #Dealer keep getting card until dealer card_sum is not less then 17
                    while dealer.calc_hand() <= 17:
                        dealer.add_hand(deck.get_card(True))
                        self.clear()
                        print(f"Your Betting money : {betting_amount}")
                        print(self.show_both_side_cards(dealer,player))

                    self.clear()
                    print(f"Your Betting money : {betting_amount}")
                    print(self.show_both_side_cards(dealer,player))
                    if dealer.calc_hand() > 21:
                        print("Dealer Busted. Player WIN")
                        player.increase_balance(betting_amount)
                    else:
                        player_card_sum = player.calc_hand()
                        dealer_card_sum = dealer.calc_hand()

                        if dealer_card_sum == player_card_sum:
                            print("Tie.")
                        elif dealer_card_sum > player_card_sum:
                            print("Dealer Win")
                            player.decrease_balance(betting_amount)
                        else:
                            print("Player Win!")
                            player.increase_balance(betting_amount)

                if self.ask_player_continue():
                    continue
                else:
                    print(f"Ending Game. Your balance is {player.balance}")
                    break



    def show_both_side_cards(self, dealer, player):
        return f'Dealer: {dealer.show_hand()}\nPlayer: {player.show_hand()}'
    
    def get_more_card(self):
        while True:
            playerInput = str(input("Do you want recieve one more card(y,n)?"))
            if playerInput.lower() in ['y','yes']:
                return True
            elif playerInput.lower() in ['n', 'no']:
                return False
            else:
                print("Wrong input.")
                continue

    
    def ask_player_continue(self):
        while True:
            playerInput = str(input("Do you want to play again(y,n)?"))
            if playerInput.lower() in ['y','yes']:
                return True
            elif playerInput.lower() in ['n', 'no']:
                return False
            else:
                print("Wrong input.")
                continue



if __name__ == '__main__':
    main_program = MainProgram()
    main_program.start_game()  