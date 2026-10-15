# 1. Variables and data types

student_name = "Vishesh Pokhriyal"
age = 20
cgpa = 8.1
is_learning_python = True

print("=== Variables and Data Types ===")
print("Name:", student_name, "| type:", type(student_name).__name__)
print("Age:", age, "| type:", type(age).__name__)
print("CGPA:", cgpa, "| type:", type(cgpa).__name__)
print("Learning Python:", is_learning_python, "| type:", type(is_learning_python).__name__)

# 2. Conditional statements

print("\n=== Conditions ===")
marks = 76
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Needs improvement"
print(f"Marks: {marks}; Grade: {grade}")

# 3. Loops

print("\n=== Loops ===")
for number in range(1, 6):
    print(number, "squared =", number * number)

countdown = 3
while countdown > 0:
    print("Countdown:", countdown)
    countdown -= 1

# 4. Functions

def calculate_average(numbers):
    """Return the arithmetic mean of a non-empty list."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

scores = [72, 85, 91, 68]
print("\n=== Functions ===")
print("Scores:", scores)
print("Average:", calculate_average(scores))

# 5. Python data structures

print("\n=== Data Structures ===")
topics = ["variables", "conditions", "loops"]  # list
unique_topics = {"loops", "functions", "loops"}  # set
student = {"name": student_name, "age": age}  # dictionary
coordinates = (30.3, 78.0)  # tuple
print("List:", topics)
print("Set (unique values):", unique_topics)
print("Dictionary:", student)
print("Tuple:", coordinates)

# 6. Easy practice: count vowels

def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)

print("\n=== Practice Problem ===")
sample = "Python programming"
print(f"Vowels in {sample!r}:", count_vowels(sample))