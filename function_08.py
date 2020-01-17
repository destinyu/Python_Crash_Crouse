def greet_user():
    print("Hello!")
greet_user()
#考虑顺序传参
def describe_pet(animlai_type,pet_name='honey'):
    print("\nI have a "+animlai_type+".")
    print("My "+animlai_type+"'s name is "+pet_name.title()+".")

describe_pet('hamster','harry')
describe_pet('dog','willie')
#不考虑顺序，用关键字传参
describe_pet(pet_name='lili',animlai_type='monkey')

#默认参数:注意默认值的参数要放在最后
