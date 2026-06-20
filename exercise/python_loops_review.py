"""
Python Review: Loops

For Winston and Ido

Topics:
1. for loops over lists
2. range()
3. range() with step
4. accumulators
5. if inside a loop
6. while loops
7. combining loops and conditionals

Instructions:
- Replace each TODO with the correct code.
- Run the file and check your answers.
- If a question is wrong, read the expected answer and try again.
"""


def check(question_name, your_answer, expected_answer):
    if your_answer == expected_answer:
        print(f"✅ {question_name}: Correct! {your_answer}")
    else:
        print(f"❌ {question_name}: Got {your_answer}, expected {expected_answer}")


# ============================================================
# Section 1: for loops over lists
# ============================================================

print()
print("Section 1: for loops over lists")
print("===============================")

animals = ["cat", "dog", "rabbit"]
animal_sentence = ""

for animal in animals:
    animal_sentence = animal_sentence + animal + " "

check("1.1 Animal sentence", animal_sentence, "cat dog rabbit ")


colors = ["red", "blue", "green"]
color_count = 0

for color in colors:
    color_count = color_count + 1

check("1.2 Count colors", color_count, 3)


# ============================================================
# Section 2: range()
# ============================================================

print()
print("Section 2: range()")
print("==================")

numbers = []

for number in range(1, 6):
    numbers.append(number)

check("2.1 Numbers 1 to 5", numbers, [1, 2, 3, 4, 5])


zero_to_four = []

for number in range(0, 5):
    zero_to_four.append(number)

check("2.2 Numbers 0 to 4", zero_to_four, [0, 1, 2, 3, 4])


countdown_small = []

for number in range(5, 0, -1):
    countdown_small.append(number)

check("2.3 Countdown 5 to 1 with range", countdown_small, [5, 4, 3, 2, 1])


# ============================================================
# Section 3: range() with step
# ============================================================

print()
print("Section 3: range() with step")
print("============================")

even_numbers = []

for number in range(2, 11, 2):
    even_numbers.append(number)

check("3.1 Even numbers", even_numbers, [2, 4, 6, 8, 10])


jump_by_three = []

for number in range(3, 13, 3):
    jump_by_three.append(number)

check("3.2 Jump by three", jump_by_three, [3, 6, 9, 12])


reverse_even = []

for number in range(10, 1, -2):
    reverse_even.append(number)

check("3.3 Reverse even numbers", reverse_even, [10, 8, 6, 4, 2])


# ============================================================
# Section 4: Accumulators
# ============================================================

print()
print("Section 4: Accumulators")
print("=======================")

scores = [10, 20, 15, 5]
total = 0

for score in scores:
    total = score + total

check("4.1 Total score", total, 50)


numbers = [4, 7, 2, 9]
product = 1

for number in numbers:
    product = product * number

check("4.2 Product", product, 504)


words = ["I", "love", "Python"]
sentence = ""

for word in words:
    sentence = sentence + word + " "

check("4.3 Build sentence", sentence, "I love Python ")


# ============================================================
# Section 5: if inside a loop
# ============================================================

print()
print("Section 5: if inside a loop")
print("===========================")

numbers = [3, 12, 7, 20, 5, 18]
big_count = 0

for number in numbers:
    if number > 10:
        big_count = big_count + 1

check("5.1 Count numbers greater than 10", big_count, 3)


words = ["apple", "banana", "pear", "blueberry"]
long_words = 0

for word in words:
    if len(word) > 5 :
        long_words = long_words + 1

check("5.2 Count long words", long_words, 2)


items = ["coin", "rock", "ruby", "stick", "coin", "diamond", "leaf"]
treasure_count = 0

for item in items:
    if item == "coin" or item == "ruby" or item == "diamond":
        treasure_count = treasure_count + 1

check("5.3 Count treasures", treasure_count, 4)


# ============================================================
# Section 6: while loops
# ============================================================

print()
print("Section 6: while loops")
print("======================")

countdown = []
count = 5

while count != 0:
    countdown.append(count)
    count = count - 1

check("6.1 Countdown", countdown, [5, 4, 3, 2, 1])


energy_list = []
energy = 0

while energy != 100:
    energy = energy + 20
    energy_list.append(energy)

check("6.2 Energy charger", energy_list, [20, 40, 60, 80, 100])


doubles = []
number = 1

while number != 32 :
    doubles.append(number)
    number = number * 2

check("6.3 Double until 16", doubles, [1, 2, 4, 8, 16])


# ============================================================
# Section 7: Boss Review — Password Attempts
# ============================================================

print()
print("Section 7: Boss Review — Password Attempts")
print("==========================================")

passwords = ["apple", "dragon", "python123", "banana"]
correct_password = "python123"
found_password = False

for password in passwords:
    if password == "python123":
        found_password = True

check("7.1 Found password", found_password, True)


# ============================================================
# Section 8: Boss Review — Game Points
# ============================================================

print()
print("Section 8: Boss Review — Game Points")
print("====================================")

actions = ["coin", "jump", "coin", "enemy", "coin", "enemy", "finish"]
points = 0

# Rules:
# - coin gives 10 points
# - enemy gives 50 points
# - finish gives 100 points
# - other actions give 0 points

for action in actions:
    if action == "coin":
        points = points + 10
    elif action == "enemy":
        points = points + 50
    elif action == "finish":
        points = points + 100

check("8.1 Game points", points, 230)


print()
print("Reflection Questions")
print("====================")
print("1. What does range(start, stop, step) do?")
print("2. Why do we often update a variable inside a loop?")
print("3. What is the difference between a for loop and a while loop?")
print("4. What could cause a while loop to run forever?")
print("5. How can if statements and loops work together?")
