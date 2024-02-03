#To display unique and duplicate items of a given list:

L1=[1,9,7,6,3,0,0,4,6,12,7,1]
l2= []
l3= []
for i in  L1:
    if i not in l2:
        l2.append(i)
    else:
         l3.append(i)


print(l2)
print(l3)

    
