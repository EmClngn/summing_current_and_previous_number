# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

# pseudo code

# create a separate value to add
for_addition = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# use for loop to write the main code for summing
for i in range(10):
    current_number = for_addition[i + 1]
    previous_number = for_addition[i]
    the_sum = current_number + previous_number
    print("The Current Number:", current_number, "  The Previous Number:", previous_number, "  Sum:", the_sum)


