import random
from art import logo
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
playing = True
print(logo)
while playing:
    wanna_play = input("Press y to play or n to exit :- ")
    if wanna_play == "y":
        ace = cards[0]
        user_cards =  random.sample(cards,2)
        print(f"Your cards {user_cards}")
        computer_cards = random.sample(cards,2)
        print(f"Computer cards {computer_cards}")
        drawing_user_card = False
        while not drawing_user_card:
            added_user_cards = sum(user_cards)
            added_computer_cards = sum(computer_cards)
            if added_computer_cards == 20:
                print("Computer has blackjack, You lose")
                drawing_user_card = True
            elif added_user_cards == 20:
                print("You have blackjack, You won")
                drawing_user_card = True
            else:
                if added_user_cards > 20:
                    for i in user_cards:
                        if i == ace:
                            ace = 1
                            if added_user_cards > 20:
                                print("You lose, You have blackjack")
                                drawing_user_card = True
                            else:
                                another_card = input("Press y to draw another card or n to continue :- ")
                                if another_card == "y":
                                    int_of_card = random.sample(cards,1)
                                    value_of_int = user_cards.append(int_of_card)
                                    sum_of_user_cards = user_cards
                                    print(f"User Cards {sum_of_added_cards}")
                                    added_user_cards = sum(sum_of_user_cards)
                                    print(f"Your cards {added_user_cards}")
                                if another_card == "n":
                                    drawing_computer_card = True
                                    while drawing_computer_card:
                                        if added_computer_cards < 17:
                                            int_of_card = random.sample(cards,1)
                                            print(f"Computer has drawn this card {int_of_card}")
                                            final_after_drawn = computer_cards.append(int_of_card)
                                            sum_of_added_cards = computer_cards
                                            print(f"Computer Cards {sum_of_added_cards}") 
                                            drawing_computer_card = False
                                        else:
                                            print(computer_cards)
                                            drawing_computer_card = False
                                    if added_computer_cards > 20:
                                        print("You won, Computer has blackjack")
                                        drawing_user_card = True
                                    else:
                                        if added_user_cards > added_computer_cards:
                                            print("You win, The sum of your cards is greater than the sum of the computer cards.")
                                            drawing_user_card = True
                                        elif added_computer_cards > added_user_cards:
                                            print("You lose, The sum of the computer cards is greater than the sum of your cards.")
                                            drawing_user_card = True
                                        else:
                                            print("Draw, The sum of both the cards are equal")
                                        drawing_user_card = True
                        else:
                            print("You lose")
                            drawing_user_card = True
                else:
                    another_card = input("Press y to draw another card or n to continue :- ")
                    if another_card == "y":
                        int_of_card = random.sample(cards,1)
                        value_of_int = user_cards.append(int_of_card)
                        sum_of_user_cards = user_cards
                        print(f"User Cards {sum_of_user_cards}")
                        added_user_cards = sum(sum_of_user_cards)
                        print(f"Your cards {added_user_cards}")
                    if another_card == "n":
                        drawing_computer_card = True
                        while drawing_computer_card:
                            if added_computer_cards < 17:
                                int_of_card = random.sample(cards,1)
                                print(f"Computer has drawn this card {int_of_card}")
                                final_after_drawn = computer_cards.append(int_of_card)
                                sum_of_added_cards = computer_cards
                                print(f"Computer Cards {sum_of_added_cards}")
                                if sum(sum_of_added_cards) > 20:
                                    print("You win")
                                    drawing_user_card = True
                                else:
                                    drawing_computer_card = False
                                drawing_computer_card = False
                            else:
                                print(computer_cards)
                                drawing_computer_card = False
                        if added_computer_cards > 20:
                            print("You won, Computer has blackjack")
                            drawing_user_card = True
                        else:
                            if added_user_cards > added_computer_cards:
                                print("You win, The sum of your cards is greater than the sum of the computer cards.")
                                drawing_user_card = True
                            elif added_computer_cards > added_user_cards:
                                print("You lose, The sum of the computer cards is greater than the sum of your cards.")
                                drawing_user_card = True
                            else:
                                print("Draw, The sum of both the cards are equal")
                            drawing_user_card = True
    elif wanna_play == "n":
        playing = False
    else:
        print("Invalid Input")
        playing = False
                        

                        
