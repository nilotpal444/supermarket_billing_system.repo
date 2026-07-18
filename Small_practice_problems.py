def main():
    display_welcome()
    customer=customer_name()
    grand_total=0

    while True:
        show_menu()

        choice = choose_item()
        quantity = choose_quantity()
        price = choice_price(choice)
        total = find_total(price, quantity)

        grand_total=update_grand_total(grand_total,total)

        print("Item Total: Rs", total)

        if not another_item():
             break
        
        
    
    




#Welcome the Customer
def display_welcome():
    print("=" * 20, "Welcome to Shopzyy", "=" * 20)

#Ask Customer Name
def customer_name():
    customer= input("Can I know Your name Sir/Madam?")
    print("Customer:", customer)
    return customer

#Decor
decor=print("-" * 62)


#List out the Menu
def show_menu():
    menu={
    "1. Rice" : "Rs 57/kg",
    "2. Sugar": "Rs 50/kg",
    "3. Meat " : "Rs 150/kg",
    "4. Fish" : "Rs 120/kg",
    "5. Wheat" : "Rs 65/kg",
    "6. Kaju" :  "Rs 60/kg"
    }
    for item in menu:
        print(item)

#Choosing what item is required
def choose_item():
   while True:
        choice = int(input("Enter Item Number (1-6): "))
        if 1<= choice <=6:
                 return choice
        else:
                print("Invalid Number! Type a number between 1-6")

#Ask Quantity
def choose_quantity():
    quantity= int(input("Enter quantity:"))
    return quantity

#defining choice and quantity
def choice_price(choice):
    prices=[57,50,150,120,65,60]
    price=prices[choice-1]
    
    return price

#Find Total of the choosen item
def find_total(price, quantity):
    total= price*quantity
    return total

#Display Total Amount to Customer
def total_amount(total):
    print("Total Amount:", total)


#Ask if customer needs another item
def another_item():
    while True:
        want= input("Do You want another item?").lower()
           
        if want=="yes":
            return True
        elif want=="no":
            return False
        else:
            print("Invalid Option! Type Yes or No")


#Find the Grant Total of all the items
def update_grand_total(grand_total,total):
     grand_total=grand_total+total
     print("Grand Total is :" ,grand_total)
     return grand_total


    
        

    
main()