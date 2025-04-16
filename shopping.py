




def calculate_discount(price, discount_percent):
    # """Calculate the discount amount."""
    if discount_percent >= 20:
        print(f"Final price after discount: {price * (1 - discount_percent / 100)}")
    else:
        print(f"Discount not applicable. Final price: {price}")


#User input for price and discount percentage

price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percentage: "))



calculate_discount(price, discount_percent)  # Example usage of the function