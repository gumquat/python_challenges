def find_the_discount(price, discount):
    if isinstance(price, int) and isinstance(discount, int):
        discount_amount = price * discount / 100
        final_price = price - discount_amount
        return final_price
    else:
        return ValueError("One of the inputs is not type int")

print("The input values are: Price :100, Discount: 25. And should return 'Discounted price is 75.0' on the next line")
print("Discounted price is {}".format(find_the_discount(100, 25)))