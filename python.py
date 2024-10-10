
print("chose your operation:")
print("1. plus")
print("2. minus")
print("3. mulpy")
print("4. divide")

choice = input("Please enter a number of operation (1/2/3/4): ")

num1 = float(input("enter the frist number: "))
num2 = float(input("enter the second number: "))

if choice == "1":
    print(int(num1+num2))
elif choice == "2":
    print(int(num1-num2))
elif choice == "3":
    print(int(num1*num2))
elif choice == "4":
    print(int(num1/num2))
else:
    print("Not valid input.")

