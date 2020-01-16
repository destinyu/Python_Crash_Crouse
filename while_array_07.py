unconfirmed_user=['alice','brian','candace']
confirmed_users=[]

while unconfirmed_user:
    current_user=unconfirmed_user.pop()
    print("Verifying user:"+current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


responses={}
polling_active=True
while polling_active:
    name=input("\nWhat's you name? ")
    response=input("Which mountain would you like to climb someday? ")

    responses[name]=response
    repeat=input("Would you like to let another person respond?(yes/no) ")
    if repeat=='no':
        polling_active=False
print("--Poll Results--")
for name,response in responses.items():
    print(name+" would like to climb "+response)