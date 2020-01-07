#列表的使用
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
#指定修改其中元素
motorcycles[0]='dukati'
print(motorcycles)
#在列表最后添加元素
motorcycles.append('lululu')
print(motorcycles)
#根据索引值插入元素
motorcycles.insert(1,'我是插入的值')
motorcycles.insert(2,'waibibabu')
print(motorcycles)
#del：删除且不会再被使用
del motorcycles[1]
print(motorcycles)
#pop：删除后继续使用值，还可以用pop（0）定位
poped_motorcycles=motorcycles.pop()
print(motorcycles)
print(poped_motorcycles)
#总结：以后再也不用，用del删除；删除后继续使用，用pop（）；

#根据值删除元素
motorcycles.remove('waibibabu')
print(motorcycles)
