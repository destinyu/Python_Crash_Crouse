#for enumber in range(1,21):
#    print(enumber)
bnumber=list(range(1,1000001))
#for number in bnumber:
#    print(number)
min=min(bnumber)
max=max(bnumber)
sum=sum(bnumber)
#print(min)
#print(max)
#print(sum)
for value in range(1,21,2):
    print(value)
times=[]
for value in range(3,31):
    time=value*3
    times.append(time)
print(times)

three_squares=[]
for value in range(1,11):
    three_squares.append(value**3)
print(three_squares)
#列表解析
msquares=[value1**3 for value1 in range(1,11)]
print(msquares)