
from art import logo
from replit import clear
import random

cards = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

#function that does the sum of cards in hands. Input are cards  
def sum_hand(hand):
  sum_in_hand = 0
  for card in hand:
    sum_in_hand += cards[card]
  return sum_in_hand
  
#function that choose what will be the value "A" based on the current sum of cards in hand
def choose_a(hand):
  s = sum_hand(hand)
  if s > 21:  #when sum>21
    if cards["A"] == 11:  #if A = 11
      if hand.count('A') == 2:  #if there are two "A" in the hand
          return 6      #the sum will be like one A is 11 and the other A is 1
      else:  # if there is a max of one A. #from a=11 to a=1 directly
        return 1
    else: # if A is 6 or 1
      return 1  
  else:  #if sum<=21
    if hand.count("A") > 2:
      return 1
    else:
      return cards["A"]

print(logo)
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

#game main loop
while start == "y":
  sum_player = 0
  sum_pc = 0
  clear()
  print(logo)
  
  #cards:
  player_cards = []
  computer_cards = []

  #computer first 2 cards
  for i in range(2):
    computer_cards.append(random.choice(list(cards)))
  cards["A"] = choose_a(computer_cards)  #decide for value of A
  sum_pc = sum_hand(computer_cards)

  #this loop will add cards to computer hand until sum of hands reach value 17
  while sum_pc < 17: 
    computer_cards.append(random.choice(list(cards)))
    cards["A"] = choose_a(computer_cards) 
    sum_pc = sum_hand(computer_cards)
  
  #player, first 2 cards
  cards["A"] = 11 #reset "A" to 11  
  #player_cards = ["10", "6"]
  for i in range(2):
    player_cards.append(random.choice(list(cards)))
  cards["A"] = choose_a(player_cards)
  sum_player = sum_hand(player_cards)
  
  
   
  print(f"You have: {player_cards}, score: {sum_player}")
  print(f"Dealer's first card is: {computer_cards[0]}\n")
  
  #sum player
  if sum_player == 21:
    clear()
    print(logo)
    another_card = "n"
    print(f"You have Black Jack: {player_cards}, score: {sum_player}")
    if sum_pc == 21:
      print(f"Dealer has also Black Jack: {computer_cards}")
      print("It's a draw!")
    else:
      print("You win!")
      print(f"Dealer has: {computer_cards}, {sum_pc}")
  else:
    another_card = input("Type 'y' to get another card, or 'n' to pass: ")
  
    #second loop for another card
  while another_card == "y":
    clear()
    print(logo)
    player_cards.append(random.choice(list(cards)))
    cards["A"] = choose_a(player_cards)
    sum_player = sum_hand(player_cards)
    
    if sum_player > 21:
      print(f"You have: {player_cards}, score: {sum_player}")
      print(f"Dealer has: {computer_cards[:2]}, score: {sum_hand(computer_cards[:2])}")
      print("Bust! Dealer wins!")
      break
      
    elif sum_player == 21:
      print(f"You have: {player_cards}, score: {sum_player}")
      print(f"Dealer has: {computer_cards}, score: {sum_pc}")
      if sum_pc == 21:
        print("Push! It's a draw.")
      else:
        print("You win!")
      break
    
    print(f"Your cards: {player_cards}, score: {sum_player}")
    print(f"Dealer's first card is: {computer_cards[0]}\n")
    
    another_card = input("Type 'y' to get another card, or 'n' to pass: ")
  

  if sum_player < 21:
    clear()
    print(logo)
    print(f"You have: {player_cards}, score: {sum_player}")
    print(f"Dealer has: {computer_cards}, score: {sum_pc}")    

    if sum_player < sum_pc < 22:
      print("Dealer wins!")
    elif sum_player == sum_pc:
      print("Push! It's a draw.")
    else:
      print("You win!")

  start = input("Type 'y' if you want to play again: ")
