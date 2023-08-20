import random  
# Function to play game  
def start_game():  
    # Print games rules and instructions  
    print(" welcome to Stone-Paper-Scissors! ")  
    print(" Please Enter your choice: ")  
    print(" 1: Stone ")  
    print(" 2: Paper ")  
    print(" 3: Scissors ")  
     
choice_user = int(input(" Select your choice from 1 - 3 : "))  
  
choice_machine = random.randint(1, 3)  
  
    # display the machines choice  
    print(" Option choosed by Machine is: ")  
    if choice_machine == 1:  
        print(" Stone ")  
    elif choice_machine == 2:  
        print("Paper")  
    else:  
        print("Scissors")  
  
    # To declare who the winner is  
    if choice_user == choice_machine:  
        print(" It's a tie! ")  
    elif choice_user == 1 and choice_machine == 3:  
        print(" You won! ")  
    elif choice_user == 2 and choice_machine == 1:  
        print(" You won! ")  
    elif choice_user == 3 and choice_machine == 2:  
        print(" You won! ")  
    else:  
        print(" Sorry! The Machine Won the Game? ")  
  
    # If user wants to play again  
    play_again = input(" Want to Play again? ( yes / no ) ").lower() 
    if play_again == " yes ":  
        start_game()  
    else:  
        print(" Thanks for playing Stone-Paper-Scissors! ")  
  
 