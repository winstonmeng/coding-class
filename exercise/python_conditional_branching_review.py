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
- Each line uses the placeholder name TODO until you fill it in.
- Replace the whole word TODO with your condition (for example: dragon_points >= 95).
- While TODO is still there, it counts as False so the file runs and you can see checks for the parts you already solved.
- Run the file anytime to check your answers.
- If a question is wrong, read the expected answer and try again.
- Try to explain why your condition works before moving on.

Difficulty: each section expects careful reading of boundaries and order of branches.
"""


def check(question_name, your_answer, expected_answer):
    if your_answer == expected_answer:
        print(f"✅ {question_name}: Correct! {your_answer}")
    else:
        print(f"❌ {question_name}: Got {your_answer}, expected {expected_answer}")


# Placeholder for unfinished conditions: keeps the file runnable (TODO is always false).
# When you solve a line, replace TODO with your full expression, e.g. dragon_points >= 95.
TODO = False


# ============================================================
# Section 1: if / elif / else — tight score bands
# ============================================================

print()
print("Section 1: Dragon Academy — exact score bands")
print("=============================================")

# Rank rules (points are inclusive on the lower bound where a range is given):
# - Dragon Master: 95 or more
# - Sky Rider: 80 up to and including 94
# - Egg Helper: 65 up to and including 79
# - Training Day: anything else

dragon_points = 86

if dragon_points >= 95:
    rank = "Dragon Master"
elif dragon_points >=80:
    rank = "Sky Rider"
elif dragon_points >=65:
    rank = "Egg Helper"
else:
    rank = "Training Day"

check("1.1 Rank for 86 points (must use ranges)", rank, "Sky Rider")


# Suit rules (degrees Celsius on the moon base):
# - lava shield: strictly above 40
# - explorer mode: above 25 and at most 40
# - jacket mode: above 15 and at most 25
# - penguin mode: everything else

moon_temperature = 31

if moon_temperature > 40:
    space_suit_mode = "lava shield"
elif moon_temperature > 25:
    space_suit_mode = "explorer mode"
elif moon_temperature >15:
    space_suit_mode = "jacket mode"
else:
    space_suit_mode = "penguin mode"

check("1.2 Suit mode at 31 °C (watch strict > vs >=)", space_suit_mode, "explorer mode")


# Submarine vertical speed (metres per minute; negative means diving):
# - staying level: exactly 0
# - going up: strictly positive
# - going down: strictly negative
# (Use three separate branches — no “catch-all” else for the real answer.)

submarine_depth_change = -4

if submarine_depth_change == 0:
    depth_status = "staying level"
elif submarine_depth_change > 0 :
    depth_status = "going up"
elif submarine_depth_change < 0:
    depth_status = "going down"
else:
    depth_status = "incomplete (fill all three conditions above)"

check("1.3 Submarine motion", depth_status, "going down")


# ============================================================
# Section 2: Comparisons — ranges and “close enough”
# ============================================================

print()
print("Section 2: Secret base — ranges and near-matches")
print("================================================")

# Squad rules by age:
# - teen squad: 13 through 19 inclusive
# - junior squad: 8 through 12 inclusive
# - cadet squad: anything else

hero_age = 11

if hero_age >= 13:
    mission_group = "teen squad"
elif hero_age >= 8:
    mission_group = "junior squad"
else:
    mission_group = "cadet squad"

check("2.1 Squad for age 11 (inclusive ranges)", mission_group, "junior squad")


# Portal needs enough crystals, but not too many (overloaded):
# - portal powered: at least 12 and at most 18 crystals
# - otherwise: need more crystals

energy_crystals = 15

if energy_crystals >= 12:
    crystal_status = "portal powered"
else:
    crystal_status = "need more crystals"

check("2.2 Crystal window [12, 18]", crystal_status, "portal powered")


# Vault opens if the guess is exact OR off by exactly 1 (too easy otherwise).

secret_number = 8
guess = 7

if guess == secret_number or guess == secret_number - 1 or guess == secret_number + 1 :
    vault_result = "vault opens"
else:
    vault_result = "alarm rings"

check("2.3 Vault: exact or within 1", vault_result, "vault opens")


# ============================================================
# Section 3: and — every requirement matters
# ============================================================

print()
print("Section 3: Team quest — stack every requirement")
print("===============================================")

has_map = True
has_lantern = True
has_rope = True

if has_map == True and has_lantern == True and has_rope == True:
    quest_status = "ready for the cave quest"
else:
    quest_status = "not ready yet"

check("3.1 Cave prep (map + lantern + rope)", quest_status, "ready for the cave quest")


# Canyon zipline: tall enough, brave enough, and not injured.

height_cm = 138
bravery_level = 10
is_injured = False

if height_cm == 138 and bravery_level == 10 and is_injured == False:
    zipline_status = "can cross the canyon"
else:
    zipline_status = "cannot cross yet"

check("3.2 Zipline (height, bravery, not injured)", zipline_status, "can cross the canyon")


# Portal: spell book required, AND you must either say the word OR show a backup charm.

has_spell_book = True
said_magic_word = False
has_backup_charm = True

if has_spell_book == True and said_magic_word == True or has_backup_charm == True:
    spell_result = "portal opens"
else:
    spell_result = "portal stays shut"

check("3.3 Portal (book and (word or charm))", spell_result, "portal opens")


# ============================================================
# Section 4: or — more than one winning path
# ============================================================

print()
print("Section 4: Bonus day — any special day counts")
print("=============================================")

day = "Friday"
is_public_holiday = True

if is_public_holiday == True:
    mission_day = "bonus quest day"
else:
    mission_day = "school day"

check("4.1 Weekend or holiday", mission_day, "bonus quest day")


animal = "raven"

if animal == "raven":
    sky_team = "bird squad"
else:
    sky_team = "not in bird squad"

check("4.2 Bird squad (several bird names)", sky_team, "bird squad")


item = "topaz"

if item == "topaz":
    chest_result = "treasure found"
else:
    chest_result = "just old socks"

check("4.3 Treasure types (several gems)", chest_result, "treasure found")


# ============================================================
# Section 5: not — including combined conditions
# ============================================================

print()
print("Section 5: Sneaky opposites and combined logic")
print("=============================================")

monster_awake = False

if monster_awake == False:
    sneak_plan = "tiptoe past the monster"
else:
    sneak_plan = "hide behind the rocks"

check("5.1 Monster asleep?", sneak_plan, "tiptoe past the monster")


# Shield: you need a new shield if the shield is broken OR the battery is dead.
# “Shield still works” only when neither problem exists.
# Tip: one clean way is not (A or B) for the else branch.

shield_broken = True
battery_dead = False

# Put the “broken” outcome on the if-branch so an empty TODO is not a false green.
if shield_broken == True:
    defense_status = "need a new shield"
else:
    defense_status = "shield still works"

check("5.2 Shield + battery (De Morgan style)", defense_status, "need a new shield")


# ============================================================
# Section 6: Mixed conditions — order matters
# ============================================================

print()
print("Section 6: Mixed conditions — read priority rules")
print("=================================================")

# Arena rules (check from top to bottom):
# - legend entrance: VIP streamer (always), OR level at least 15 with a battle pass
# - standard entrance: level at least 10 with a battle pass (and not a legend case above)
# - no entrance: everything else

level = 11
has_battle_pass = True
is_streamer = False

if level >= 15 and has_battle_pass == True:
    arena_result = "legend entrance"
elif level >= 10 and has_battle_pass == True:
    arena_result = "standard entrance"
else:
    arena_result = "no entrance"

check("6.1 Arena priority (streamer / level+pass)", arena_result, "standard entrance")


# Login rules (order is part of the puzzle):
# 1) banned accounts are always blocked
# 2) wrong username or password → wrong username or password
# 3) correct login but no parent permission → need parent permission
# 4) otherwise → login successful

username = "winston"
password = "python123"
has_parent_permission = True
is_banned = False

if is_banned == True:
    login_result = "blocked"
elif password != "python123" or username != "winston":
    login_result = "wrong username or password"
elif has_parent_permission == False:
    login_result = "need parent permission"
elif has_parent_permission == True:
    login_result = "login successful"
else:
    login_result = "incomplete (fill all four conditions above)"

check("6.2 Login branch order", login_result, "login successful")


# Scholarship bands (exclusive upper bounds except the top tier):
# - full ride: average at least 95
# - half ride: average at least 88 but below 95
# - book stipend: average at least 80 but below 88
# - none: below 80

test_average = 91

if test_average >= 95:
    scholarship = "full ride"
elif test_average >= 88:
    scholarship = "half ride"
elif test_average >= 80:
    scholarship = "book stipend"
else:
    scholarship = "none"

check("6.3 Scholarship tiers at average 91", scholarship, "half ride")


# ============================================================
# Section 7: Boss — element battle (two fights)
# ============================================================

print()
print("Section 7: Boss — element dragon battle")
print("=======================================")

player_element = "grass"
enemy_element = "water"

# Rules:
# - water beats fire
# - fire beats grass
# - grass beats water
# - same element means draw

if player_element == enemy_element:
    battle_result = "draw"
elif player_element == "water" and enemy_element == "fire":
    battle_result = "win"
elif player_element == "fire" and enemy_element == "grass":
    battle_result = "win"
elif player_element == "grass" and enemy_element == "water":
    battle_result = "win"
else:
    battle_result = "lose"

check("7.1 Grass vs water", battle_result, "win")


player_element_2 = "fire"
enemy_element_2 = "water"

if player_element_2 == enemy_element_2:
    battle2 = "draw"
elif player_element_2 == "water" and enemy_element_2 == "fire":
    battle2 = "win"
elif player_element_2 == "fire" and enemy_element_2 == "grass":
    battle2 = "win"
elif player_element_2 == "grass" and enemy_element_2 == "water":
    battle2 = "win"
elif player_element_2 == "fire" and enemy_element_2 == "water":
    battle2 = "lose"
else:
    battle2 = "incomplete (fill all five conditions above)"

check("7.2 Fire vs water", battle2, "lose")


# ============================================================
# Section 8: Expert — one compound guard
# ============================================================

print()
print("Section 8: Expert — robot guard")
print("===============================")

# You may pass if:
# - the alarm is NOT tripped, AND
# - the password is correct, AND
# - either it is visiting hours OR the captain gave an override

password_ok = True
alarm_tripped = False
is_visiting_hours = False
captain_override = True

if alarm_tripped == False and password_ok == True and is_visiting_hours == True or captain_override == True:
    guard_result = "enter the lab"
else:
    guard_result = "halt"

check("8.1 Robot guard (not, and, or together)", guard_result, "enter the lab")


print()
print("Reflection Questions")
print("====================")
print("1. Which problem had the trickiest boundaries (>, >=, or ranges)?")
print("2. Why does Python check if / elif conditions from top to bottom?")
print("3. How is (A and (B or C)) different from ((A and B) or C)? Give an example.")
print("4. Why might not (A or B) be easier to read than (not A and not B)?")
print("5. In 6.2, what would happen if you checked “login successful” before “banned”?")
