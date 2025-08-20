import os,sys
FileName = "myfile.txt"
if os.path.isfile(FileName):
    f = open(FileName,"r")
else:
    print("File Does not exist")
    sys.exit()    

s = f.read()
print(s)
f.close()
            