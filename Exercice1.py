print ("Please enter your name: ")
name = str(input())

if name == "VIP":
    print("Enjoy the show for free!")
else:
    print ("How many tickets would you like to buy?")
    tickets = int(input())  
    ticket_price = 15.5  
    total_cost = tickets * ticket_price  
    print("The total cost is:", total_cost)
    