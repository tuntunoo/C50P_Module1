#Ask user to type name
name=input("What is your name? ")

#Print, what they type
print("Hello,")
print (name)

#Print above in one line
print("Hello,",end="")
print(name)

#Formating String with "f", special indicator
print(f"Hello,{name}")

#Using method, "strip" to remove white space
name= name.strip()
print(f"Hello,{name}")

#Using method, "title" to capitalize the first word
name= name.title()
print(f"Hello,{name}")

#Using more method together, "strip and ""title" 
name= name.title().strip()
print(f"Hello,{name}")
