#practise_01
def customer(*toppings):
    for topping in toppings:
        print("You select "+topping)


customer('a','b')
customer('a','b','c')

#practise_02
def car_information(factory,model,**car_info):
    info={}
    info['factory']=factory
    info['model']=model
    for key,value in car_info.items():
        info[key]=value
    return info

car=car_information('subaru','outback',color='blue',tow_package=True)
print(car)