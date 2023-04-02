class factorial:

    def __init__(self,number):
        self.number=number
        self.factorial_= 1

    def fact_calculator(self):
        for i in range(1,self.number+1):
            self.factorial_=self.factorial_*i
        return self.factorial_


your_input=int(input("Enter the number you want to calculate factorial of: "))
number1= factorial(your_input)

print(number1.fact_calculator())

        