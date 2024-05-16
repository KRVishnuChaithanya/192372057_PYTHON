f = open("calendar.py", "r") 
print(f.read())
print(f.read(5)) 
print(f.readline()) 
print(f.readline())
print(f.readline()) 
f.close()
f = open("calendar.py", "a") 
f.write("Now the file has more content!")
f = open("calendar2.py", "w") 
f.close()
print(f.read()) 
