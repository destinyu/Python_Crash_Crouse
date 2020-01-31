import json


#number=input("Please input your favourite number: ")
#filename='favourite.json'
#with open(filename,'w') as f_obj:
#    json.dump(number,f_obj)


'''filename='favourite.json'
with open(filename) as f_obj:
    number=json.load(f_obj)
print("Your favourite number is "+number+"!")'''

def get_stored_users():
    filename='favourite.json'
    try:
        with open(filename) as f_obj:
            name=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return name

def get_new_username():
    name = input("Please input your name: ")
    filename = 'favourite.json'
    with open(filename, 'w') as f_obj:
        json.dump(name, f_obj)


def greet_user():
    name=get_stored_users()
    if name:
        choose=input("Is the name "+name+" right?(y/n)")
        if choose=='y':
            print("Welcome back "+name+"!")
        else:
            get_new_username()


    else:
      get_new_username()

greet_user()
