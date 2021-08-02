print("\n3x + 1")                         
print("By WackyFolf (for some reason)\n")
number = int(input("Enter a number: " ))
progression = 0                           # Create int for counting how many times the process is run
while number != 1:                        # I'm looking for 1, which is what this always gets to, no matter what
    if ((number % 2) == 0):               # If the number is even, divide it by two, as the problem goes
        number = number/2
    else:
        number = ((3*number) + 1)         # If the number is odd, do 3x + 1
    print(int(number))
    progression += 1                      # Add 1 to the number of steps taken
print("Got to 1 after " + str(progression) + " steps")

"""
Take any number. If it's even, divide it by two. If it's odd, multiply it by 3 and add 1.
Do the same to the result.
Repeat this until you reach the sequence "4, 2, 1", which will always happen. 
"""