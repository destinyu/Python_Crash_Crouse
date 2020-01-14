informations = {
    'first_name': 's',
    'last_name': 'b',
    'age': 10,
    'city': 'toyota'
}
print(informations)

knowledge = {
    '数组': '线性排列的一组数',
    '栈': '一种先进后出的数据结构',
    '字典': '存放对应键值对的数组'
}
print("数组是：" + knowledge['数组'])
print("栈是：" + knowledge['栈'])
print("字典是：" + knowledge['字典'])

for name,mean in knowledge.items():
    print(name+":"+mean)
