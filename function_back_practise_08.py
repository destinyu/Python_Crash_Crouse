#practise_01
def city_country(name,country):
    content=name+', '+country
    return content
c1=city_country('shanghai','China')
c2=city_country('tokoyo','Japan')
c3=city_country('toroto','USA')
print(c1)
print(c2)
print(c3)

#practise_02
def make_album(singer_name,album_name,songs_num=''):
    person = {'singer': singer_name, 'album': album_name}
    if songs_num:
        person['songs_num']=songs_num
    return person
person1=make_album('jj lin','come to love')
print(person1)
person2=make_album('yamaha','what fuck',100)
print(person2)