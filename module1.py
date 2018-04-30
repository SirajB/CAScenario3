#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     19/10/2012
# Copyright:   (c) user 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
gameBoard = 20
player1 = 0
player2 = 0

SandL = [6,14,] # All spaces that whill bring you up or down
UpandDown = [17,3,] # All corosponding spaces to SandL

while True:
     if player1 >= 20 or player2 >= 20: # Keeps the score less then or equil to 20
          #Winning statment

        if player1 < player2:
            print ('Player 2 has won')
            break
        else:
            print ('Player 1 has won')
            break

            #PLAYER 1
     play1 = input('Press enter to continue')
     if play1 == '':
        print (' Player 1 turn.')
        roll = random.randint(1,6)
        print (' You rolled a', roll)

               #To tell if you are on a snake or a ladder and where you will end up
        if player1 in SandL:
            player1 = SandL.index(player1)
            print ('you are at space', UpandDown[player1])
        else:
            player1 = player1 + roll
            print ('you are at space', player1)

          #To check if the roll is >20 if it is reset pos
        if player1 > 20:
            player1 = player1 - roll

     else:
         break


            #PLAYER 2
     play2 = input('Press enter to continue')
     if play2 == '':
        print (' Player 2 turn.')
        roll = random.randint(1,6)
        print (' You rolled a', roll)


           #To tell if you are on a snake or a ladder and where you will end up
        if player2 in SandL:
            player2 = SandL.index(player2)
            print  ('you are at space', UpandDown[player2])
        else:
            player2 = player2 + roll
            print ('you are at space', player2)


          #To check if the roll is >20 if it is reset pos
        if player2 > 20:
            player = player2 - roll
     else:
        break