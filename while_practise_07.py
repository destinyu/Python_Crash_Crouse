sandwich_orders = ['milk sandwich', 'tomato sandwich', 'lili sandwich']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I finished your " + current_sandwich)
    finished_sandwiches.append(current_sandwich)

print("--finished_sandwiched--")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
# 7.9
sandwich_orders = ['milk sandwich', 'tomato sandwich', 'pastrami', 'pastrami', 'lili sandwich', 'pastrami']
print("The pastrami have been sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
print("\n")

respones = {}
active = True
while active:
    name = input("What's your name? \n")
    respone = input("Where would you go? \n")
    respones[name] = respone
    repeat = input("Do you want anyone else to answer it?(yes/no)\n")
    if repeat == 'no':
        active = False
print("--THE ANSWER--")
for name, respone in respones.items():
    print(name + "'s favourite place is " + respone)
