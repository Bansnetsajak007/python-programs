def calculate_installments():
    purchase_amount = float(input("Enter the amount of purchase: $"))
    num_installments = int(input("Enter the desired number of payment instalments: "))


    total_purchase_amount = purchase_amount * 1.05

 
    installment_cost = total_purchase_amount / num_installments

    print("\nTotal Purchase Amount: ${:.2f}".format(total_purchase_amount))
    print("Each Instalment Cost: ${:.2f}".format(installment_cost))



calculate_installments()
