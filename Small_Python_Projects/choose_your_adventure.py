name = input(" Enter your name: ")
print("Welcome to the adventure", name + ".")

answer= input("You are on a road and it has a left and a right to move. Which way you want to head? Left or Right?: ")

if answer == "left":
    answer = input("You have came to a river, you can swim across or you can walk around? Do you want to walk or swim?: ")

    if answer == "swim":
        print("You were attacked by Alligator, trying to swim across the river. You lose!")

    elif answer == "walk":
        print("You ran out of water & food trying to walk across the road. You lose!")

    else:
        print("Not a valid option. You lose!")

elif answer == "right":
    answer = input("You have came to a bridge, it look woobly. Do you want to cross it or head back(cross/headback)?: ")

    if answer=="cross":
        answer = input("You have succesfully crossed the bridge. There is stranger standing, do you want to talk (yes/no) ?: ")
       
        if answer == "yes":
            print("The stranger provided you with a bag full of gold. You won!")
        
        elif answer == "no":
            print("The stranger was offended . You lost!")

        else:
            print("Not a valid option. You lose!")
      
    elif answer == "headback":
            print("You were not supposed to headback as you will run out of fuel. You lose!")


else:
    print("Not a valid option. You lose!")

print("Thank you for trying", name )