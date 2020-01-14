alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Origin x_position:" + str(alien_1['x_position']))
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':

    x_increment = 2
else:
    x_increment = 3
alien_1['x_position'] = alien_1['x_position'] + x_increment
print("New x_position:" + str(alien_1['x_position']))
print(alien_0)
del alien_0['color']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print("Sarah's favourite language is " +
      favorite_languages['sarah'].title() +
      ".")

for name,language in favorite_languages.items():
    print(name+"'s favourite language is "+language)

#for name1 in favorite_languages.keys():
#   print(name1)

for name1 in sorted(favorite_languages.keys()):
    print(name1)

for value in favorite_languages.values():
    print(value)
print("\n")

for value in set(favorite_languages.values()):
    print(value)