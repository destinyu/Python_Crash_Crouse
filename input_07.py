message=input("Tell me something,and i will repeat it back to you: ")
print(message)

name=input("Please enter your name: ")
print("Hello,"+name+"!")

prompt="If you tell us who you are, we can personalize the messages you see.\nWhat's your name? "
#prompt+="\n..."
name=input(prompt)
print("\nHello "+name)

height=input("How tall are you,in inches? ")
height=int(height)
if height>36:
    print("You are tall enough to ride!")
else:
    print("you will be able to ride when you are a little bit taller")

#用数字就int(),用字符就str()