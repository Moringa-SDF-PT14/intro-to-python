def calculate_total(prices, discount=0.0):
    """
    Calculates total price of cart after applying relevant discount
    """
    if not isinstance(prices, list):
        raise TypeError("Prices must be a list")
    if not (0.0 <= discount <= 1.0):
        raise ValueError("Discount must be between 0 and 100%")
    
    subtotal = sum(prices)
    total = subtotal - (discount * subtotal)
    return round(total, 2)

