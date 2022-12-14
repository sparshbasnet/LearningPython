print("Welcome to my computer quiz!")

play = input("Do you want to play? ")
score= 0

if play.lower() != "yes":
    quit()
print("Okey! Lets play")

QA = input("What does  CPU stands for? ")
if QA.lower() == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

QA = input("What does  GPU stands for? ")
if QA.lower() == "graphics processing unit" :
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

QA = input("What does  RAM stands for? ")
if QA.lower() == "random acess memory" :
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

QA = input("What does ROM stands for? ")
if QA.lower() == "read only memory":
    score +=1
    print("Correct!")
else:
    print("Incorrect!")

print("You got "  +  str(score)  +  " question coreect")
print("You got "  +  str((score/4) * 100)  +  "% .")
