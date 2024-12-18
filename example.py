def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

def test_add_numbers():
    """Test cases for add_numbers function."""
    # Test positive numbers
    assert add_numbers(2, 3) == 5
    
    # Test negative numbers
    assert add_numbers(-1, 1) == 0
    
    # Test zeros
    assert add_numbers(0, 0) == 0
    
    print("All tests passed!")

if __name__ == "__main__":
    test_add_numbers()