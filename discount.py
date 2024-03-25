def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

# Prompting the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculating the final price after applying the discount
final_price = calculate_discount(original_price, discount_percentage)

# Printing the final price after applying the discount
if final_price != original_price:
    print("Final price after applying the discount:", final_price)
else:
    print("No discount applied. Original price:", original_price)
