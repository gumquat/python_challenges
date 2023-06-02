def find_the_discount(price, discount):
    if isinstance(price, int) and isinstance(discount, int):
        discount_amount = price * discount / 100
        final_price = price - discount_amount
        return final_price
    else:
        return ValueError("One of the inputs is not type int")