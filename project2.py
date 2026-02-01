import math

"""In this project we will make a purchase, 
and the program will ask us how many children and adults there are, as well as the price of the meals."""

# Meal Price Calculater
# Introductory
print("\nWelcome to Chicken Burger, " \
    "How can I help you?")

# question to the user 
meal_to_children = float(input("\nWhat is the price of a child's meal? ")) 
meal_to_adults = float(input("What is the price of an adult's meal? "))
count_children = int(input("How many children are there? "))
count_adult = int(input("How many adults are there? "))

# subtotal price

sub_total_1 = count_children * meal_to_children

sub_total_2 = count_adult * meal_to_adults

sub_total_price = sub_total_1 + sub_total_2

# sales_tax
tax = float(input("\nWhat is the sales tax rate? "))
sales_tax = (sub_total_price * tax) / 100
total = sales_tax + sub_total_price

print("\n-----------------------------------")

print("\nYour invoice will be displayed here: ")
print(f"\nSubtotal: ${sub_total_price:.2f} ")
print(f"Sales Tax: ${sales_tax:.2f} ")
print(f"Total: ${total:.2f} ")

print("\n-----------------------------------")

# Change
change_inter = float(input("\nWhat is the payment amount? "))

change_out = change_inter - total

print("\nThank you for your purchase. ")

print(f"\nYou change is: ${change_out:.2f}")

phrase = ("Enjoy your meal!")
print(f"\n{phrase.upper ()}")

