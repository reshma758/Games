### number guessing game
def num_guess():
    import random
    print("*"*5,"Welcome to number guessing game","*"*5)
    s_num = random.randint(1,100)
    atm = 1
    while atm < 10:
        user_num = int(input("Enter your Guess:"))
        if user_num > 0 and user_num <= 100:
            if user_num > s_num:
                print(f"your Guess is Higher Then The Secret Number, you Have Remaining {9-atm} Attempts")
            elif user_num < s_num:
                print(f"your Guess is Lower Then The Secret Number, you Have Remaining {9-atm} Attempts")
            else:
                print(f"Well done! {s_num} in {atm} attempts!")
                break
            atm += 1
        else:
            print("please enter a num between 1 and 100 only")
    else:
        print("Your attempts are over.Try again later!")


## Color Guessing Game
def color_guess():
    import random
    print("*"*5,"Welcome to color guessing Game","*"*5)
    colors = ["black","white","blue","red","purple" ]
    s_color = random.choice(colors)
    atm = 1
    while atm < 5:
        user_color = input("Choose your color :\n1.black \n2.white \n3.blue \n4.red \n5.purple \n>>")
        if user_color.lower() in colors:
            if user_color.lower() == s_color:
                print(f"Well Done, You Guessed the Correct color {s_color} in {atm} Attempts!!!")
                break
            else:
                print(f"your guess is wrong, you have remaining {4 - atm} Attempts only !!!")
        else:
            print("Invaild Enter, please Enter Valid Input !!")
        atm += 1
    if user_color.lower() == s_color.lower():
        print("*"*5,"Well Done","*"*5)
    else:
        print("Sorry your Attempts are Over. try Again Later !!!")


### Rock paper scissor Game
def rps_game():
    import random
    print("*"*5,"Welcome to rock, paper, scissor Game","*"*5)
    item = ["rock", "paper", "scissor"]
    system = random.choice(item)
    atm = 1
    name = input("Enter your Name:")
    rounds = int(input("How Many Rounds :"))
    s_score = 0
    u_score = 0
    while atm <= rounds:
        print("______________________")
        system = random.choice(item)
        user = input("Enter your choose :\n1.rock \n2.paper \n3.scissor \n>>>")
        if user.lower() in item:
            if (system == "rock" and user.lower() == "scissor") or (system == "scissor" and user.lower() == "paper") or (system== "paper" and user.lower() == "rock"):
                print(f"Round {atm} : System win the Round")
                s_score += 1
            elif (system == "rock" and user.lower() == "paper") or (system == "scissor" and user.lower() == "rock") or (system== "paper" and user.lower() == "scissor"):
                print(f"Round {atm} : {name} win the Round")  
                u_score += 1
            else:
                print(f"Round {atm} : Tie Round")
                u_score += 0.5
                s_score += 0.5
        else:
            print("Invalid Enter, please Enter Valid Input !!!")
            atm -= 1
        atm += 1
    print("*"*5,"Game Result","*"*5)
    if s_score > u_score:
        print(f"System : {s_score} \n{name} : {u_score} \nsorry you lost the match !!!")
    elif u_score > s_score:
        print(f"System : {s_score} \n{name} : {u_score} \nWeldone you won the match !!!")
    else:
        print(f"System : {s_score} \n{name} : {u_score} \nThe match ends with tia !!!")

