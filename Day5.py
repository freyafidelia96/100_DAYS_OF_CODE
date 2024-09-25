"""list_input = input("Enter the numbers you want to find average\n")

numbers = list_input.split(" ")
noOfnumbers = 0
sumOfnumbers = 0
max = 0

for number in numbers:
    int_num = int(number)
    sumOfnumbers += int(number)
    noOfnumbers += 1

    if int_num > max:
        max = int_num

average = sumOfnumbers / noOfnumbers
print(f"Total height = {sumOfnumbers}\nTotal number of students = {noOfnumbers}\nAverage height = {average}")
print(f"The highest score is: {max}")"""

"""target = int(input("Enter target: "))
total_even = 0

for even in range(2, target + 1, 2):
    total_even += even

print(total_even)"""

for fizzBuzz in range(1, 101):
    if (fizzBuzz % 3 == 0 and fizzBuzz % 5 == 0):
        print("FizzBuzz")
    elif fizzBuzz % 3 == 0:
        print("Fizz")
    elif fizzBuzz % 5 == 0:
        print("Buzz")
    else:
        print(fizzBuzz)