"""
Python Practice: Conditional Branching

For Winston and Ido

Instructions:
1. Fill in the blanks marked ___.
2. Run this file and check the printed answers.
3. Try to explain why each branch is chosen.
"""


# ============================================================
# Question 1: Basic — Theme Park Ride Checker
# ============================================================

import cmath


height_cm = 132
has_adult = False

print("Question 1: Theme Park Ride Checker")
print("-----------------------------------")

# Rules:
# - If height is at least 140 cm, print "You can ride alone."
# - Else if height is at least 120 cm AND has_adult is True, print "You can ride with an adult."
# - Else, print "You cannot ride yet."

if height_cm >= 140:
    print("You can ride alone.")
elif (height_cm >= 120) and (has_adult == True):
    print("You can ride with an adult.")
else:
    print("You cannot ride yet.")


print()
print()


# ============================================================
# Question 2: Basic — Number Classifier
# ============================================================

number = 17

print("Question 2: Number Classifier")
print("-----------------------------")

# Print:
# - "zero" if number is 0
# - "positive" if number is greater than 0
# - "negative" if number is less than 0

if number == 0:
    print("zero")
elif number > 0:
    print("positive")
else:
    print("negative")


print()
print()


# ============================================================
# Question 3: Logical Operators — Homework Reward
# ============================================================

finished_homework = True
read_book = True
helped_at_home = False

print("Question 3: Homework Reward")
print("---------------------------")

# Rules:
# - To earn game time, you must finish homework AND read a book.
# - If you also helped at home, print "You earned bonus game time!"
# - If you only finished homework and read a book, print "You earned game time."
# - Otherwise, print "No game time yet."

if (finished_homework) and (read_book) and (helped_at_home) == True:
    print("You earned bonus game time!")
elif (finished_homework) and (read_book) == True:
    print("You earned game time.")
else:
    print("No game time yet.")


print()
print()


# ============================================================
# Question 4: Disjunction — Magic Door Password
# ============================================================

word = "dragon"

print("Question 4: Magic Door Password")
print("-------------------------------")

# The magic door opens if the word is either:
# - "dragon"
# - "phoenix"
#
# Use OR in your condition.

if (word == "dragon") or (word == "pheonix"):
    print("The magic door opens!")
else:
    print("The door stays closed.")


print()
print()


# ============================================================
# Question 5: Mixed Conditions — Soccer Match Ticket
# ============================================================

age = 11
has_ticket = True
is_vip = False

print("Question 5: Soccer Match Ticket")
print("--------------------------------")

# Rules:
# - A VIP can always enter.
# - Otherwise, a person can enter only if they have a ticket AND age is at least 7.
# - Otherwise, they cannot enter.

if is_vip is True:
    print("Welcome, VIP!")
elif (age >= 7) and (has_ticket == True):
    print("You can enter with your ticket.")
else:
    print("Sorry, you cannot enter.")


print()
print()


# ============================================================
# Question 6: A Bit Challenging — Element Battle
# ============================================================

player_element = "water"
enemy_element = "fire"

print("Question 6: Element Battle")
print("--------------------------")

# Rules:
# - water beats fire
# - fire beats grass
# - grass beats water
# - if both elements are the same, it is a draw
# - otherwise, print "You lose!"

if player_element == enemy_element:
    print("Draw!")
elif (player_element == "water") and (enemy_element == "fire"):
    print("You win!")
elif (player_element == "fire") and (enemy_element == "grass"):
    print("You win!")
elif (player_element == "grass") and (enemy_element == "water"):
    print("You win!")
else:
    print("You lose!")


# ============================================================
# Extra Thinking Questions
# ============================================================

print()
print("Extra Thinking Questions")
print("------------------------")
print("1. What is the difference between if and elif?")
print("2. When do we need else?")
print("3. What does and mean?")
print("4. What does or mean?")
print("5. Why is the order of if / elif checks important?")
