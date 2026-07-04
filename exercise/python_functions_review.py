"""
Python Review: Functions

For Winston and Ido

Topics:
1. calling functions
2. defining functions
3. parameters
4. return values
5. functions that use string/list methods
6. functions that combine loops and conditionals

Instructions:
- Replace each TODO placeholder with the correct code.
- Run the file and check your answers.
- The file keeps running while unfinished, so you can solve a few questions at a time.
- If a question is wrong, read the expected answer and try again.
"""


def check(question_name, your_answer, expected_answer):
    if your_answer == expected_answer:
        print(f"✅ {question_name}: Correct! {your_answer}")
    else:
        print(f"❌ {question_name}: Got {your_answer}, expected {expected_answer}")


# Placeholders for unfinished answers. Replace these in the questions below.
TODO_BOOL = False
TODO_TEXT = ""
TODO_NUMBER = 0
TODO_LIST = []


# ============================================================
# Section 1: Call functions and store their return values
# ============================================================

print()
print("Section 1: Call functions and store their return values")
print("=======================================================")


def make_uppercase(word):
    return word.upper()


def find_biggest(numbers):
    return max(numbers)


def add_excited_ending(sentence):
    return sentence + "!"


# Call make_uppercase("python").
answer_1_1 = TODO_TEXT
check("1.1 Call make_uppercase()", answer_1_1, "PYTHON")

# Call find_biggest([4, 19, 7, 12]).
answer_1_2 = TODO_NUMBER
check("1.2 Call find_biggest()", answer_1_2, 19)

# Store the return value from add_excited_ending("Functions are useful").
answer_1_3 = TODO_TEXT
check("1.3 Store a return value", answer_1_3, "Functions are useful!")


# ============================================================
# Section 2: Define functions with parameters
# ============================================================

print()
print("Section 2: Define functions with parameters")
print("==========================================")


def make_badge(name, level):
    # Return text like: Sara - Level 5
    return TODO_TEXT


check("2.1 Badge for Sara", make_badge("Sara", 5), "Sara - Level 5")
check("2.2 Badge for Winston", make_badge("Winston", 12), "Winston - Level 12")


def rectangle_area(width, height):
    # Return the area of a rectangle.
    return TODO_NUMBER


check("2.3 Rectangle 4 by 6", rectangle_area(4, 6), 24)
check("2.4 Rectangle 3 by 9", rectangle_area(3, 9), 27)


def first_and_last(word):
    # Return the first letter plus the last letter.
    return TODO_TEXT


check("2.5 First and last of python", first_and_last("python"), "pn")
check("2.6 First and last of dragon", first_and_last("dragon"), "dn")


# ============================================================
# Section 3: Return values for time conversion
# ============================================================

print()
print("Section 3: Return values for time conversion")
print("============================================")


