def calculate_discount(price, customer_type):
    # Variable non utilisée (problème détectable)
    unused_variable = "this is not used"
    
    # Magic numbers (problème de maintenabilité)
    if customer_type == "premium":
        if price > 1000:
            return price * 0.2  # Magic number
        else:
            return price * 0.1  # Magic number
    elif customer_type == "regular":
        if price > 1000:
            return price * 0.1  # Duplication du 0.1
        else:
            return price * 0.05  # Magic number
    else:
        return 0

def get_tax_amount(price, tax_rate):
    # Code dupliqué volontairement
    if price > 100:
        result = price * tax_rate
        return result
    else:
        return 0

def get_shipping_cost(price, shipping_rate):
    # Code identique à get_tax_amount (duplication)
    if price > 100:
        result = price * shipping_rate
        return result
    else:
        return 0