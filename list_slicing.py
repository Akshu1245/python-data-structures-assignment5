# =============================================================================
# Program: List Slicing Demonstration
# Description: This program demonstrates list slicing by extracting and
#              reversing elements from a list.
# Module: Data Structures and Strings in Python
# =============================================================================

def main():
    """
    Main function that demonstrates list slicing operations.
    """
    
    # Step 1: Create a list of numbers from 1 to 10
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original list: {original_list}")
    
    # Step 2: Extract the first five elements using slicing
    # Syntax: list[start:end] - extracts from index 'start' to 'end-1'
    extracted_elements = original_list[:5]
    print(f"Extracted first five elements: {extracted_elements}")
    
    # Step 3: Reverse the extracted elements using slicing
    # Syntax: list[::-1] - reverses the list
    reversed_elements = extracted_elements[::-1]
    print(f"Reversed extracted elements: {reversed_elements}")


# Run the program
if __name__ == "__main__":
    main()
