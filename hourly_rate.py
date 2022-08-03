# 2.3 Write a program to prompt the user for the hours and rate per hour using input to
# compute the gross pay. Use 35 hours and a rate of 2.75 per hour to test the program
# (the pay should be 96.25). You should input to read a string and float() to
# convert the string to a number. Do not worry about error checking or bad user
# data.

# This first line is provided for you.

hrs = input("Enter Hours:")
rate = input("Enter rate per hour:")

output = float(hrs) * float(rate)
print("Pay: {}".format(output))
