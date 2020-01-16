# print(input("What kind of the car you want to lent?\n"))

message = input("How many people for this dinner?\n")
num = int(message)
if num > 8:
    print("Sorry,there is no empty table.")
else:
    print("You can come here.")

number=input("Please input a number:")
number=int(number)
if number%10==0:
    print("It can be divided by 10")
else:
    print("Sorry,it cant be")