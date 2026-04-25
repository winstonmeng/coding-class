"""
Python List Practice: Indexing and Slicing

For Winston and Ido

Instructions:
1. Do not change the original lists.
2. Fill in the blanks marked TODO.
3. Run this file and check your answers.
4. Try to explain what each index or slice means.
"""


# ============================================================
# Question 1: Basic — Mystery Animal Line
# ============================================================

animals = ["cat", "dog", "rabbit", "tiger", "panda", "eagle"]

print("Question 1: Mystery Animal Line")
print("--------------------------------")

# 1. What is the first animal?
first_animal = animals[0]   # TODO: fill in the index
print("1. First animal:", first_animal)

# 2. What is the last animal?
last_animal = animals[-1]    # TODO: use a negative index
print("2. Last animal:", last_animal)

# 3. What is the third animal from the end?
third_from_end = animals[-3] # TODO: use a negative index
print("3. Third animal from the end:", third_from_end)

# 4. What are the first three animals?
first_three = animals[0:3] # TODO: use slicing
print("4. First three animals:", first_three)

# 5. What are the last two animals?
last_two = animals[4::1]       # TODO: use slicing with a negative index
print("5. Last two animals:", last_two)


print()
print()


# ============================================================
# Question 2: A Bit Challenging — Secret Message Decoder
# ============================================================

words = [
    "banana", "Meet", "dragon", "me", "castle",
    "at", "robot", "the", "moon", "library"
]

print("Question 2: Secret Message Decoder")
print("----------------------------------")

# Your goal is to create this secret message:
#
# ["Meet", "me", "at", "the", "library"]
#
# Rules:
# 1. Do not modify the original list.
# 2. Use indexing or slicing.
# 3. Try to use at least one negative index.

# Part A: Get each word one by one using indexes.
word_1 = words[1]   # TODO: should be "Meet"
word_2 = words[3]   # TODO: should be "me"
word_3 = words[5]   # TODO: should be "at"
word_4 = words[-3]   # TODO: should be "the"
word_5 = words[-1]   # TODO: should be "library"; try using a negative index

secret_message = [word_1, word_2, word_3, word_4, word_5]
print("Part A secret message:", secret_message)


# Part B: Bonus challenge
# Can you get the whole secret message with ONE slice?
#
# Hint:
# The secret words are every other word starting from "Meet".

secret_message_bonus = words[1::2]  # TODO: fill in start, stop, step
print("Part B bonus message:", secret_message_bonus)


# ============================================================
# Extra Thinking Questions
# ============================================================

print()
print("Extra Thinking Questions")
print("------------------------")
print("1. Why does words[-1] mean the last word?")
print("2. What does the step number do in words[start:stop:step]?")
print("3. What would words[::-1] do?")
