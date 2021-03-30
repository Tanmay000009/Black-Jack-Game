import random
from art import logo
import os
import time 
print(logo)
game=input("Do you wanna play Blackjack?: type 'y' for 'yes' and 'any other key' for 'no' ")

def num_gen():
    a=random.randint(0,12)
    return a

def sum_list(a):
    sum=0
    for i in range(len(a)):
      sum+=a[i]
    return sum

while game=='y':
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  win=0
  
  yourCard=[]
  compHand=[]

  while game=="y":

    if (yourCard==[]):
      yourCard.append(cards[num_gen()])
      yourCard.append(cards[num_gen()])
      compHand.append(cards[num_gen()])
      compHand.append(cards[num_gen()])
    else:
      yourCard.append(cards[num_gen()])

    sum_player= sum_list(yourCard)
    sum_comp= sum_list(compHand)
    
    if sum_player > 21:
      for i in range(len(yourCard)):
        if yourCard[i]==11:
          yourCard[i]=1
    
    if( sum_comp == 21 ):
      print('''
            *********   
            
            Computer Wins  
            
            *********''')
      win=1
      break
    elif( sum_player == 21):
      print('''
            *********   
            
            You Won  
            
            *********''')
      win=1
      break
    elif( sum_comp>21 ):
      print('''
            *********   
            
            You Won  
            
            *********''')
      win=1
      break
    elif( sum_player>21 ):
      print('''
            *********   
            
            Computer Wins  
            
            *********''')
      win=1
      break

    print("Your cards: ",yourCard,' , current score: ',sum_player)

    print("Computer's first card: ",compHand[0])

    
    game=input("Type 'y' to get another card, press 'any other key' to pass:")

  if(win == 0):
    while sum_comp<17:
      compHand.append(cards[num_gen()])
      
      if sum_comp > 21:
        for i in range(len(compHand)):
          if compHand[i]==11:
            compHand[i]=1
    if (sum_comp == sum_player ):
        print("It's a draw")
    elif (sum_comp > sum_player ):
        print('''
              *********   
              
              Computer Wins  
              
              *********''')
    elif (sum_comp < sum_player ):
        print('''
              *********   
              
              You Won  
              
              *********''')
  
  print("Your cards: ",yourCard,' , score: ',sum_player)

  print("Computer's cards: ",compHand,' , score: ',sum_comp)
  
  game=input("Do you wanna play Blackjack?: type 'y' for 'yes' and 'any other key' for 'no' ")
  os.system("cls")
  print(logo)
