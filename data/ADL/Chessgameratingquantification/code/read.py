# We want to read a part formular starting with '1.'
def read_moves_from_match(filename):
	f = open(filename,"r")
	formular = f.read()


	# we want to seperate this into individual moves by searching for gaps " ".
	gap_list =[]
	for k in range(len(formular)):
		if(formular[k] == ' '):
			gap_list.append(k)
		
	# Now we can create the moves:
	move_list = []
	mini_count = 0
	for k in range(len(gap_list)-1):
		# introduce a mini count that removes the "2." , "3." and so on move.
		if(mini_count == 2):
			mini_count = 0
			continue
		move_list.append(formular[gap_list[k]+1:gap_list[k+1]])
		mini_count = mini_count + 1
	
	return move_list

def seperate_into_x_and_y(filename):
	f = open(filename,"r")
	formular = f.read()
	print('formular')
	# Find the WhiteElo
	elo_list = []
	game_list = []
	result_list = []
	for k in range(3,len(formular)-16):
		if(formular[k:k+8]=='WhiteElo' or formular[k:k+8]=='BlackElo'):
			# get length of the list
			for j in range(4, 7):
				if (formular[k + 8 + j] == '"'):
					elo_list.append(int(formular[k+10:k+8+j])*1.0)
		# we also want to create the game list
		if(formular[k:k+3]=='1. ' and formular[k-3]==']'):
			for j in range(2,len(formular)-k):
				if(formular[k+j:k+j+7]=='1/2-1/2' or formular[k+j:k+j+3]=='1-0' or formular[k+j:k+j+3]=='0-1'):
					game_list.append([formular[k:k+j]])
					# We directly transform the result into the points a player gets for the game:
					# We use a string with 3 chars, to get parts of it later more easily
					if(formular[k+j:k+j+7]=='1/2-1/2'):
						result_list.append('0.5')
					if(formular[k+j:k+j+3]=='1-0'):
						result_list.append('1.0')
					if(formular[k+j:k+j+3]=='0-1'):
						result_list.append('0.0')
					break
	return game_list,elo_list,result_list

games, elos, results = seperate_into_x_and_y('lichess_db_standard_rated_2013-01.txt')

# we only want to get one game. That is with comments,
# because it takes a lot time do execute it.
# Hence only do it once.
# Results was the part, which output structure got changed later.
#for k in range(len(games)):
#	f = open('games/games'+str(k)+'.txt',"w")
#	f.write(str(games[k]))
#	f.close()
g = open('results.txt',"w")
g.write(str(results))
g.close()
# Here we write the results, but only once, as it takes some time.
#h = open('elos.txt',"w")
#h.write(str(elos))
#h.close

# Here we execute the function
move_list = read_moves_from_match('games.txt')
# We print to the terminal all moves (from all matches)
print('move_list')
print(move_list)