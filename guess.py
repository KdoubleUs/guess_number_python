#first generate a random number between 1-100 

import random
num=0
while num == 0: 
    # randomNumber = random.randint(0,100)
    # print(randomNumber)
   
    player_Guess=[int(player_Guess) for player_Guess in input('give me 5 numbers i will choose 1 and you will guess what i chose:').split(",")]
    guess=int(input('guess a number i chose from your selection: '))
    print(player_Guess)
    player_Choice=random.choice(player_Guess)
    print(player_Choice)


    if(player_Choice==guess): 
        replay=str(input("Winner!! do you want to play again: y/n:"))
        if replay=="y": 
            continue
        elif replay=="n":
            break
    else: 
        print('not the right number choose again')



        
