def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: GCD of a and b
    """
    # Convert to positive integers
    a = abs(int(a))
    b = abs(int(b))
    
    # Handle edge cases
    if a == 0 and b == 0:
        return 0
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    
    return a

def main():
    """
    Main function to get user input and calculate GCD.
    """
    print("GCD (Greatest Common Divisor) Calculator")
    print("=" * 40)
    
    try:
        # Get input from user
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        # Calculate GCD
        result = gcd(num1, num2)
        
        # Display result
        print(f"\nThe GCD of {num1} and {num2} is: {result}")
        
    except ValueError:
        print("Error: Please enter valid integers only.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
