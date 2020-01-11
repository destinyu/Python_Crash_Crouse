#for value in range(1,5):
#   print(value)
for value in range(1,6):
    print(value)
#数字列表
number=list(range(1,6))
print(number)
#奇数列表
even_number=list(range(2,11,2))
print(even_number)
#空表再添加
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
#对数字列表执行简单计算
digit=list(range(1,11))
min=min(digit)
print(min)
max=max(digit)
print(max)
sum=sum(digit)
print(sum)
#列表解析
squares1=[value**2 for value in range(1,11)]
print(squares1)