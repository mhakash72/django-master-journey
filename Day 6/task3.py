names =[]
for i in range(3):
    name = input(f'Enter your {i+1} name :')
    names.append(name)
with open('names.txt','w') as file:
    for name in names:
        file.write(name+ "\n")
print("Names saved succesfully.")

with open('names.txt','r') as file:
    content = file.read()
    print(content)