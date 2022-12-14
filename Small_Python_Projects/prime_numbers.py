for number in range(100,200):
    if all(number%i !=0 for i in range(2,number)):
        print (number)