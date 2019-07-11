# Challenge: Number Loop with User Input
# Lets comebine some of the things we know!
# I want you to write a new program that gets two whole numbers from the user
# and counts between them using a for loop!

# cast input to int for whole numbers
# get input and store starting number
start = int(input("Starting whole number ? "))
# get input and store stop number
end = int(input("Ending whole number ? "))
# loop from start to end + 1 so you reach the end number
for x in range(start, end+1):
    # print the value of x in our current loop
    print(x)
