# command = " "
# started= False
# stopped= False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print ("Car is already started...")
#         else:
#             started= True
#             print ("Car started...")
#     elif command == "end":
#         if stopped:
#             print ("Car is already stopped...")
#         else:
#             stopped= True
#             print ("Car stopped...")
#     elif command == "help":
#         print ("""
# start- to start the car
# stop- to stop the car
# quit- to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print ("Sorry I dont understand ")

# sparsh = ["sparsh","basnet","ram","shyam"]
# for ones in sparsh:
#     print (ones)

# for see in range(1,500+1):
#     if see%5==0:
#         print (see)
# prices=[10,20,30]
# total=0
# for price in prices:
#     total += price
#     print (f"Total:{total}")

# numbers =[5,2,5,2,2]
# for x in numbers:
#     output =''
#     for count in range (x):
#         output += 'x'
#     print (output)

# list =[16,28,13,4,55,47,9]
# max = list[0]
# for number in list:
#     if number>max:
#         max = number
#     print (max)



# list =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for numbers in list:
#     for items in numbers:
#         print (items)



# numbers=[2,2,3,4,5,6,6,7,3]
# uniques = []
# for list in numbers:
#     if list not in uniques:
#         uniques.append(list)
#     print (uniques)




# phone = input ("Phone: ")
# digits_maping = {
#   "1": "One",
#   "2":"Two",
#   "3":"Three",
#   "4":"Four"
# }
# output =""
# for chr in phone:
#     output += digits_maping.get(chr, "!")+ " "
# print(output)



# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)" : " 😀 ",
#     ":(" : " 😌 "
# }
# for word in words:
#     output = " "
#     output += emojis.get(word, word) + " "
# print (output)



# def greetuser():
#     print ("Hey there")
#     print ("Goodmorning")
# print("Start")
# greetuser()
# print("Finish")


def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)" : " 😀 ",
        ":(" : " 😌 "
    }
    for word in words:
        output = " "
        output += emojis.get(word, word) + " "
    return output
    
message = input(">")
print (emoji_converter(message))