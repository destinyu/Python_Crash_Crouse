filename='programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming\n")
    file_object.write("I love creating new game\n")

with open(filename,'a')as file_object:
    file_object.write("i love you too")