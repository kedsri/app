name='Kedar'
age=46
what ="learning python at this age"
#print("Sairam")
#print(name,age,what)
name1=input("What is your name ?")
#name2=input("What is your age ?")
#name3=input("What are you doing now ?")
print("Hey " + name1)

if name1 == "Kedar":
    print("the input that is typed " +name1 +" matches")
elif name1=="Nath":
    print("you are in elif:"+name1)
else:
    print("different name")