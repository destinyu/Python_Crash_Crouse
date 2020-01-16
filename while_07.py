current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1

for num in range(1,6):
    print(num)

prompt="\nTell me something, and i will repeat it back to you: "
prompt+="\nEnter 'quit' to end the program."
message=""
#while message!='quit':
 #   message=input(prompt)
  #  if message!='quit':
   #     print(message)

#标志的用法
active=True
while active:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)

#continue用法
current_number=0
while  current_number<10:
    current_number+=1
    if current_number%2==0:
        continue

    print(current_number)