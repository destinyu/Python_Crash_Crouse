cars=['bmw','audi','toyota','subaru']
#按首字母排序
cars.sort()
print(cars)

#反向排序
cars.sort(reverse=True)
print(cars)

#sorted可以暂时排序，不彻底改变
print(sorted(cars))

#使序列翻转
#再用一次可以复原
cars.reverse()
print(cars)

#知道序列的长度
print(len(cars))
