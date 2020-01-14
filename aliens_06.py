# 字典可以嵌套在数组里
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#for alien in aliens:
    #print(alien)
print("\n")
print(str(len(aliens)))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'mewdium'
        alien['points'] = 10
#for alien in aliens:
    #print(alien)

#字典里还可以嵌套列表
pizza={
    'crust':'thick',
    'toppings':['mushroom','extra cheese']
}
print("You order a "+pizza['crust']+"-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(topping)

favourite_languages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}
for name,languages in favourite_languages.items():
    print("\n"+name.title()+"'s favourite languages are:")
    for language in languages:
        print(language.title())