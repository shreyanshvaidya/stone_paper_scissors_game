import random
user_score=0
computer_score=0
tie=0
print("welcome to the Stone Paper Scissors game")
print()
user_name = input("enter your name :")
print()
options = ["stone", "paper", "scissors"]

print("The rules are simple:\nyou have three choices stone,paper and scissors")
print("stone beats scissors\nscissors beats paper\npaper beats stone")
print()
while True:
    random_choice = random.choices(options)
    user_choice = input("enter your choice :").lower()
    for computer_choice in random_choice:
        pass
    print("your choice is:", user_choice, "\ncomputers choice is:", computer_choice)
    if user_choice == computer_choice:
        print("the game was a tie")
        tie +=1
    elif user_choice == "stone":
        if computer_choice == "scissors":
            print("Congratulations,you won the game")
            user_score+=1
        elif computer_choice == "paper":
            print("ohh,you lose the game")
            computer_score+=1 
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Congratulations,you won the game")
            user_score+=1
        elif computer_choice == "scissors":
            print("ohh,you lose the game")
            computer_score+=1
    elif user_choice == "paper":
        if computer_choice == "stone":
            print("Congratulations,you won the game")
            user_score+=1
        elif computer_choice == "scissors":
            print("ohh,you lose the game")
            computer_score+=1
    else:
        print("you had done a spelling mistake \nplease check the spelling and try again")
    repeat = input("do you want to play again (y/n):").lower()
    if repeat == "n":
        print("you want to quit")
        break
    elif repeat == "y":
        print()
        continue
    else:
        print("invalid input!")
        break
print()
print("scorecard")
print(user_name,"=",user_score,"\ncomputers score=",computer_score,"\ntie=",tie )


