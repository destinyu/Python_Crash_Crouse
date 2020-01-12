cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

#检查多个条件：
#age_0=22
#age_1=18
#age_0>=21 and age_1>=21

request_toppings=['mushroom','onions','pineapple']
m='mushroom' in request_toppings
print(m)

car='subaru'
print("Is car=='subaru?I predict True.")
print(car=='subaru')