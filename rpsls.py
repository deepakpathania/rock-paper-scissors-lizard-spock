from random import randrange
import math

#converts string input from user to number
def convert_to_number(string):
    if string=="rock":
        number=0
    elif string=="spock":
        number=1
    elif string == "paper":
        number=2
    elif string == "lizard":
        number=3
    elif string == "scissors":
        number=4
    else :
        number = 1000
    return number

 #converts number to string for displaying selected options
def number_to_name(number):
    if number == 0:
        number = "rock"
    elif number == 1:
        number = "Spock"
    elif number == 2:
        number = "paper"
    elif number == 3:
        number = "lizard"
    elif number == 4:
        number = "scissors"
    return number

 #randomly selects computer's input and compares with user input to determine the winner       
def game(n):
    uinp=convert_to_number(n)
    if uinp !=1000:
        inp=randrange(0,5)
        diff=(uinp-inp)%5
        print "Player chose %s" % number_to_name(uinp)
        print "Computer chose %s" %number_to_name(inp)
        if diff==0:
            print "You guys tie"
        elif diff==1 or diff==2:
            print "Player wins"
        elif diff==3 or diff==4:
            print "Computer wins"
        else :
            print " "
        return 1
    else :
        print "Invalid input. Try again."
        return 0
number_of_plays=int(raw_input("How many times would you like to play ? "))
i=0
while i < number_of_plays:
    t=raw_input("Welcome to rock paper scissors lizard spock !! Choose your option : " )
    a=1
    a = game(t)
    i+=1
    if a==0:
        print "Added a turn"
        number_of_plays+=1
raw_input("Press whatever you feel like to quit")    
        
