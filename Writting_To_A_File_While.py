f = open("myfile.txt","w")
print("Enter Text(Type # when you are done)")
s=''
while s != '#end':
    s = input()
    f.write(s+ "\n")

f.close 