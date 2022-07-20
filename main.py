
from art import logo
from replit import clear
import random

a = 11 #function: choose_a() will make a = 1 if hands score becomes greater than 10

cards = {"A": a, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

#function that does the sum of cards in hands. Input are cards  
def sum_hand(hand):
  sum_in_hand = 0
  for card in hand:
    sum_in_hand += cards[card]
  return sum_in_hand
  
#function that choose what will be the value "A" based on the current sum of cards in hand
def choose_a(hand):
  s = sum_hand(hand)
  if s > 10:
    if (hand[0] == "A" or hand[1] == "A") and (hand[0] != hand[1]) and len(hand)<3:
      cards["A"] = 11
    elif (hand[0] == hand[1] == "A") and len(hand)<3:  #when first cards are "A"
      cards["A"] = 6
    elif (hand[0] == hand[1] == "A"):  #when three "A"
      if hand[-1] == "A":
        cards[hand[0]] = 11
        cards["A"] = 1
      elif cards[hand[-1]] == 10:
        cards["A"] = 1
      elif cards[hand[-1]] < 10:
        cards["A"] = 6
    if s > 21:
      cards["A"] = 1
  else:
    cards["A"] = 11

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
  cards["A"] = 11
  for i in range(2):
    computer_cards.append(random.choice(list(cards)))
  choose_a(computer_cards)  #check for double A
  sum_pc = sum_hand(computer_cards)

  #this loop will add cards to computer hand until sum of hands reach value 17
  while sum_pc < 17: 
    computer_cards.append(random.choice(list(cards)))
    choose_a(computer_cards) 
    sum_pc = sum_hand(computer_cards)
  
  #player, first 2 cards
  cards["A"] = 11 #reset "A" to 11  
  for i in range(2):
    player_cards.append(random.choice(list(cards)))

  choose_a(player_cards)  #check for double A
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
    choose_a(player_cards)
    sum_player = sum_hand(player_cards)
    
    if sum_player > 21:
      print(f"You have: {player_cards}, score: {sum_player}")
      if sum_hand(computer_cards[:2]) == 22:
        cards["A"] = 6
      else:
        cards["A"] = 11
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
