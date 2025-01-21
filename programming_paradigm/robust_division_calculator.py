def safe_divide(numerator, denominator):
    """Performs division while handling division by zero and non-numeric inputs."""
    try:
        num = float(numerator)
        denom = float(denominator)


        result = num / denom
        return f"Result: {result:.2f}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
    except ValueError:
        return "Error: Both inputs must be numeric."
    
