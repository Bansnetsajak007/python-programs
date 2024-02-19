def calculate_total_amount():
    food_charge = float(input("Enter the charge for the food: $"))

    tip_percentage = 0.18
    sales_tax_percentage = 0.07

    tip_amount = food_charge * tip_percentage
    sales_tax_amount = food_charge * sales_tax_percentage

    total_amount = food_charge + tip_amount + sales_tax_amount

    print("\nFood Charge: ${:.2f}".format(food_charge))
    print("Tip (18%): ${:.2f}".format(tip_amount))
    print("Sales Tax (7%): ${:.2f}".format(sales_tax_amount))
    print("Total Amount: ${:.2f}".format(total_amount))


calculate_total_amount()
