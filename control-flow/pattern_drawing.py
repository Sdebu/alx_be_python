# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate over each row
while row < size:
    # Use a for loop to print '*' for each column in the current row
    for col in range(size):
        print("*", end="")
    # Move to the next line after finishing a row
    print()
    # Increment the row counter
    row += 1
