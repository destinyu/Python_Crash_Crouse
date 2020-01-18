# *parameter->元组
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)


make_pizza('a')
make_pizza('b', 'c', 'd')


def make_big_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)


make_big_pizza(16, 'a')
make_big_pizza(12, 'b', 'c', 'd')


# **parameter->字典
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('a', 'b', location='c', filed='d')
print(user_profile)
