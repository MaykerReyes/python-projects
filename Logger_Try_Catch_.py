import time

today = time.strftime("%m_%d_%Y")
t = time.localtime()
current_time = time.strftime("%H_%M_%S", t)
LogFile = open(str(today)+"_mylogfile.txt","a")

try:
    f = open("myfile","w")
    a,b = [int(x) for x in input("Enter two numbers:").split()]
    LogFile.write(current_time+" : Division in progress \n")
    c = a/b
    f.write("Writting %d into file" %c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero number")
    LogFile.write(current_time+" : Division by zero \n")
except: 
     print("an error occurs")     
     LogFile.write(current_time+" : an error occured \n")

finally:
    f.close()
    LogFile.close()
    print("file Closed")
print("Code after the exception")               