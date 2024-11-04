# Take input from the user for the multiplication table number
num = int(input("Enter a number for the multiplication table: "))

# Display the multiplication table for the entered number
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
