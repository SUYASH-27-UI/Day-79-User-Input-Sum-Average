numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)
