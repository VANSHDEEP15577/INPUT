sum=0
cube=0
while input() != 'k':
    num=int(input("ENTER THE NUMBER:"))
    cube=num*num*num
    sum=cube+sum
print(sum)