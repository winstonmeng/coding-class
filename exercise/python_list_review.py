"""
Python List Slicing Practice

For Winston and Ido

General syntax:

    lst[start:stop:step]

Practice topics:
1. Extract 1 element with a 0-based index.
2. Extract 1 element with a negative index.
3. Extract a range.
4. Extract a range with a non-1 step.
5. Extract a range in reverse.

Instructions:
- Do not change the original lists.
- Replace each TODO with the correct index or slice number.
- Run the file and check your answers.
"""


def check(question_name, your_answer, expected_answer):
    if your_answer == expected_answer:
        print(f"✅ {question_name}: Correct! {your_answer}")
    else:
        print(f"❌ {question_name}: Got {your_answer}, expected {expected_answer}")


# ============================================================
# Section 1: Warm-up — 0-based indexes
# ============================================================

print()
print("Section 1: Warm-up — 0-based indexes")
print("====================================")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

answer_1_1 = colors[0]   # should be "red"
check("1.1 First color", answer_1_1, "red")

answer_1_2 = colors[2]   # should be "yellow"
check("1.2 Third color", answer_1_2, "yellow")

answer_1_3 = colors[4]   # should be "blue"
check("1.3 Fifth color", answer_1_3, "blue")

answer_1_4 = colors[-1]   # should be "violet"
check("1.4 Seventh color", answer_1_4, "violet")


# ============================================================
# Section 2: Negative indexes
# ============================================================

print()
print("Section 2: Negative indexes")
print("===========================")

animals = ["ant", "bee", "cat", "dog", "eel", "fox", "goat", "hawk"]

answer_2_1 = animals[-1]   # should be "hawk"
check("2.1 Last animal", answer_2_1, "hawk")

answer_2_2 = animals[-2]   # should be "goat"
check("2.2 Second last animal", answer_2_2, "goat")

answer_2_3 = animals[-3]   # should be "fox"
check("2.3 Third last animal", answer_2_3, "fox")

answer_2_4 = animals[3]   # should be "dog"
check("2.4 Fifth animal from the end", answer_2_4, "dog")


# ============================================================
# Section 3: Extract a range
# ============================================================

print()
print("Section 3: Extract a range")
print("==========================")

numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

answer_3_1 = numbers[0:3]   # should be [10, 11, 12]
check("3.1 First three numbers", answer_3_1, [10, 11, 12])

answer_3_2 = numbers[3:-4]   # should be [13, 14, 15]
check("3.2 Middle three numbers", answer_3_2, [13, 14, 15])

answer_3_3 = numbers[6:]   # should be [16, 17, 18, 19]
check("3.3 Last four numbers using positive indexes", answer_3_3, [16, 17, 18, 19])

answer_3_4 = numbers[6::1]       # should be [16, 17, 18, 19]
check("3.4 Last four numbers using start only", answer_3_4, [16, 17, 18, 19])

answer_3_5 = numbers[:4:1]       # should be [10, 11, 12, 13]
check("3.5 First four numbers using stop only", answer_3_5, [10, 11, 12, 13])


# ============================================================
# Section 4: Non-1 step
# ============================================================

print()
print("Section 4: Non-1 step")
print("=====================")

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

answer_4_1 = digits[0:9:2]   # should be [0, 2, 4, 6, 8]
check("4.1 Even digits", answer_4_1, [0, 2, 4, 6, 8])

answer_4_2 = digits[1::2]   # should be [1, 3, 5, 7, 9]
check("4.2 Odd digits", answer_4_2, [1, 3, 5, 7, 9])

answer_4_3 = digits[2:9:3]   # should be [2, 5, 8]
check("4.3 Jump by 3", answer_4_3, [2, 5, 8])

answer_4_4 = digits[0::3]   # should be [0, 3, 6, 9]
check("4.4 Every third digit", answer_4_4, [0, 3, 6, 9])


# ============================================================
# Section 5: Reverse order using negative step
# ============================================================

print()
print("Section 5: Reverse order using negative step")
print("============================================")

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

answer_5_1 = letters[::-1]   # should be ["h", "g", "f", "e", "d", "c", "b", "a"]
check("5.1 Reverse the whole list", answer_5_1, ["h", "g", "f", "e", "d", "c", "b", "a"])

answer_5_2 = letters[6:3:-1]   # should be ["g", "f", "e"]
check("5.2 Reverse from g to e", answer_5_2, ["g", "f", "e"])

