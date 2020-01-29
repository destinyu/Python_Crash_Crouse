class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print("Welcome to the "+self.restaurant_name)
        print("We have "+self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is opening")


class User():
    def __init__(self,first_name,last_name,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=login_attempts

    def describe_user(self):
        print("My fname is "+self.first_name)
        print("My lname is "+self.last_name)
        print(self.login_attempts)

    def greet_user(self):
        print("Nice to meet you, "+self.first_name+" "+self.last_name)

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

bbc=Restaurant('bbc','trush')
aab=Restaurant('aab','many food')
print(bbc.number_served)

bbc.describe_restaurant()
aab.describe_restaurant()

a=User('s','b',3)
b=User('2','x',4)
c=User('s','x',5)
a.describe_user()
a.greet_user()
b.describe_user()
b.greet_user()
c.describe_user()
c.greet_user()

c.increment_login_attempts()
c.increment_login_attempts()
c.describe_user()
c.reset_login_attempts()
c.describe_user()