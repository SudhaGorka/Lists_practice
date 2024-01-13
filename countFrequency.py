#Write a program to count frequency of a given element in a list of numbers.

List = eval(input("Enter a list of numbers: "))
num=int(input("Enter a number you want frequency of: "))

count=0

for i in List:
    if i == num:
        count=count+1
        
print("count is: ",count)
    
