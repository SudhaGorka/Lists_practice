#reads a line, then counts words and displays how many words are there in the line.

line=input("Enter a sentence: ")
x=line.split()
count=0
for i in x:
    count=count+1
print(count)
    
