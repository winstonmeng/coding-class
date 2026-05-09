"""
Python Review: Conditional Branching

For Winston and Ido

Topics:
1. if / elif / else
2. comparison operators
3. logical operator: and
4. logical operator: or
5. logical operator: not
6. mixed conditions

Instructions:
- Replace each TODO with the correct condition or value.
- Run the file and check your answers.
- If a question is wrong, read the expected answer and try again.
"""


def check(question_name, your_answer, expected_answer):
    if your_answer == expected_answer:
        print(f"✅ {question_name}: Correct! {your_answer}")
    else:
        print(f"❌ {question_name}: Got {your_answer}, expected {expected_answer}")


# ============================================================
# Section 1: Basic if / elif / else
# ============================================================

print()
print("Section 1: Basic if / elif / else")
print("=================================")

score = 86

if TODO:
    grade = "A"
elif TODO:
    grade = "B"
elif TODO:
    grade = "C"
else:
    grade = "Keep practising"

check("1.1 Grade for score 86", grade, "B")


temperature = 31

if TODO:
    weather = "very hot"
elif TODO:
    weather = "warm"
elif TODO:
    weather = "cool"
else:
    weather = "cold"

check("1.2 Weather for 31 degrees", weather, "warm")


number = -4

if TODO:
    number_type = "zero"
elif TODO:
    number_type = "positive"
else:
    number_type = "negative"

check("1.3 Number type", number_type, "negative")


# ============================================================
# Section 2: Comparison operators
# ============================================================

print()
print("Section 2: Comparison operators")
print("===============================")

age = 11

if TODO:
    age_group = "teenager"
else:
    age_group = "child"

check("2.1 Age group", age_group, "child")


coins = 15

if TODO:
    coin_status = "enough coins"
else:
    coin_status = "not enough coins"

check("2.2 Coin status", coin_status, "enough coins")


secret_number = 8
guess = 8

if TODO:
    guess_result = "correct"
else:
    guess_result = "wrong"

check("2.3 Guess result", guess_result, "correct")


# ============================================================
# Section 3: Logical operator — and
# ============================================================

print()
print("Section 3: Logical operator — and")
print("=================================")

finished_homework = True
packed_bag = True

if TODO:
    school_status = "ready for school"
else:
    school_status = "not ready yet"

check("3.1 Ready for school", school_status, "ready for school")


height_cm = 138
age = 10

if TODO:
    ride_status = "can ride"
else:
    ride_status = "cannot ride"

check("3.2 Ride status", ride_status, "can ride")


has_ticket = True
arrived_on_time = False

if TODO:
    movie_status = "can watch movie"
else:
    movie_status = "missed the movie"

check("3.3 Movie status", movie_status, "missed the movie")


# ============================================================
# Section 4: Logical operator — or
# ============================================================

print()
print("Section 4: Logical operator — or")
print("================================")

day = "Saturday"

if TODO:
    day_type = "weekend"
else:
    day_type = "weekday"

check("4.1 Weekend checker", day_type, "weekend")


animal = "parrot"

if TODO:
    animal_group = "bird"
else:
    animal_group = "not this bird group"

check("4.2 Bird checker", animal_group, "bird")


item = "ruby"

if TODO:
    treasure_status = "treasure"
else:
    treasure_status = "not treasure"

check("4.3 Treasure checker", treasure_status, "treasure")


# ============================================================
# Section 5: Logical operator — not
# ============================================================

print()
print("Section 5: Logical operator — not")
print("=================================")

is_raining = False

if TODO:
    plan = "play outside"
else:
    plan = "stay indoors"

check("5.1 Rain checker", plan, "play outside")


is_locked = True

if TODO:
    door_status = "door is open"
else:
    door_status = "door is locked"

check("5.2 Door checker", door_status, "door is locked")


# ============================================================
# Section 6: Mixed conditions
# ============================================================

print()
print("Section 6: Mixed conditions")
print("===========================")

age = 11
has_ticket = True
is_vip = False

if TODO:
    entry_result = "VIP entry"
elif TODO:
    entry_result = "normal entry"
else:
    entry_result = "no entry"

check("6.1 Soccer match entry", entry_result, "normal entry")


username = "winston"
password = "python123"
has_parent_permission = True
is_banned = False

if TODO:
    login_result = "blocked"
elif TODO:
    login_result = "login successful"
elif TODO:
    login_result = "need parent permission"
else:
    login_result = "wrong username or password"

check("6.2 Game login", login_result, "login successful")


# ============================================================
# Section 7: Boss Review — Element Battle
# ============================================================

print()
print("Section 7: Boss Review — Element Battle")
print("=======================================")

player_element = "grass"
enemy_element = "water"

# Rules:
# - water beats fire
# - fire beats grass
# - grass beats water
# - same element means draw

if TODO:
    battle_result = "draw"
elif TODO:
    battle_result = "win"
elif TODO:
    battle_result = "win"
elif TODO:
    battle_result = "win"
else:
    battle_result = "lose"

check("7.1 Element battle", battle_result, "win")


print()
print("Reflection Questions")
print("====================")
print("1. Why does Python check if / elif conditions from top to bottom?")
print("2. What is the difference between and and or?")
print("3. When would not be useful?")
print("4. Why might the order of conditions change the answer?")
