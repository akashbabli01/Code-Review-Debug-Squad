def divide(numerator, denominator):
    if not isinstance(numerator, (int, float)):
        raise TypeError("Numerator must be numeric")

    if not isinstance(denominator, (int, float)):
        raise TypeError("Denominator must be numeric")

    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return numerator / denominator