answer_5_3 = letters[::-2]   # should be ["h", "f", "d", "b"]
check("5.3 Reverse by step 2", answer_5_3, ["h", "f", "d", "b"])

answer_5_4 = letters[5:0:-2]   # should be ["f", "d", "b"]
check("5.4 Reverse from f by step 2", answer_5_4, ["f", "d", "b"])


# ============================================================
# Section 6: Story Challenge — Space Mission
# ============================================================

print()
print("Section 6: Story Challenge — Space Mission")
print("==========================================")

mission_log = [
    "launch",
    "orbit",
    "scan moon",
    "collect sample",
    "repair antenna",
    "take photo",
    "return",
    "land"
]

answer_6_1 = mission_log[0]          # should be "launch"
check("6.1 First mission step", answer_6_1, "launch")

answer_6_2 = mission_log[-1]          # should be "land", using negative index
check("6.2 Last mission step", answer_6_2, "land")

answer_6_3 = mission_log[2:5]     # should be ["scan moon", "collect sample", "repair antenna"]
check("6.3 Moon work", answer_6_3, ["scan moon", "collect sample", "repair antenna"])

answer_6_4 = mission_log[0:-1:2]  # should be ["launch", "scan moon", "repair antenna", "return"]
check("6.4 Every other mission step starting from launch", answer_6_4, ["launch", "scan moon", "repair antenna", "return"])

answer_6_5 = mission_log[-1:-5:-1]  # should be ["land", "return", "take photo", "repair antenna"]
check("6.5 Last four mission steps in reverse", answer_6_5, ["land", "return", "take photo", "repair antenna"])


# ============================================================
# Section 7: Story Challenge — Secret Code
# ============================================================

print()
print("Section 7: Story Challenge — Secret Code")
print("========================================")

code_words = [
    "apple", "The", "banana", "dragon",
    "key", "is", "under", "robot",
    "the", "blue", "stone", "castle"
]

# Goal 1:
# Extract this secret message:
# ["The", "key", "is", "under", "the", "blue", "stone"]

answer_7_1 = [
    code_words[1],   # "The"
    code_words[4],   # "key"
    code_words[5],   # "is"
    code_words[6],   # "under"
    code_words[-4],   # "the"
    code_words[-3],   # "blue"
    code_words[-2],   # "stone"
]
check("7.1 Secret message using individual indexes", answer_7_1, ["The", "key", "is", "under", "the", "blue", "stone"])

# Goal 2:
# Extract this part using ONE slice:
# ["the", "blue", "stone"]

answer_7_2 = code_words[-4:-1]
check("7.2 Final location using one slice", answer_7_2, ["the", "blue", "stone"])

# Goal 3:
# Extract this reversed clue using ONE slice:
# ["stone", "blue", "the"]

answer_7_3 = code_words[-2:-5:-1]
check("7.3 Reversed final location", answer_7_3, ["stone", "blue", "the"])


# ============================================================
# Section 8: Boss Challenge — Build the Spell
# ============================================================

print()
print("Section 8: Boss Challenge — Build the Spell")
print("===========================================")

spell_parts = [
    "fire", "moon", "water", "star", "earth",
    "cloud", "wind", "sun", "light", "shadow",
    "stone", "spark"
]

# Challenge A:
# Use slicing to get:
# ["moon", "star", "cloud", "sun"]

answer_8_1 = spell_parts[1:8:2]
check("8.1 Every other magic word from moon to sun", answer_8_1, ["moon", "star", "cloud", "sun"])

# Challenge B:
# Use slicing to get:
# ["spark", "shadow", "sun", "cloud"]

answer_8_2 = spell_parts[-1:-8:-2]
check("8.2 Reverse magic jump", answer_8_2, ["spark", "shadow", "sun", "cloud"])

# Challenge C:
# Use slicing to get:
# ["light", "wind", "earth", "water", "fire"]

check("8.3 Reverse spell path", answer_8_3, ["light", "wind", "earth", "water", "fire"])


# ============================================================
# Final Reflection
# ============================================================

print()
print("Final Reflection")
print("================")
print("1. In lst[start:stop:step], does Python include the stop index?")
print("2. What does a negative index count from?")
print("3. What does a negative step do?")
print("4. Why does lst[1:5:-1] give an empty list?")
print("5. What is one slicing question you can create for someone else?")
