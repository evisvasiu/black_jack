
from art import logo
from replit import clear
import random

a = 11 #function: choose_a() will make a = 1 if hands score becomes greater than 10

cards = {"A": a, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

  
def sum_hand(hand):
  sum_in_hand = 0
  for card in hand:
    sum_in_hand += cards[card]
  return sum_in_hand
def choose_a(s):
  if s > 10:
    if s == 22:
      return 6
    else:
      return 1
  else:
    return 11

print(logo)
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while start == "y":
  sum_player = 0
  sum_pc = 0
  clear()
  print(logo)
  #player cards:
  player_cards = []
  computer_cards = []

  #player, first hand
  for i in range(2):
    player_cards.append(random.choice(list(cards)))
  sum_player = sum_hand(player_cards)
  
  #computer possible cards
  for i in range(2):
    computer_cards.append(random.choice(list(cards)))
  sum_pc = sum_hand(computer_cards)
 
  while sum_pc < 17:
    computer_cards.append(random.choice(list(cards)))
    pc_a = choose_a(sum_pc)
    sum_pc = sum_hand(computer_cards)
  
  
  
  print(f"Your cards: {player_cards}, score: {sum_player}")
  print(f"Computer first card: {computer_cards[0]}\n")
  
  #sum player
  if sum_player == 21:
    print(f"You have Black Jack: {player_cards}, score: {sum_player}")
    if sum_pc == 21:
      print(f"Computer has also Black Jack: {computer_cards}")
      print("Draw!")
    else:
      print("You win!")
      print(f"Computer cards: {computer_cards}")
  else:
    another_card = input("Type 'y' to get another card, or 'n' to pass: ")

  while another_card == "y":
    clear()
    print(logo)
    player_cards.append(random.choice(list(cards)))
    a = choose_a(sum_player)
    sum_player = sum_hand(player_cards)
    
    if sum_player > 21:
      print(f"You have: {player_cards}, score: {sum_player}")
      print(f"Computer has: {computer_cards[:2]}")
      print("Burst")
      break
      
    elif sum_player == 21:
      print(f"You have Black Jack: {player_cards}, score: {sum_player}")
      if sum_pc == 21:
        print(f"Computer has Black Jack: {computer_cards}")
        print("Draw!")
      else:
        print(f"Computer has Black Jack: {computer_cards}")
        print("You win!")
      break
    
    
    
    
    
    print(f"Your cards: {player_cards}, score: {sum_player}")
    print(f"Computer first card: {computer_cards[0]}\n")
    
    another_card = input("Type 'y' to get another card, or 'n' to pass: ")
  

  if sum_player < 21:
    clear()
    print(logo)
    print(f"Your cards: {player_cards}, score: {sum_player}")
    print(f"Computer cards: {computer_cards}, score: {sum_pc}")    

    if sum_player < sum_hand(computer_cards) < 22:
      print("You loose")
    elif sum_player == sum_hand(computer_cards):
      print("You draw")
    else:
      print("You win!")
  
  
  
  start = input("Type 'y' if you want to play again: ")


    
    
    

  
