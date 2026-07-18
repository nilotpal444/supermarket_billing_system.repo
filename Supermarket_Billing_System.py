def main():
    welcome()
    name=get_name()
    show_menu()
    customer_choice=get_customer_choice()
    price=get_price(customer_choice)
    quantity=get_quanity()
    total=total_amount(price,quantity)
    discount=calculate_discount(total)
    print_bill()


#Welcome the Customer
def welcome():
     print("----------Welcome to Barman Enterprise----------")


#Ask for the customer name 
def get_name():
    name= input("Can I know Your Name Sir/Madam?")
    return name

#Show Menu
def show_menu():
    print("1. Rice : 75Rs per kg")
    print("2. Sugar: 96Rs per kg")
    print("3. Salt: 50Rs per kg")
    print("4. Soap: 30Rs Per Piece")
    print("5. Flour: 50Rs Per kg")
    return show_menu()

#Ask Customer to choose one item
def customer_choice():
    input("What items do you want?")
return customer_choice()


def get_price(customer_choice):
    if customer_choice=="Rice":
         price=75
    elif customer_choice=="Sugar":
        price=96
    elif customer_choice=="Salt":
        price=50
    elif customer_choice=="Soap":
        price=50
    elif customer_choice=="Flour":
        price=50
    else:
        print("Invalid Item")
    
    return price

def get_quanity():
    quantity= int(input("How Much do You Want?"))
    return quantity

def total_amount(price,quantity):
    total=price*quantity
    return total

#Apply Discount 
def apply_discount():
    if 40>total>30:
        print("You get 20% Discount")
    elif total>=50:
        print("You get 30% Discount")
    else:
        print("No Discount!!!")
   
    return discount



#Define the amount of discount
def calculate_discount(total):
    
    if 40>total>30:
        discount=total*20/100
    elif total>=50:
        discount=total*30/100
    else:
        print("No Discount!!!")

    return discount

def discounted_total():
    total_discount=total-discount
    
    return total_discount



#print a neat bill

def print_bill():
   def main():
    welcome()
    name=get_name()
    show_menu()
    customer_choice=get_customer_choice()
    price=get_price(customer_choice)
    quantity=get_quanity()
    total=total_amount(price,quantity)
    calculate_discount(total)
    print_bill()


#Welcome the Customer
def welcome():
     print("----------Welcome to Barman Enterprise----------")


#Ask for the customer name 
def get_name():
    name= input("Can I know Your Name Sir/Madam?")
    return name

#Show Menu
def show_menu():
    print("1. Rice : 75Rs per kg")
    print("2. Sugar: 96Rs per kg")
    print("3. Salt: 50Rs per kg")
    print("4. Soap: 30Rs Per Piece")
    print("5. Flour: 50Rs Per kg")
return show_menu()

#Ask Customer to choose one item
def get_customer_choice():
    customer_choice= input("What Items do you want?")
    return customer_choice


def get_price(customer_choice):
    if customer_choice=="Rice":
         price=75
    elif customer_choice=="Sugar":
        price=96
    elif customer_choice=="Salt":
        price=50
    elif customer_choice=="Soap":
        price=50
    elif customer_choice=="Flour":
        price=50
    else:
        print("Invalid Item")
    
    return price

def get_quanity():
    quantity= int(input("How Much do You Want?"))
    return quantity

def total_amount(price,quantity):
    total=price*quantity
    return total

#Apply Discount 
def apply_discount():
    if 40>total>30:
    print("You get 20% Discount")
    elif total>=50:
    print("You get 30% Discount")
    else:
    print("No Discount!!!")
   
    return discount



#Define the amount of discount
def calculate_discount(total):
    
    if 40>total>30:
        discount=total*20/100
    elif total>=50:
        discount=total*30/100
    else:
        print("No Discount!!!")

    return discount

def discounted_total():
    total_discount=total-discount
    
    return total_discount



#print a neat bill

def print_bill()
   return print_bill

main()