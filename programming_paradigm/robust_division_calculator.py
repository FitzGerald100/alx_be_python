# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs division while handling division by zero and non-numeric inputs."""
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        denom = float(denominator)
        
        # Attempt division
        result = num / denom
        return f"Result: {result:.2f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter a numeric value only."
    
