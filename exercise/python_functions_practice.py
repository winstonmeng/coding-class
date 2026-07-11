"""
Python Practice: Functions

For Winston and Ido

Instructions:
- Replace the TODO placeholders with the correct code.
- Run the file anytime to check your answers.
- The file is designed to keep running even while some answers are unfinished.
- Try to explain the difference between calling, defining, parameters, and return values.
"""


def check(question_name, your_answer, expected_answer):
    if your_answer == expected_answer:
        print(f"✅ {question_name}: Correct! {your_answer}")
    else:
        print(f"❌ {question_name}: Got {your_answer}, expected {expected_answer}")


# Placeholders for unfinished answers. Replace these in the questions below.
TODO_TEXT = ""
TODO_NUMBER = 0
TODO_LIST = []


# ============================================================
# Section 1: Calling built-in functions
# ============================================================

print()
print("Section 1: Calling built-in functions")
print("=====================================")

scores = [10, 16, 30, 21, 25, 28]

# Use max(scores).
answer_1_1 = max(scores)
check("1.1 Highest score with max()", answer_1_1, 30)

# Use min(scores).
answer_1_2 = min(scores)
check("1.2 Lowest score with min()", answer_1_2, 10)

# Use len(pets).
pets = ["cat", "dog", "rabbit", "panda"]
answer_1_3 = len(pets)
check("1.3 Number of pets with len()", answer_1_3, 4)


# ============================================================
# Section 2: Calling functions that belong to data
# ============================================================

print()
print("Section 2: Calling functions that belong to data")
print("================================================")

message = "python makes me happy"

# Use message.upper().
answer_2_1 = message.upper()
check("2.1 Make a string uppercase", answer_2_1, "PYTHON MAKES ME HAPPY")

# Use message.replace("happy", ":D").
answer_2_2 = message.replace("happy",":D")
check("2.2 Replace part of a string", answer_2_2, "python makes me :D")

countdown = [1, 2, 3]

# Replace the next line with a method call that changes countdown into [3, 2, 1].
countdown=list(reversed(countdown))
check("2.3 Reverse a list with reverse()", countdown, [3, 2, 1])


# ============================================================
# Section 3: Define and call a function with no parameters
# ============================================================

print()
print("Section 3: Define and call a function with no parameters")
print("========================================================")


def say_python():
    # Return the exact text: I am learning functions
    return "I am learning functions"


answer_3_1 = say_python()
check("3.1 Call say_python()", answer_3_1, "I am learning functions")


def seconds_per_day():
    hours = 24
    minutes = hours * 60
    seconds = minutes * 60

    # Return the variable seconds.
    return seconds


answer_3_2 = seconds_per_day()
check("3.2 Return seconds in one day", answer_3_2, 86400)


# ============================================================
# Section 4: Parameters
# ============================================================

print()
print("Section 4: Parameters")
print("=====================")


def greet(name):
    # Use the parameter name to return: Hello Sara
    return "Hello " + name


answer_4_1 = greet("Sara")
check("4.1 Greet Sara", answer_4_1, "Hello Sara")


def double_number(number):
    # Return number doubled.
    return number * 2


answer_4_2 = double_number(7)
check("4.2 Double a number", answer_4_2, 14)


def days_to_seconds(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    # Return the variable seconds.
    return seconds


answer_4_3 = days_to_seconds(7)
check("4.3 Convert 7 days to seconds", answer_4_3, 604800)


# ============================================================
# Section 5: Store and use a return value
# ============================================================

print()
print("Section 5: Store and use a return value")
print("=======================================")

seconds_for_three_days = days_to_seconds(3)

# Use seconds_for_three_days to calculate milliseconds.
milliseconds = seconds_for_three_days * 1000
check("5.1 Convert 3 days to milliseconds", milliseconds, 259200000)


def add_points(coins, gems):
    # Coins are worth 10 points. Gems are worth 50 points.
    return coins * 10 + gems * 50


total_points = add_points(4, 2)
check("5.2 Return total game points", total_points, 140)


print()
print("Reflection Questions")
print("====================")
print("1. What does it mean to call a function?")
print("2. Why do some functions need parameters?")
print("3. What is the difference between print() and return?")
print("4. Why is a clear function name helpful?")
print("5. What happens if you call a function before Python has seen its def line?")
