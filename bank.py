# Collect student's name
name = input("Enter student's name: ")

# Collect grades as numbers (float)
sub_1 = float(input("Enter student's grade for subject 1: "))
sub_2 = float(input("Enter student's grade for subject 2: "))
sub_3 = float(input("Enter student's grade for subject 3: "))

# Store grades in a list
subjects = [sub_1, sub_2, sub_3]

# Calculate average
average = sum(subjects) / len(subjects)

# Display average
print(f"{name}'s average grade is: {average:.2f}")

# Check for academic honors
if average >= 95:
    print("Wow the bloody legend! Certified hacker? HAHA good job for achieving Highest Honors, you deserved it!")
elif average >= 85:
    print("Congrats! You just achieved Academic Honors, good job!")
else:
    print("Hey, you tried your best, better than failing that's for sure HAHA! Next time, I'm sure you'll reach High Honors one day!")
