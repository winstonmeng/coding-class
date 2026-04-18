import random

MAX_PER_TURN = 3
LOSING_TARGET = 31
SAFE_RESIDUE = (LOSING_TARGET - 1) % (MAX_PER_TURN + 1)  # 2 for 31 game with 1-3 numbers


def compute_ai_move(current_total: int) -> list[int]:
	"""
	Return the sequence of numbers the AI will say this turn.
	AI plays optimally to force the opponent to eventually say LOSING_TARGET when possible.
	"""
	# Next target that is congruent to SAFE_RESIDUE mod (MAX_PER_TURN+1)
	next_target = None
	for step in range(1, MAX_PER_TURN + 1):
		candidate = current_total + step
		if candidate % (MAX_PER_TURN + 1) == SAFE_RESIDUE and candidate < LOSING_TARGET:
			next_target = candidate
			break

	# If we can move to the next safe target, do so; else pick minimal safe-ish move
	if next_target is not None:
		end_number = next_target
	else:
		# If we're already on a safe number (rare if opponent plays well),
		# no move can keep us on safe; choose 1 to minimize advantage given.
		end_number = min(current_total + 1, LOSING_TARGET)

	return list(range(current_total + 1, end_number + 1))


def explain_winning_method() -> str:
	"""
	Explain the deterministic method to always win when you play first when possible.
	"""
	targets = [n for n in range(SAFE_RESIDUE, LOSING_TARGET, (MAX_PER_TURN + 1)) if n > 0]
	if SAFE_RESIDUE == 0:
		return (
			"Winning method (general):\n"
			f"- Safe numbers are multiples of {MAX_PER_TURN + 1}.\n"
			"- Because the first safe number is 0, the SECOND player has the inherent advantage if both play optimally.\n"
			f"- If your opponent ever misses a safe number, jump to the next multiple of {MAX_PER_TURN + 1} to take control.\n"
		)

	start_seq = " ".join(str(n) for n in range(1, SAFE_RESIDUE + 1))
	return (
		"Winning method (when you go first):\n"
		f"- Aim to finish your turns on these numbers: {targets}.\n"
		f"- Start by saying: {start_seq} (so the total is {SAFE_RESIDUE}).\n"
		f"- Whatever your opponent says (1 to {MAX_PER_TURN} numbers), say enough numbers to land on the next target.\n"
		f"- If you maintain this, you'll end on {targets[-1] if targets else LOSING_TARGET - 1}, forcing the opponent to say {LOSING_TARGET} and lose.\n"
	)


def read_human_move(current_total: int) -> list[int]:
	"""
	Read and validate the human's move as a sequence of 1 to MAX_PER_TURN consecutive numbers.
	"""
	while True:
		user_input = input(f"Your turn - enter 1 to {MAX_PER_TURN} numbers separated by spaces: ").strip()
		parts = user_input.split()
		if not (1 <= len(parts) <= MAX_PER_TURN):
			print(f"Please enter between 1 and {MAX_PER_TURN} numbers.")
			continue
		try:
			nums = [int(p) for p in parts]
		except ValueError:
			print("Please enter integers only.")
			continue

		# Validate they are consecutive and start from current_total+1
		expected = list(range(current_total + 1, current_total + 1 + len(nums)))
		if nums != expected:
			print(f"Numbers must be consecutive starting from {current_total + 1}: {' '.join(map(str, expected))}")
			continue

		# Validate they don't go beyond LOSING_TARGET (saying LOSING_TARGET loses immediately)
		if nums[-1] > LOSING_TARGET:
			print(f"You cannot go beyond {LOSING_TARGET}.")
			continue

		return nums


def play_game():
	print("31 Counting Game (say 31 and you lose)")
	print("- Each turn, say 1 to 3 consecutive numbers.")
	print("- Whoever says 31 loses.")
	print()
	print(explain_winning_method())

	# Choose who goes first
	while True:
		first = input("Do you want to go first? (y/n): ").strip().lower()
		if first in ("y", "n"): break
		print("Please enter 'y' or 'n'.")

	current_total = 0
	human_turn = (first == "y")

	while True:
		if human_turn:
			human_move = read_human_move(current_total)
			print(f"You said: {' '.join(map(str, human_move))}")
			current_total = human_move[-1]
			if current_total == LOSING_TARGET:
				print(f"You said {LOSING_TARGET}. You lose. AI wins!")
				break
			# Switch turn
			human_turn = False
		else:
			ai_move = compute_ai_move(current_total)
			# If compute_ai_move returns empty (shouldn't), fall back to minimal move 1 number
			if not ai_move:
				ai_move = [current_total + 1]
			print(f"AI says: {' '.join(map(str, ai_move))}")
			current_total = ai_move[-1]
			if current_total == LOSING_TARGET:
				print(f"AI said {LOSING_TARGET}. AI loses. You win!")
				break
			# Switch turn
			human_turn = True


if __name__ == "__main__":
	play_game()
