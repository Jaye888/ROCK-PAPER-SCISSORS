import random
options = ["R", "P", "S"]
print("Welcome, Player. To start playing, pick an option: R is for rock. P is for paper. S is for scissors. Best of luck!")

computer_input = random.choice(options)
# print(computer_input)


while True:
    player_input = input("Make your pick: ")
    if player_input not in options:
        print("Error! Try again.")
    
    

    if computer_input is options[0] and player_input is options[1]:
        print("Player:" + player_input + " " + "CPU:" + computer_input)
        print("You win, champ! Game over.")
        break

    elif computer_input is options[0] and player_input is options[2]:
        print("Player:" + player_input + " " + "CPU:" + computer_input)
        print("You lose, challenger! Game over.")
        break

    elif computer_input is options[1] and player_input is options[0]:
        print("Player:" + player_input + " " + "CPU:" + computer_input)
        print("You lose, challenger! Game over.")
        break

    elif computer_input is options[1] and player_input is options[2]:
        print("Player: " + player_input + " " + "CPU:" + computer_input)
        print("Nice work, champion! Game over.")
        break

    elif computer_input is options[2] and player_input is options[0]:
        print("Player:" + player_input + " " + "CPU:" + computer_input)
        print("You win, champ! Game over.")
        break

    elif computer_input is options[2] and player_input is options[1]:
        print("Player:" + player_input + " " + "CPU:" + computer_input)
        print("You lose, challenger! Game over")
        break
        
    elif player_input == computer_input:
        print("It's a tie! Try again, challenger. ")
        continue
