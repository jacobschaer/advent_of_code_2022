# A = X = Rock = 0
# B = Y = Paper = 1
# C = Scissors = 2


# Rock (0) bests Scissors (2)
# Paper (1) beats Rock (0)
# Scissors (2) beats Paper (1)

beats = (2, 0, 1)

def score_round(opponent, player):
	score = player + 1

	if player == opponent:
		score += 3
	elif beats[player] == opponent:
		score += 6
	return score

# Pt 1
# score = 0
# with open('input.txt') as input_file:
# 	for line in input_file:
# 		opponent, player = line.split(' ')
# 		opponent = ord(opponent.strip()) - ord('A')
# 		player = ord(player.strip()) - ord('X')
# 		score += score_round(opponent, player)

# # Pt 2
score = 0
with open('input.txt') as input_file:
	for line in input_file:
		opponent, win_lose_draw = line.split(' ')
		opponent = ord(opponent.strip()) - ord('A')
		win_lose_draw = ord(win_lose_draw.strip()) - ord('X')
		player = opponent

		if win_lose_draw == 0:
			# Lose
			player = beats[opponent]

		elif win_lose_draw == 1:
			# Draw
			pass

		else:
			# Lose
			for _ in range(2):
				player = (player + 1) % 3
				if beats[player] == opponent:
					break


		score += score_round(opponent, player)
		#print(score)
	print(score)