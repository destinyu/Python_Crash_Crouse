namelist=['tony_ma','jack_ma','yanhong_li']
print(namelist[0])
print(namelist[1])
print(namelist[2])
print("yanhong_li cant come to our banquet")

namelist[2]='minhong_yu'
print(namelist)

print("i find a bigger table")
namelist.append('jack_chen')
namelist.append('benshan_zhao')
namelist.append('luo_c')
print(namelist)

print("i find a bigggger table")
namelist.insert(0,'yu_xing')
namelist.insert(3,'anglebaby')
namelist.append('xiaoming_huang')
print(namelist)

print("sorry,i only can invite two people")
name1=namelist.pop()
print("sorry,"+name1)
name2=namelist.pop()
print("sorry,"+name2)
print(namelist)
print("sorry,"+namelist.pop())
print(namelist)
del namelist[2]
print(namelist)