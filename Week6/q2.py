phonebook = {}

num = int(input("Enter the number of entries you want to do: "))
for i in range(num):
    name = input(f"Enter name : ")
    number = input(f"Enter number for name {name}: ")
    phonebook[name] = number

search_name = input("\nEnter the name to search Phone number: ")

if search_name in phonebook:
    print(f"{search_name} : {phonebook[search_name]}")
else:
    print(f"Phone number for {search_name} not found")
