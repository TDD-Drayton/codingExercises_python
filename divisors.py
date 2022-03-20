__author__='TDD-Drayton'

num=int(input("Enter number and I will list the divisors: "))
numList = list(range(1,num+1))
divisorList = []

for i in numList:
    if num % i == 0:
        divisorList.append(i)
