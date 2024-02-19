def calculate_mpg():

    miles_driven = float(input("Enter the number of miles driven: "))
    gallons_used = float(input("Enter the gallons of gas used: "))

    mpg = miles_driven / gallons_used

    print("\nYour car's MPG is: {:.2f} miles per gallon".format(mpg))

calculate_mpg()
