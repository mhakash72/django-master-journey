name = input("Enter name : ")
age = int(input(" Enter age : "))
district =input("Enter District : ")
dict={
    "Name = " : name,
    "Age =" : age,
    "District =" : district
}
for key,value in dict.items():
    print(f'{key} {value}')