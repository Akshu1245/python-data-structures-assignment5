# =============================================================================
# Program: Student Marks Dictionary
# Description: This program creates a dictionary of student marks and allows
#              the user to look up a student's marks by name.
# Module: Data Structures and Strings in Python
# =============================================================================

def main():
    """
    Main function that manages student marks using a dictionary.
    """
    
    # Step 1: Create a dictionary with student names as keys and marks as values
    student_marks = {
        "Alice": 85,
        "Bob": 90,
        "Charlie": 78,
        "Diana": 92,
        "Eve": 88
    }
    
    # Step 2: Ask the user to input a student's name
    name = input("Enter the student's name: ")
    
    # Step 3: Check if the student exists and display marks
    if name in student_marks:
        # Student found - display their marks
        print(f"{name}'s marks: {student_marks[name]}")
    else:
        # Student not found - display appropriate message
        print("Student not found.")


# Run the program
if __name__ == "__main__":
    main()
