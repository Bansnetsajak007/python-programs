
class BUS:
    start_point = "bhadrapur"
    bus_type = "public"


    def __init__(self):
        self.max_seat = 90
        self.menue()

    def menue(self):
        print("*" * 50)
        print("Welcome to online Bus reservation system");
        print("*" * 50)

        print(
            '''
                What would you like to choose?

                1) check bus details
                2) book tickets
                3) check routes
                4) exit


            '''
        )

        option = int(input("Enter your choice: "))

        if option == 1:
            self.bus_details()

        elif option == 2:
            self.book_tickets()
        


    def bus_details(self):
        print("Bus name : sagarmatha yatayat")
        print("driver name : hari")
        print(f"maximum capacity {self.max_seat}")

    def book_tickets(self):
        number = int(input("Enter number of passenger:"))
        self.max_seat = 90-number
        source = input("Enter source place name: ")
        destination = input("Enter your destination place:")

        print(f"your ticket is bookd")
        print(f'''
            ticket details
            number of passenger: {number}
            {source} to {destination}
            no. of seat available is : {self.max_seat}
        
        
        ''')



    



  
obj1 = BUS();

        

