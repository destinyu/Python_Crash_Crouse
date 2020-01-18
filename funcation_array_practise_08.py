
def show_magicians(magicians):
    for magicaian in magicians:
        print(magicaian)

def make_great(magicians,magicians2):
    for magician in magicians:
        current_magician='The Great '+magician
        magicians2.append(current_magician)


magicians=['David','backham','willim','fuck']
magicians2=[]

make_great(magicians,magicians2)
show_magicians(magicians2)
show_magicians(magicians)


#本例构想的方法：
#建立两个列表，通过pop（）来转移
#用make_great(magician[:],new_magician)方法来不修改原来的列表

#突然完成的新奇方法：
#构建new_magician方法，用for循环修改后存储，原列表不动