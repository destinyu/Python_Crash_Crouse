names=[]
names=['abbi','flank','jack','john','mark','admin']
if names:
 for name in names:
    if name=='admin':
        print("Hello admin,would you like to see a status report?")
    else:
            print("Hello "+name+",thank you for logging in again.")
else:
    print("We need find some users!")

#practise 02
current_users=['abbi','flank','jack','john','mark','admin']
new_users=['Abbi','mike','Jack','rbi','sabi']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("The user name has been used.")
    else:
        print("The user name can be used!")