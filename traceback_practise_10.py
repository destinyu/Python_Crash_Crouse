#10——6
print("Give me two numbers,and i'll plus them.")
print("Enter 'q' to quit.")

while True:
    first_number=input("\nFirst number: ")
    if first_number=='q':
        break
    second_number=input("\nSecond number: ")
    try:
        answer=int(first_number)+int(second_number)
    except ValueError:
        print("You must input two numbers")
    else:
        print(answer)


#10_10
filename='Alice in Wonderland.txt'
with open(filename) as f_obj:
    contents = f_obj.read()
num=contents.lower().count('the')
print("The 'the' has come out "+str(num)+" times")

