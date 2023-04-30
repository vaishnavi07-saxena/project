'''A Game of Dice
In this project, we will look at how you can emulate a player throwing a set of dice. Then we
will look at how you can store these dice in a pile the player wants to keep. you write a game where
you throw dice to determine the outcome, this is one way to store the results for later use. example,
normal dice with six eyes. The program will work no matter how many eyes your dice have.'''


import random

l=[1,2,3,4,5,6]
ans=random.choice(l)

if ans==1:
    print(' _____\n|     |\n|  o  |\n|     |\n|_____|')
elif ans==2:
    print(' _____\n|     |\n| o o |\n|     |\n|_____|')
elif ans==3:
    print(' _____\n|     |\n| o o |\n|  o  |\n|_____|')
elif ans==4:
    print(' _____\n|     |\n| o o |\n| o o |\n|_____|')
elif ans==5:
    print(' _____\n| o o |\n|  o  |\n| o o |\n|_____|')
elif ans==6:
    print(' _____\n| o o |\n| o o |\n| o o |\n|_____|')
