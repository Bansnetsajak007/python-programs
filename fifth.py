def ingredient_adjuster():
    # Original recipe
    sugar_original = 1.5  
    butter_original = 1  
    flour_original = 2.75 

    num_cookies = int(input("Enter the number of cookies you want to bake: "))

    # Calculate adjusted amounts
    sugar_adjusted = sugar_original * (num_cookies / 48)
    butter_adjusted = butter_original * (num_cookies / 48)
    flour_adjusted = flour_original * (num_cookies / 48)

    print(f"\nAdjusted amounts for {num_cookies} cookies:")
    print(f"Sugar: {sugar_adjusted:.2f} cups")
    print(f"Butter: {butter_adjusted:.2f} cups")
    print(f"Flour: {flour_adjusted:.2f} cups")

if __name__ == "__main__":
    ingredient_adjuster()
