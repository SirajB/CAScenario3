#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HAMBREPOS1
#
# Created:     16/11/2012
# Copyright:   (c) HAMBREPOS1 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# # Having these two hashtags mean that I have finished my comment for that chosen segment# #

from colorama import init
from colorama import Fore, Back, Style
init()

import csv
#Everything above this is so that I am able to import it and use it in my game#



game_array=[
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','','']]
#This array is what the background of the game is based off. The co-ordinates of this is how the robot moves and how the people and the base are initialy spawned.#

#game_array [0][0]='R'#
#game_array [0][2]='P'#
#game_array [2][7]='P'#
#game_array [3][6]='B'#
#game_array [6][4]='P'# #Ignore this, this was to help me earlier on in this course#
#game_array [6][9]='P'#



rowcount=1 #This and colcount (columncount) is  so that the game_array can pick it up and I can make the background of the game from this
colcount=1 #From this I can also begin to generate the people, robot and basecamp [See def playgame() ]#

robot_original=150 #This is the original power units that enable the robots power to change per level#
robot_power=150# Robot power units#
pom=4#POM=People On Map#
passanger_bay=0#Amount in Passanger Bay#`
maxpass=2

passangerbaycost=0
movingontograsscost=0
movingontoicecost=0
movingontorockscost=0
#All of this sets the power units depending on the traction#


p1x=0
p1y=2
p2x=2
p2y=7
p3x=6
p3y=4
p4x=6
p4y=9
r1x=0
r1y=0
b1x=3
b1y=6
#All of these are the variable names for the people (p1x,p1y ect.) robot (r1x,r1y) and base camp (b1x,b1y)
#The numbers next to each variable represent their initial spawn points. The only one that I have made that is able to change
#Is the robot#





def show_menu():# This is the first menu you will see when running my game The lines underneath this show GAMES MENU#
    print (Fore.CYAN+Back.BLACK+Style.BRIGHT+'  _____          __  __ ______  _____      __  __ ______ _   _ _    _'+Fore.RESET+Back.RESET+Style.RESET_ALL)
    print (Fore.RED+Back.BLACK+Style.BRIGHT+' / ____|   /\   |  \/  |  ____|/ ____|    |  \/  |  ____| \ | | |  | |'+Fore.RESET+Back.RESET+Style.RESET_ALL)
    print (Fore.GREEN+Back.BLACK+Style.BRIGHT+'| |  __   /  \  | \  / | |__  | (___      | \  / | |__  |  \| | |  | |'+Fore.RESET+Back.RESET+Style.RESET_ALL)
    print (Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'| | |_ | / /\ \ | |\/| |  __|  \___ \     | |\/| |  __| | . ` | |  | |'+Fore.RESET+Back.RESET+Style.RESET_ALL)
    print (Fore.CYAN+Back.BLACK+Style.BRIGHT+'| |__| |/ ____ \| |  | | |____ ____) |    | |  | | |____| |\  | |__| |'+Fore.RESET+Back.RESET+Style.RESET_ALL)
    print (Fore.RED+Back.BLACK+Style.BRIGHT+' \_____/_/    \_\_|  |_|______|_____/     |_|  |_|______|_| \_|\____/'+Fore.RESET+Back.RESET+Style.RESET_ALL)
    print (Fore.GREEN+Back.BLACK+Style.BRIGHT+'**********************************************************************'+Fore.RESET+Back.RESET+Style.RESET_ALL)
    print (Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'**********************************************************************'+Fore.RESET+Back.RESET+Style.RESET_ALL)

    print ("")#This is so that the game is a little bit neater#
    print (Fore.CYAN+'[1] Play')#Options the player can choose, the reason for no Fore.RESET is because this can apply to everything in this menu#
    print ('[2] Shop')
    print ('[3] Exit')
    gamemenuinput()#Moves the program along to gamemenuinput#

def gamemenuinput():#This is to make sure that if an option is chosen, the game respnds correctly#
    global game
    choice = input("Please Choose An Option ")
    if choice == "1":#Pressing 1 outputs the game#
        playgame()
    elif choice == "2":#Pressing 2 takes the player to the shop#
        shop()
    elif choice == "3":#Pressing 3 closes the game#
        game = False
    else:
        show_menu()#If no option is chosen, loop back to the starting menu#

def playgame():#This is how the option 1 works
    game = csv.reader(open('landscape.csv'))
    global rowcount,colcount#This makes rowcount and colcount global and able to use everywhere#
    global cell
    rowcount=0#Reson for this to be 0 is so that I can generate spawns for my variables.#
    colcount=0

    for row in game:#This is for everyrow in my game#
        for cell in row:#For everyspace in my game#
            game_array[rowcount][colcount] = cell#This is where the rowcount and colcount = 0 come into place.#
            character=' '
            if rowcount == p1x and colcount ==p1y:#All of this is how each person how the robot and basecamp are shown on the map initially#
                character = Fore.YELLOW+'P'+Fore.RESET
            if rowcount == p2x and colcount ==p2y:
                character = Fore.YELLOW+'P'+Fore.RESET
            if rowcount == p3x and colcount ==p3y:
                character = Fore.YELLOW+'P'+Fore.RESET
            if rowcount == p4x and colcount ==p4y:
                character = Fore.YELLOW+'P'+Fore.RESET
            if rowcount == r1x and colcount ==r1y:
                character = Fore.CYAN+'R'+Fore.RESET
            if rowcount == b1x and colcount ==b1y:
                character = Fore.RED+'B'+Fore.RESET
            if cell == 'grass':#From Excel if it said grass make it green, ice = white rocks=red#
                    print (Back.GREEN+Style.BRIGHT+Fore.BLACK+('| '+character+' |')+Back.RESET+Style.RESET_ALL,end='')
            elif cell == 'ice':
                print(Back.WHITE+Style.BRIGHT+Fore.BLACK+('| '+character+' |')+Back.RESET+Style.RESET_ALL,end='')
            elif cell == 'rocks':
                print(Back.RED+Style.BRIGHT+Fore.BLACK+('| '+character+' |')+Back.RESET+Style.RESET_ALL,end='')
            colcount =colcount+1#adds 1 to colcount so that it can verify and make it work with game_array#
        print()
        rowcount =rowcount+1 #adds 1 to rowcount so that it can verify and make it work with game_array#
        colcount=0 # This resets colcount so that I can use it again#
    pickup()#Takes this to pickup#
    robot()#Takes this to robot#







def robot():
    global robot_power#sets robot_power to be global so that I may use it more then once in this function#
    global r1x,r1y#Makes the robot global so that I am able to use it everywhere in this coding.#
    choice = input ('You May Move Up (w) Down (s) Left (a) Right (d) ')#Telling the person playing the controls
    print ("Robot Power is at")
    reducepower()#Prints how much power the robot has#
    print ("Power Units")
    while choice not in ("w","s","a","d"):
        choice =input ("You can only use w,s,a,d ")#If they choose something that is not defined it will print this#
    if choice == "w" and r1x>=1:
        r1x=r1x-1
    elif choice =="s"and r1x<=8:
        r1x=r1x+1
    elif choice =="a"and r1y>=1:
        r1y=r1y-1
    elif choice == "d"and r1y<=8:
        r1y=r1y+1#All of these are the borders that control where the robot can and can't move#
    else:
        print (Fore.RED+Style.BRIGHT+Back.CYAN+"Robot Says No"+Fore.RESET+Style.RESET_ALL+Back.RESET)#If they do move off the map, this will be printed in red with a background cyan#
    playgame()#Loops back to outputting the game background with the new locations#


def pickup():#This is how the pickup system works#
    global maxpass
    global robot_power
    global game
    global pom
    global p1x,p1y
    global p2x,p2y
    global p3x,p3y
    global p4x,p4y
    global passanger_bay
    #All the above allows me to use these variables more then once#
    if (r1x == p1x) and (r1y == p1y):
        p1x= -1
        p1y= -1
        passanger_bay=passanger_bay+1#Adds +1 to the passanger bay and moves the person off the map therefore, he is 'picked up'#
        print ((Fore.GREEN+"You have"))
        print (passanger_bay)
        print(("People in your passanger bay"+Fore.RESET))#Tells the player how many people are in his passanger bay#
        pom=pom-1#Takes away 1 from the people on the map#
        print (Fore.MAGENTA+Style.BRIGHT+"You Still Have "+Fore.RESET+Style.RESET_ALL)
        print (pom)
        print (Fore.MAGENTA+Style.BRIGHT+"Left To Pick Up "+Fore.RESET+Style.RESET_ALL)
    if (r1x == p2x) and (r1y == p2y):
        p2x= -1
        p2y= -1
        passanger_bay=passanger_bay+1#Adds +1 to the passanger bay and moves the person off the map therefore, he is 'picked up'#
        print ((Fore.GREEN+"You have"))
        print (passanger_bay)
        print(("People in your passanger bay"+Fore.RESET))#Tells the player how many people are in his passanger bay#
        pom=pom-1#Takes away 1 from the people on the map#
        print (Fore.MAGENTA+Style.BRIGHT+"You Still Have "+Fore.RESET+Style.RESET_ALL)
        print (pom)
        print (Fore.MAGENTA+Style.BRIGHT+"Left To Pick Up "+Fore.RESET+Style.RESET_ALL)#Tells how many left to pick up#
    if (r1x == p3x) and (r1y == p3y):
        p3x = -1
        p3y = -1
        passanger_bay=passanger_bay+1#Adds +1 to the passanger bay and moves the person off the map therefore, he is 'picked up'#
        print ((Fore.GREEN+"You have"))
        print (passanger_bay)
        print(("People in your passanger bay"+Fore.RESET))#Tells the player how many people are in his passanger bay#
        pom=pom-1#Takes away 1 from the people on the map#
        print (Fore.MAGENTA+Style.BRIGHT+"You Still Have "+Fore.RESET+Style.RESET_ALL)
        print (pom)
        print (Fore.MAGENTA+Style.BRIGHT+"Left To Pick Up "+Fore.RESET+Style.RESET_ALL)#Tells how many left to pick up#
    if (r1x == p4x) and (r1y == p4y):
        p4x = -1
        p4y = -1
        passanger_bay=passanger_bay+1#Adds +1 to the passanger bay and moves the person off the map therefore, he is 'picked up'#
        print ((Fore.GREEN+"You have"))
        print (passanger_bay)
        print(("People in your passanger bay"+Fore.RESET))#Tells the player how many people are in his passanger bay#
        pom=pom-1#Takes away 1 from the people on the map#
        print (Fore.MAGENTA+Style.BRIGHT+"You Still Have "+Fore.RESET+Style.RESET_ALL)
        print (pom)
        print (Fore.MAGENTA+Style.BRIGHT+"Left To Pick Up "+Fore.RESET+Style.RESET_ALL)#Tells how many left to pick up#
    if (r1x ==b1x) and (r1y == b1y):
        if passanger_bay==0:
            print (Fore.RED+Style.BRIGHT+"Bad Robot, BAD! Go And Pick Up Some People!"+Fore.RESET+Style.RESET_ALL)#If the robot enters base camp with no people this message would be outputted#
            print (Fore.MAGENTA+Style.BRIGHT+"You Still Have "+Fore.RESET+Style.RESET_ALL)
            print (pom)#Tells the player how many people are left ot pick up#
            print (Fore.MAGENTA+Style.BRIGHT+"Left To Pick Up "+Fore.RESET+Style.RESET_ALL)
        if passanger_bay==1:
            print (Fore.GREEN+Style.BRIGHT+"You Have Dropped"+Fore.RESET+Style.RESET_ALL)
            print(passanger_bay)
            print (Fore.GREEN+Style.BRIGHT+"Passangers"+Fore.RESET+Style.RESET_ALL)#Telling the player how many people they have dropped in the base camp#
            passanger_bay=passanger_bay-passanger_bay
            print (Fore.MAGENTA+Style.BRIGHT+"You Still Have "+Fore.RESET+Style.RESET_ALL)
            print (pom)
            print (Fore.MAGENTA+Style.BRIGHT+"Left To Pick Up "+Fore.RESET+Style.RESET_ALL)#Telling the player how many people they have left to pick up#
        if passanger_bay==2:
           print (Fore.GREEN+Style.BRIGHT+"You Have Dropped"+Fore.RESET+Style.RESET_ALL)
           print(passanger_bay)
           print (Fore.GREEN+Style.BRIGHT+"Passangers"+Fore.RESET+Style.RESET_ALL)#Telling the player how many people they have dropped in the base camp#
           passanger_bay=passanger_bay-passanger_bay
           print (Fore.MAGENTA+Style.BRIGHT+"You Still Have "+Fore.RESET+Style.RESET_ALL)
           print (pom)
           print (Fore.MAGENTA+Style.BRIGHT+"Left To Pick Up "+Fore.RESET+Style.RESET_ALL)#Telling the player how many people they have left to pick up#
        if passanger_bay==3:
           print (Fore.GREEN+Style.BRIGHT+"You Have Dropped"+Fore.RESET+Style.RESET_ALL)
           print(passanger_bay)
           print (Fore.GREEN+Style.BRIGHT+"Passangers"+Fore.RESET+Style.RESET_ALL)#Telling the player how many people they have dropped in the base camp#
           passanger_bay=passanger_bay-passanger_bay
           print (Fore.MAGENTA+Style.BRIGHT+"You Still Have "+Fore.RESET+Style.RESET_ALL)
           print (pom)
           print (Fore.MAGENTA+Style.BRIGHT+"Left To Pick Up "+Fore.RESET+Style.RESET_ALL)#Telling the player how many people they have left to pick up#
        if passanger_bay==4:
           print (Fore.GREEN+Style.BRIGHT+"You Have Dropped"+Fore.RESET+Style.RESET_ALL)
           print(passanger_bay)
           print (Fore.GREEN+Style.BRIGHT+"Passangers"+Fore.RESET+Style.RESET_ALL)#Telling the player how many people they have dropped in the base camp#
           passanger_bay=passanger_bay-passanger_bay
           print (Fore.MAGENTA+Style.BRIGHT+"You Still Have "+Fore.RESET+Style.RESET_ALL)
           print (pom)
           print (Fore.MAGENTA+Style.BRIGHT+"Left To Pick Up "+Fore.RESET+Style.RESET_ALL)#Telling the player how many people they have left to pick up#
        if pom==0 and passanger_bay==0:
            print(Fore.CYAN+Back.BLACK+Style.BRIGHT+'____    ____  ______    __    __     ____    __    ____  __  .__   __.'+Fore.RESET+Back.RESET+Style.RESET_ALL)
            print(Fore.RED+Back.BLACK+Style.BRIGHT+'\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  |'+Fore.RESET+Back.RESET+Style.RESET_ALL)
            print(Fore.GREEN+Back.BLACK+Style.BRIGHT+' \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  |'+Fore.RESET+Back.RESET+Style.RESET_ALL)
            print(Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  |'+Fore.RESET+Back.RESET+Style.RESET_ALL)
            print(Fore.CYAN+Back.BLACK+Style.BRIGHT+'    |  |    |  `--`' '       `--'          '                           '+Fore.RESET+Back.RESET+Style.RESET_ALL)
            print(Fore.RED+Back.BLACK+Style.BRIGHT+'    |__|     \______/   \______/         \__/  \__/     |__| |__| \__|'+Fore.RESET+Back.RESET+Style.RESET_ALL)
            print(Fore.GREEN+Back.BLACK+Style.BRIGHT+'')#This message would be outputted upon completion#

        if robot_power == 0 and pom ==0 and passanger_bay ==0:
            print(Fore.CYAN+Back.BLACK+Style.BRIGHT+'____    ____  ______    __    __     ____    __    ____  __  .__   __.'+Fore.RESET+Back.RESET+Style.RESET_ALL)
            print(Fore.RED+Back.BLACK+Style.BRIGHT+'\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  |'+Fore.RESET+Back.RESET+Style.RESET_ALL)
            print(Fore.GREEN+Back.BLACK+Style.BRIGHT+' \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  |'+Fore.RESET+Back.RESET+Style.RESET_ALL)
            print(Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  |'+Fore.RESET+Back.RESET+Style.RESET_ALL)
            print(Fore.CYAN+Back.BLACK+Style.BRIGHT+'    |  |    |  `--`' '       `--'          '                           '+Fore.RESET+Back.RESET+Style.RESET_ALL)
            print(Fore.RED+Back.BLACK+Style.BRIGHT+'    |__|     \______/   \______/         \__/  \__/     |__| |__| \__|'+Fore.RESET+Back.RESET+Style.RESET_ALL)
            print(Fore.GREEN+Back.BLACK+Style.BRIGHT+'')#This message would be outputted upon completion#










def reducepower():#everything for reduce power#
    global passangerbaycost
    global movingontograsscost
    global movingontoicecost
    global movingontorockscost
    global robot_power
    if cell == 'grass':
                robot_power=robot_power-passangerbaycost-movingontograsscost#calculates the amount of power deducted#
                print (robot_power)#If grass then this is how much power would be left after the equation above#
                if robot_power <=0:
                    robot_power=robot_power=0
                    print (robot_power)
                    print ('')
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'  @@@@@@@   @@@@@@  @@@@@@@@@@  @@@@@@@@'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+' !@@       @@!  @@@ @@! @@! @@! @@!'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'!@! @!@!@ @!@!@!@! @!! !!@ @!@ @!!!:!'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+':!!   !!: !!:  !!! !!:     !!: !!:'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+' :: :: :   :   : :  :      :   : :: :::'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print ('')
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'  @@@@@@  @@@  @@@ @@@@@@@@ @@@@@@@'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'@@!  @@@ @@!  @@@ @@!      @@!  @@@'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'@!@  !@! @!@  !@! @!!!:!   @!@!!@!'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'!!:  !!!  !: .:!  !!:      !!: :!!'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'  : :. :     ::    : :: :::  :   : :'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    input ('')
                    gameend()
                    game=False
    elif cell == 'ice':
                robot_power=robot_power-passangerbaycost-movingontoicecost#calculates the amount of power deducted#
                print (robot_power)#If ice then this is how much power would be left after the equation above#
                if robot_power <=0:
                    robot_power=robot_power=0
                    print (robot_power)
                    print ('')
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'  @@@@@@@   @@@@@@  @@@@@@@@@@  @@@@@@@@'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+' !@@       @@!  @@@ @@! @@! @@! @@!'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'!@! @!@!@ @!@!@!@! @!! !!@ @!@ @!!!:!'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+':!!   !!: !!:  !!! !!:     !!: !!:'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+' :: :: :   :   : :  :      :   : :: :::'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print ('')
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'  @@@@@@  @@@  @@@ @@@@@@@@ @@@@@@@'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'@@!  @@@ @@!  @@@ @@!      @@!  @@@'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'@!@  !@! @!@  !@! @!!!:!   @!@!!@!'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'!!:  !!!  !: .:!  !!:      !!: :!!'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'  : :. :     ::    : :: :::  :   : :'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    input()
                    gameend()
                    game=False
    elif cell == 'rocks':
                robot_power=robot_power-passangerbaycost-movingontorockscost#calculates the amount of power deducted#
                print (robot_power)#If rocks then this is how much power would be left after the equation above#
                if robot_power <=0:
                    robot_power=robot_power=0
                    print (robot_power)
                    print ('')
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'  @@@@@@@   @@@@@@  @@@@@@@@@@  @@@@@@@@'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+' !@@       @@!  @@@ @@! @@! @@! @@!'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'!@! @!@!@ @!@!@!@! @!! !!@ @!@ @!!!:!'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+':!!   !!: !!:  !!! !!:     !!: !!:'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+' :: :: :   :   : :  :      :   : :: :::'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print ('')
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'  @@@@@@  @@@  @@@ @@@@@@@@ @@@@@@@'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'@@!  @@@ @@!  @@@ @@!      @@!  @@@'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'@!@  !@! @!@  !@! @!!!:!   @!@!!@!'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'!!:  !!!  !: .:!  !!:      !!: :!!'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    print(Fore.RED+Back.BLACK+Style.BRIGHT+'  : :. :     ::    : :: :::  :   : :'+Fore.RESET+Back.RESET+Style.RESET_ALL)
                    input ('')
                    gameend()








def shop():
    print ('')#Just to keep things neat#
    print (Fore.CYAN+Back.BLACK+Style.BRIGHT+' _____   ____  ____   ____      __  __ ______ _   _ _    _'+Fore.RESET+Back.RESET+Style.RESET_ALL)
    print (Fore.RED+Back.BLACK+Style.BRIGHT+'|  __ \ / __ \|  _ \ / __ \    |  \/  |  ____| \ | | |  | |'+Fore.RESET+Back.RESET+Style.RESET_ALL)
    print (Fore.GREEN+Back.BLACK+Style.BRIGHT+'| |__) | |  | | |_) | |  | |   | \  / | |__  |  \| | |  | |'+Fore.RESET+Back.RESET+Style.RESET_ALL)
    print (Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'|  _  /| |  | |  _ <| |  | |   | |\/| |  __| | . ` | |  | |'+Fore.RESET+Back.RESET+Style.RESET_ALL)
    print (Fore.CYAN+Back.BLACK+Style.BRIGHT+'| | \ \| |__| | |_) | |__| |   | |  | | |____| |\  | |__| |'+Fore.RESET+Back.RESET+Style.RESET_ALL)
    print (Fore.RED+Back.BLACK+Style.BRIGHT+'|_|  \_\\____/|____/ \____/     |_|  |_|______|_| \_|\____/'+Fore.RESET+Back.RESET+Style.RESET_ALL)
    print (Fore.GREEN+Back.BLACK+Style.BRIGHT+'***********************************************************'+Fore.RESET+Back.RESET+Style.RESET_ALL)
    print (Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'***********************************************************'+Fore.RESET+Back.RESET+Style.RESET_ALL)
    print (Fore.GREEN+'[1] Traction')#Options they can choose, all printed out in green#
    print ('[2] Passanger Bay')
    print ('[3] Return to Game Menu')
    shopmenuinput()#Goes to shopmenuinput

def shopmenuinput():#As before, this is so that if an option is chosen, the game can correctly respond.#
    global game
    choice = input("Please Choose An Option ")
    if choice == "1":
        traction()#option 1 directs them to traction#
    elif choice == "2":
        passangers()#option 2 directs them to passangers#
    elif choice == "3":
        show_menu()#option three directs them back to the game menu#

def traction():
    print ('')#Keep things neat#
    print (Style.BRIGHT+Fore.YELLOW+'Ski''s, Tracks and Wheels!'+Style.RESET_ALL+Fore.RESET)#This is just so that they know what is here#
    print ('')
    print (Fore.YELLOW+'[1] Ski''s')#Options they can choose, all printed out in yellow#
    print ('[2] Tracks')
    print ('[3] Wheels')
    print ('[4] Return to Shop Menu')
    subtraction()#goes to subtraction#


def passangers():
    print ('')#keeps things neat#
    print (Style.BRIGHT+'Carry More Passangers!'+Style.RESET_ALL)#This is so they know what is here#
    print ('')
    print (Fore.BLUE+'[1] Large ')#Options they can choose, all printed out in blue#
    print ('[2] Medium')
    print ('[3] Small')
    print ('[4] Return to Shop Menu')
    subpassangers()#Goes to subpassangers#

def subtraction():#This is so that if they choose traction, the game can output the correct messages and correct additions#
    global game
    global movingontograsscost
    global movingontoicecost
    global movingontorockscost
    choice = input("Please Choose An Option")
    if choice == "1":
        print ('')
        print ('You now have Ski''s')#If 1 is chosen the robot now has ski's#
        movingontograsscost=movingontograsscost+3
        movingontoicecost=movingontoicecost+1
        movingontorockscost=movingontorockscost+3
        shop()
    elif choice == "2":
        print ('')
        print ('You now have Tracks')#If 2 is chosen the robot now has tracks#
        movingontograsscost=movingontograsscost+3
        movingontoicecost=movingontoicecost+3
        movingontorockscost=movingontorockscost+3
        shop()
    elif choice == "3":
        print ('')
        print ('You now have Wheels')#If 3 is chosen the robot now has wheels#
        movingontograsscost=movingontograsscost+1
        movingontoicecost=movingontoicecost+2
        movingontorockscost=movingontorockscost+3
        shop()
    elif choice == "4":
        shop()#If 4 is chosen, the player is redirected to game menu#


def subpassangers():#This is so that if they choose passangers, the game can output the correct messages and correct additions#
    global game
    global passangerbaycost
    global maxpass
    choice = input("Please Choose An Option ")
    if choice == "1":
        print ('')
        print ('You now have a Large Bay')#If 1 is chosen, the robot now has a large carrier bay#
        passangerbaycost=passangerbaycost=2
        maxpass=maxpass=3
        shop()
    elif choice == "2":
        print ('')
        print ('You now have a Medium Bay')#If 2 is chosen, the robot now has a medium carrier bay#
        passangerbaycost=passangerbaycost=1
        maxpass=maxpass=2
        shop()
    elif choice == "3":
        print ('')
        print ('You now have a Small Bay')#If 3 is chosen, the robot now has a small carrier bay#
        passangerbaycost=passangerbaycost=0
        maxpass=maxpass=1
        shop()
    elif choice == "4":
        shop()#If 4 is chosen, the player is redirected to game menu#


def gameend():
    game=True
    while (game == True):
        print ("YOU HAVE LOST LEAVE THE GAME!")
        choice=input('You have lost, press enter to end game[NOTE] this message will continue to loop if enter is not pressed')
        while choice=='':
            game = False
#main program loops#
#######################
## Main Program Loop ##
#######################
game = True
while (game == True):
    show_menu()#Keeps the game running#