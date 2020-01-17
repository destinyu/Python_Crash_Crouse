#01.简单返回值
def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()

musician=get_formatted_name('jimi','hendrix')
print(musician)

#可选实参
def get_formatted_name_ya(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=first_name+' '+middle_name+' '+last_name
    else:
        full_name=first_name+' '+last_name
    return full_name.title()

musician=get_formatted_name_ya('john','hokker','lee')
print(musician)

#02.返回字典
def build_person(first_name,last_name,age=''):
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician=build_person('jimi','hendrix',age=27)
print(musician)