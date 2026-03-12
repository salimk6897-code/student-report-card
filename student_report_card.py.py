
# STUDENT REPORT CARD - by NJR
# Calculates grades and gives feedback
# Built with Python

# ============================================
# STUDENT INFORMATION
# ============================================
print("=" * 40)
print("    STUDENT REPORT CARD - by NJR")
print("=" * 40)

name = input("Enter your name: ")
english_marks = int(input("English marks (out of 100): "))
science_marks = int(input("Science marks (out of 100): "))
math_marks = int(input("Math marks (out of 100): "))

# ============================================
# CALCULATE AVERAGE
# ============================================
def average_marks(english, science, math):
    return (english + science + math) / 3

average = average_marks(english_marks, science_marks, math_marks)

# ============================================
# DETERMINE GRADE
# ============================================
if average >= 90:
    grade = "A"
    message = f"Excellent work {name}! You are outstanding!"
elif average >= 80:
    grade = "B"
    message = f"Great job {name}! You are doing really well!"
elif average >= 70:
    grade = "C"
    message = f"Good effort {name}! Keep pushing forward!"
else:
    grade = "Need Improvement"
    message = f"Keep working hard {name}! You can do it!"

# ============================================
# DISPLAY RESULTS
# ============================================
marks = [english_marks, science_marks, math_marks]
labels = ["English", "Science", "Math"]

print("\n" + "=" * 40)
print(f"  REPORT CARD FOR: {name.upper()}")
print("=" * 40)
print("\nSUBJECT MARKS:")

for i, mark in enumerate(marks):
    print(f"  {labels[i]}: {mark}/100")

print("\n" + "-" * 40)
print(f"  Average Marks : {average:.2f}/100")
print(f"  Grade         : {grade}")
print("-" * 40)
print(f"\n  {message}")
print("=" * 40)