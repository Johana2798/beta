'''
Dev: Johana Moncayo 
Description:
Get player Name
Generate two Randow Number into 2 dices 
Dice 1: 1-6
Dice 2: 1-6
print dices values 
'''

import os 
os.system('clear')
print("::: WELCOME TO MY PARCHIS :::")

#print("player name:")

player_name= input("player name:")
dice1 = randint(1,6)
dice2 = randint(1,6)

print(f"dice 1:{dice1}")
print(f"dice 2:{dice2}")