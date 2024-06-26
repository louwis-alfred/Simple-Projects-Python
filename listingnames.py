names = []

how_many_name = int(input('Enter a number: '))

for i in range(how_many_name):
  name = input(f"{i+1}.) Enter name: ")
  names.append(name)
    
last_name = input("Enter the last name: ")
names.append(last_name)

print('List of names:')
for index, names in enumerate(names, start=1):
  print(f"{index}.{names}")