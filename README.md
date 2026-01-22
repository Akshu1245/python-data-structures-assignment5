# Assignment 5: Module 6 - Data Structures and Strings in Python

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

## 📚 Overview

This repository contains Python programs demonstrating **data structures** in Python, specifically **dictionaries** and **lists**. These examples show how to store, retrieve, and manipulate data efficiently.

---

## 📋 Assignment Tasks

### Task 1: Create a Dictionary of Student Marks
**File:** `student_marks.py`

**Problem Statement:**
1. Creates a dictionary where student names are keys and their marks are values
2. Asks the user to input a student's name
3. Retrieves and displays the corresponding marks
4. If the student's name is not found, displays an appropriate message

### Task 2: Demonstrate List Slicing
**File:** `list_slicing.py`

**Problem Statement:**
1. Creates a list of numbers from 1 to 10
2. Extracts the first five elements from the list
3. Reverses these extracted elements
4. Prints both the extracted list and the reversed list

---

## 🎯 Learning Objectives

After completing these exercises, you will understand:

- ✅ How to create and use dictionaries in Python
- ✅ How to access dictionary values using keys
- ✅ How to check if a key exists in a dictionary
- ✅ How to use list slicing to extract elements
- ✅ How to reverse a list using slicing

---

## 📁 Project Structure

```
python-data-structures-assignment5/
│
├── student_marks.py    # Task 1: Dictionary of student marks
├── list_slicing.py     # Task 2: List slicing demonstration
└── README.md           # This documentation file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your computer
- A terminal or command prompt
- A text editor or IDE (VS Code recommended)

### Running the Programs

#### Task 1: Student Marks Dictionary

```bash
python student_marks.py
```

**If the student exists:**
```
Enter the student's name: Alice
Alice's marks: 85
```

**If the student does not exist:**
```
Enter the student's name: John
Student not found.
```

#### Task 2: List Slicing

```bash
python list_slicing.py
```

**Sample Output:**
```
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]
```

---

## 📖 Concepts Explained

### 1. Dictionaries

Dictionaries store key-value pairs:

```python
student_marks = {
    "Alice": 85,
    "Bob": 90
}
```

**Accessing values:**
```python
marks = student_marks["Alice"]  # Returns 85
```

**Checking if key exists:**
```python
if "Alice" in student_marks:
    print("Found!")
```

### 2. List Slicing

List slicing extracts portions of a list:

| Syntax | Description | Example |
|--------|-------------|---------|
| `list[:5]` | First 5 elements | `[1,2,3,4,5,6,7,8,9,10][:5]` → `[1,2,3,4,5]` |
| `list[5:]` | From index 5 to end | `[1,2,3,4,5,6,7,8,9,10][5:]` → `[6,7,8,9,10]` |
| `list[::-1]` | Reverse the list | `[1,2,3,4,5][::-1]` → `[5,4,3,2,1]` |

### 3. Available Students in Dictionary

| Name | Marks |
|------|-------|
| Alice | 85 |
| Bob | 90 |
| Charlie | 78 |
| Diana | 92 |
| Eve | 88 |

---

## ✅ Features

- Clean, beginner-friendly code with meaningful comments
- Proper handling when student is not found
- Clear output formatting matching expected results
- Demonstrates essential data structure operations

---

## 📝 Reference

Python Course - Module 6: Data Structures and Strings in Python

---

## 👤 Author

**Student Assignment**  
Module 6: Data Structures and Strings in Python

---

*Happy Coding! 🐍*