def convert_days_to_seconds(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    # Return the variable seconds.
    return TODO_NUMBER


check("3.1 Seconds in 1 day", convert_days_to_seconds(1), 86400)
check("3.2 Seconds in 7 days", convert_days_to_seconds(7), 604800)


def convert_days_to_milliseconds(days):
    seconds = convert_days_to_seconds(days)

    # Use the return value stored in seconds.
    return TODO_NUMBER


check("3.3 Milliseconds in 2 days", convert_days_to_milliseconds(2), 172800000)
check("3.4 Milliseconds in 5 days", convert_days_to_milliseconds(5), 432000000)


def total_seconds(days, hours, minutes):
    # Return the total number of seconds.
    return TODO_NUMBER


check("3.5 1 day, 2 hours, 3 minutes", total_seconds(1, 2, 3), 93780)
check("3.6 0 days, 1 hour, 30 minutes", total_seconds(0, 1, 30), 5400)


# ============================================================
# Section 4: Functions with if / elif / else
# ============================================================

print()
print("Section 4: Functions with if / elif / else")
print("==========================================")


def choose_rank(points):
    # Rank rules:
    # - Dragon Master: 95 or more
    # - Sky Rider: 80 up to 94
    # - Egg Helper: 65 up to 79
    # - Training Day: anything else
    if TODO_BOOL:
        return "Dragon Master"
    elif TODO_BOOL:
        return "Sky Rider"
    elif TODO_BOOL:
        return "Egg Helper"
    else:
        return "Training Day"


check("4.1 Rank for 99", choose_rank(99), "Dragon Master")
check("4.2 Rank for 86", choose_rank(86), "Sky Rider")
check("4.3 Rank for 65", choose_rank(65), "Egg Helper")
check("4.4 Rank for 40", choose_rank(40), "Training Day")


def can_open_portal(has_spell_book, said_magic_word, has_backup_charm):
    # The portal opens when:
    # - there is a spell book, AND
    # - either the magic word was said OR there is a backup charm.
    if TODO_BOOL:
        return "portal opens"
    else:
        return "portal stays shut"


check("4.5 Portal with backup charm", can_open_portal(True, False, True), "portal opens")
check("4.6 Portal without spell book", can_open_portal(False, True, True), "portal stays shut")
check("4.7 Portal with magic word", can_open_portal(True, True, False), "portal opens")


# ============================================================
# Section 5: Functions that use loops
# ============================================================

print()
print("Section 5: Functions that use loops")
print("===================================")


def count_treasures(items):
    treasure_count = 0

    for item in items:
        # Count only "coin", "ruby", and "diamond".
        if TODO_BOOL:
            treasure_count = TODO_NUMBER

    return treasure_count


check("5.1 Count treasure list A", count_treasures(["coin", "rock", "ruby", "leaf"]), 2)
check("5.2 Count treasure list B", count_treasures(["stick", "diamond", "coin", "coin"]), 3)


def total_game_points(actions):
    points = 0

    for action in actions:
        # coin gives 10, enemy gives 50, finish gives 100, anything else gives 0.
        if TODO_BOOL:
            points = TODO_NUMBER
        elif TODO_BOOL:
            points = TODO_NUMBER
        elif TODO_BOOL:
            points = TODO_NUMBER

    return points


check("5.3 Game points A", total_game_points(["coin", "jump", "enemy", "finish"]), 160)
check("5.4 Game points B", total_game_points(["coin", "coin", "enemy"]), 70)


# ============================================================
# Section 6: Method-style function calls inside your functions
# ============================================================

print()
print("Section 6: Method-style function calls inside your functions")
print("===========================================================")


def clean_message(message):
    # Replace "bug" with "feature", then return the message in uppercase.
    return TODO_TEXT


check("6.1 Clean one bug message", clean_message("this bug is tiny"), "THIS FEATURE IS TINY")
check("6.2 Clean two bug messages", clean_message("bug found another bug"), "FEATURE FOUND ANOTHER FEATURE")


def make_reversed_copy(items):
    # Make a copy, reverse the copy, and return it.
    # Do not change the original list.
    result = items.copy()
    TODO_LIST
    return result


original_order = ["cat", "dog", "rabbit"]
reversed_order = make_reversed_copy(original_order)

check("6.3 Reversed copy", reversed_order, ["rabbit", "dog", "cat"])
check("6.4 Original list unchanged", original_order, ["cat", "dog", "rabbit"])


# ============================================================
# Section 7: Boss Review — combine everything
# ============================================================

print()
print("Section 7: Boss Review — combine everything")
print("===========================================")


def mission_report(name, days, coins, gems):
    # Return a sentence like:
    # SARA explored for 172800 seconds and earned 90 points!
    #
    # Rules:
    # - name should be uppercase
    # - use convert_days_to_seconds(days)
    # - coins are worth 10 points
    # - gems are worth 50 points
    return TODO_TEXT


check(
    "7.1 Sara mission report",
    mission_report("Sara", 2, 4, 1),
    "SARA explored for 172800 seconds and earned 90 points!",
)
check(
    "7.2 Ido mission report",
    mission_report("Ido", 1, 3, 2),
    "IDO explored for 86400 seconds and earned 130 points!",
)


print()
print("Reflection Questions")
print("====================")
print("1. Why should a function usually return a value instead of only printing?")
print("2. How can tests with different inputs show whether a function really uses its parameters?")
print("3. Why is convert_days_to_seconds a clearer name than print_seconds_per_day here?")
print("4. What is the difference between message.upper() and upper(message)?")
print("5. Why did make_reversed_copy copy the list before reversing it?")
