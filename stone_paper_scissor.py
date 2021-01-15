import random

'''
1=snake
2=water
3=gun
'''



count1=0
count2=0
j=3

for i in range (j):
    n = random.randint(1, 3)
    u = int(input('1.Snake\n'
                  '2.water\n'
                  '3.gun\n'))
    if (n==1 and u==2):
        count1=count1+1
        print(n,u)
    elif (n==3 and u==2):
        count2=count2+1
        print(n, u)
    elif(n==2 and u==1):
        count2=count2+1
        print(n, u)
    elif(n==3 and u==1):
        count1=count1+1
        print(n, u)
    elif(n==1 and u==3):
        count2+=1
        print(n, u)
    elif(n==2 and u==3):
        count1+= 1
        print(n, u)
    elif(n==u):
        i=i-1
        print(n, u)
    n = random.randint(1, 3)

if count1>count2:
    print('Sorry you loss')

else:
    print('Congratulation you win')