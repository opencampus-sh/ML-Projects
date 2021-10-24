import numpy as np
import scipy.sparse
from scipy.sparse import csr_matrix

def read_moves_from_match(filename):
	f = open(filename, "r")
	formular = f.read()

	# we want to seperate this into individual moves by searching for gaps " ".
	gap_list = []
	for k in range(len(formular)):
		if (formular[k] == ' '):
			gap_list.append(k)

	# Now we can create the moves:
	move_list = []
	mini_count = 0
	for k in range(len(gap_list) - 1):
		# introduce a mini count that removes the "2." , "3." and so on move.
		if (mini_count == 2):
			mini_count = 0
			continue
		move_list.append(formular[gap_list[k] + 1:gap_list[k + 1]])
		mini_count = mini_count + 1

	return move_list


# First we implement the initialisation of a chess board.
# We use a 8 x 8 x 12 tensor with 12 as a 1-hot vector with only looking at the last component:
# a[0] = 1 => King is there, 
#a[1]=Queen
#a[2] = Rook (Turm),
#a[3] = bishop (Läufer),
# a[4] = knight, 
#a[5] = pawn each of them for white and black is a[6] to a[11]
# a[6] = king, 
#a[7]= queen, 
#a[8]=rook, 
#a[9]=bishop, 
#a[10] = knight, 
#a[11] = pawn

def initialise_chess_board():
	# returns the initialisation of the checkerboard
	x = np.zeros((8,8,12))
	#field a1=x[0,0] until a8=x[0,7] and h1=x[7,0] and h8=x[7,7]
	
	# setting the pawns
	for k in range(0,8):
		x[k,1,5] = 1.0
		x[k,6,11] = 1.0
		
	# setting the white rooks
	x[0,0,2] = 1.0
	x[7,0,2] = 1.0
	# setting the black rooks
	x[0,7,8] = 1.0
	x[7,7,8] = 1.0
	
	# setting the knights
	x[1,0,4] = 1.0
	x[6,0,4] = 1.0
	x[1,7,10] = 1.0
	x[6,7,10] = 1.0
	
	# setting the bishops
	x[2,0,3] = 1.0
	x[5,0,3] = 1.0
	x[2,7,9] = 1.0
	x[5,7,9] = 1.0
	
	# setting the queens
	x[3,0,1] = 1.0
	x[3,7,7] = 1.0
	
	# setting the kings
	x[4,0,0] = 1.0
	x[4,7,6] = 1.0
	
	return x 

def figure_sort(n):
	# get input n and return string with colour w or b for white or black
	# and figure sort with K=king, Q=queen, R=rook, B=bishop, N=knight,
	# for pawn only the colour is returned
	if(n==0):
		return "wK"
	if(n==1):
		return "wQ"
	if(n==2):
		return "wR"
	if(n==3):
		return "wB"
	if(n==4):
		return "wN"
	if(n==5):
		return "Pw"
	if(n==6):
		return "bK"
	if(n==7):
		return "bQ"
	if(n==8):
		return "bR"
	if(n==9):
		return "bB"
	if(n==10):
		return "bN"
	if(n==11):
		return "Pb"
	if(n==100):
		return "OO"
def visualise_checkerboard(x):
	# We implement a "visualisation" from shape (8,8,12) to (8,8) with saying,
	# which figure is at which position. That visualisatio is rotated by 90 degrees.
	fs = figure_sort
	# save figures of one row
	fig_row = np.zeros((8,1))+100
	for k in range(0,8):
		fig_row[:,:] = 100 # initialise to empty value again.
		for i in range(0,8):
			for j in range(0,12):
				if(x[k,i,j] == 1):
					fig_row[i,0] = j
		print(fs(fig_row[0,0]), fs(fig_row[1,0]), fs(fig_row[2,0]), fs(fig_row[3,0]),
		fs(fig_row[4,0]), fs(fig_row[5,0]),fs(fig_row[6,0]),fs(fig_row[7,0])) 
	

# Now we impelement the move function with get as input an array and the game and performs a move
def move(x,s,number):
	# We first need to know the length of the string
	# number is the number of the move
	# we transform it into 0=white and 1=black
	number = number % 2
	# puts the string into it chars
	chars = list(s)
	n = len(chars)

	transform= False
	for k in range (0,n):
		if(chars[k] == '='):
			transform = True
	# Initialise the special moves short and long rochade
	if(s=='O-O' or s=='O-O+' or s=='O-O#'):
		if(number == 0):
			x[4,0,0] = 0
			x[6,0,0] = 1
			x[7,0,2] = 0
			x[5,0,2] = 1
		if(number == 1):
			x[4,7,6] = 0
			x[6,7,6] = 1
			x[7,7,8] = 0
			x[5,7,8] = 1
	elif(s=='O-O-O' or s=='O-O-O+' or s=='O-O-O#'):
		if(number == 0):
			x[4,0,0] = 0
			x[2,0,0] = 1
			x[0,0,2] = 0
			x[3,0,2] = 1
		if(number == 1):
			x[4,7,6] = 0
			x[2,7,6] = 1
			x[0,7,8] = 0
			x[3,7,8] = 1
	elif(transform==True):
			# we transform a pawn into another figure
			if(len(chars)<6):
				if(number==0): # whites move
					x[x_coordinate(chars[0]),y_coordinate(chars[1])-1,5] = 0
					x[x_coordinate(chars[0]),y_coordinate(chars[1]),which_figure(chars[3],number)] = 1
				else:
					x[x_coordinate(chars[0]),y_coordinate(chars[1])+1,11] = 0
					x[x_coordinate(chars[0]),y_coordinate(chars[1]),which_figure(chars[3],number)] = 1#
			else:
				x[x_coordinate(chars[2]), y_coordinate(chars[3]), :] = 0 # white or black moves and removes a figure
				x[x_coordinate(chars[2]),y_coordinate(chars[3]),which_figure(chars[5],number)] = 1
				if(number==0): #white moves and removes a figure
					x[x_coordinate(chars[0]),7,5] = 0
				else: #black moves
					x[x_coordinate(chars[0]),1,11] = 0
	# If we do not do rochade, we do a more normal move
	else:
	# We do not need the chess or checkmate sign
		if(chars[n-1]=="+"):
			n = n - 1
		if(chars[n-1]=="#"):
			n = n - 1
		# After removing that possible sign the last sign from that n is the y coordinate
		y_cord = y_coordinate(chars[n-1])
		# For the x coordinate we need the second last argument
		x_cord = x_coordinate(chars[n-2])

		# Now as we have the coordinate we have to figure out, which figure was moved
		# That is the first char.
	
		fig_num = which_figure(chars[0],number)
		# We want to remove the old position before we set the new one to reduce the positions we looked at for removing the old position.
		x = remove_old_position(x,chars,n,number,x_cord,y_cord,fig_num)
		# Setting the figure
		x[x_cord,y_cord,:] = 0 # We first remove old figures from that position
		x[x_cord,y_cord,fig_num] = 1 # Set the new figure

	return x
	
def remove_old_position(x,chars,n,number,x_cord,y_cord,fig_num):
	# We first want to know where figures are
	y = np.zeros((8,8),dtype=np.int8)
	y = np.sum(x,axis=2)

	# get the number of real candidates
	real_cand = []

	# pawn moving
	if(fig_num ==5):
		if(n==2): # not removing another key
		# we go moves in negative y direction
			y_new = y_cord - 1
			while(y[x_cord,y_new] == 0):
				y_new = y_new - 1
			x[x_cord,y_new,fig_num] = 0
		else:
			# we removed another key. Hence there are only two possible positions where the pawn could come from
			# we get the candidates function
			cand = []
			if(x_cord>0 and y_cord>0):
				if(x[x_cord-1,y_cord-1,5]==1):
					cand.append([x_cord-1,y_cord-1])
			if(x_cord<7 and y_cord>0):
				if(x[x_cord+1,y_cord-1,5]==1):
					cand.append([x_cord+1,y_cord-1])
			if(len(cand)==1):
				test = cand[0]
				x[test[0],test[1],5] = 0
			# We want to control the case, that we remove a key with en passant
			if(np.sum(x[x_cord,y_cord,:])==0): # there was no figure at this position
				# Then we remove the figure with x_cord-1
				x[x_cord,y_cord-1,11] = 0
			else: # then in the game formular is the exact old position written.
				x[x_coordinate(chars[0]),y_cord-1,5] = 0
	if(fig_num ==11):
		if(n==2):
			y_new = y_cord + 1
			while(y[x_cord,y_new] == 0):
				y_new = y_new + 1
			x[x_cord,y_new,fig_num] = 0
		else:
			cand = []
			if(x_cord > 0):
				if(x[x_cord-1,y_cord+1,11]==1):
					cand.append([x_cord-1,y_cord+1])
			if(x_cord < 7):
				if(x[x_cord+1,y_cord+1,11]==1):
					cand.append([x_cord+1,y_cord+1])
			if(len(cand)==1):
				test = cand[0]
				x[test[0],test[1],11] = 0
			# We want to control the case, that we remove a key with en passant
			if (np.sum(x[x_cord, y_cord, :]) == 0):  # there was no figure at this position
				# Then we remove the figure with x_cord+1
				x[x_cord, y_cord+1, 5] = 0
			else: # then in the game formular is the exact old position written.
				x[x_coordinate(chars[0]),y_cord+1,11] = 0
	# if n==3 we have only one possible move, if n==4 there are two or more possible moves to that position. 
	# (three or four possible moves should be handled by notation.)
	
	# King is unique and makes it easy
	if(fig_num == 0 or fig_num==6):
		x[:,:,fig_num] = 0
		x[x_cord,y_cord,fig_num] = 1
		
	# Looking for the white or black knight
	if(fig_num == 4 or fig_num==10):
		#unique case
		# First we get the candidates
		#cand = np.where(x[:,:,4]==1)
		#print('last move')
		cand = candidates(x,x_cord,y_cord,fig_num)
		# create the real candidates
		real_cand = []
		for test in cand:
			if(test[0] != x_cord and test[1] != y_cord):
				if(abs(x_cord-test[0])+abs(y_cord-test[1])==3):
					real_cand.append(test)
		if(len(real_cand)==1):
			x[real_cand[0][0],real_cand[0][1],fig_num] = 0
				## Still to implement, if there are two possibilities


	# Looking for the white or black bishop
	if(fig_num == 3 or fig_num==9):
		# we first want to get all bishops available
		cand = candidates(x,x_cord,y_cord,fig_num)
		# create the real candidates
		real_cand = []
		for test in cand:
			if(abs(test[0]-x_cord)==abs(test[1]-y_cord)): # that is a necessary condition for a bishop
				nothing_between = True
				# get the direction of the move
				dir_x = int((x_cord-test[0])/(abs(test[0]-x_cord)))
				dir_y = int((y_cord-test[1])/(abs(test[1]-y_cord)))
				for k in range(1,abs(x_cord-test[0])):
					if(y[x_cord-k*dir_x,y_cord-k*dir_y]==1):
						nothing_between= False
				if(nothing_between==True):
					real_cand.append(test)
		if(len(real_cand)==1):
			x[real_cand[0][0],real_cand[0][1],fig_num] = 0
			## Stil to implement, if there are two possibilities
	# Looking for the white or black rook
	if(fig_num == 2 or fig_num==8):

		cand = candidates(x,x_cord,y_cord,fig_num)

		real_cand = []
		for test in cand:
			if(x_cord == test[0] or y_cord == test[1]):
				nothing_between = True
				if(x_cord != test[0]):
					dir_x = int((x_cord-test[0])/(abs(test[0]-x_cord)))
					dir_y = 0
					for k in range(1,abs(x_cord-test[0])):
						if(y[x_cord-k*dir_x,y_cord-k*dir_y]==1):
							nothing_between= False
				else:
					dir_y = int((y_cord-test[1])/(abs(test[1]-y_cord)))
					dir_x = 0
					for k in range(1,abs(y_cord-test[1])):
						if(y[x_cord-k*dir_x,y_cord-k*dir_y]==1):
							nothing_between= False
				if(nothing_between==True):
					real_cand.append(test)
		if(len(real_cand)==1):
			x[real_cand[0][0],real_cand[0][1],fig_num]=0
			##  Stil to implement, if there are two possibilities

	# Looking for the white or black queen
	if(fig_num == 1 or fig_num == 7):
		cand = candidates(x,x_cord,y_cord,fig_num)
		real_cand = []
		for test in cand:

			# We test rook moves
			if(x_cord == test[0] or y_cord == test[1]):
				nothing_between = True
				if(x_cord != test[0]):
					dir_x = int((x_cord-test[0])/(abs(test[0]-x_cord)))
					dir_y = 0
					for k in range(1,abs(x_cord - test[0])):
						if (y[x_cord - k * dir_x, y_cord] == 1):
							nothing_between = False
					if(nothing_between==True):
						real_cand.append(test)
				else:
					dir_y = int((y_cord-test[1])/(abs(test[1]-y_cord)))
					dir_x = 0
					for k in range(1,abs(y_cord-test[1])-1):
						if(y[x_cord,y_cord-k*dir_y]==1):
							nothing_between= False
							break
					if(nothing_between==True):
						real_cand.append(test)
			if (abs(test[0] - x_cord) == abs(test[1] - y_cord)):  # that is a necessary condition for a bishop
				nothing_between = True
				# get the direction of the move
				dir_x = int((x_cord - test[0]) / (abs(test[0] - x_cord)))
				dir_y = int((y_cord - test[1]) / (abs(test[1] - y_cord)))
				for k in range(1,abs(x_cord - test[0])):
					if (y[x_cord - k * dir_x, y_cord - k * dir_y] == 1):
						nothing_between = False
				if (nothing_between == True):
					real_cand.append(test)
			if(len(real_cand)==1):
				x[real_cand[0][0], real_cand[0][1], fig_num] = 0

		# we now implement something to get only the one real candidat
		# it means that the seond entry in chars is either the line or column where the figure comes from
	if(len(real_cand)>1):
		#print('the two case scenario')
		x_known, y_known = get_old(chars)
		if(x_known==True):
			#print('case 1')
			# We now the x_coordinate of the real moved figure.
			for test in real_cand:
				if(test[0] == x_coordinate(chars[1])):
					x[test[0],test[1],fig_num]=0
		if(y_known==True):
			for test in real_cand:
				print('test')
				print(test)
				print('move')
				print(chars)
				if(chars[1]=='x'):
					if(test[1]==y_coordinate(chars[3])):
						y[test[0],test[1],fig_num]=0
				elif(test[1]==y_coordinate(chars[1])):
					x[test[0],test[1],fig_num]=0

	# The following situation is not handled:
	# First one thinks, that two figures could move to one position.
	# But at second glance one of the figures can not move, as it is bounded, because of the king.

	return x

def get_old(chars):
	# returns if the second char is a,b,c..., = x_known or 1,2,3,... = y_known
	x_known = False
	y_known = False
	# relevant notation
	v = chars[1]
	if('a'==v or 'b'==v or 'c'==v or 'd'==v or 'e'==v or 'f'==v or 'g'==v or 'h'==v):
		x_known = True
	else:
		y_known = True

	return x_known,y_known

def candidates(x,x_cord,y_cord,fig_num):
	# returns the candidates where the figure could come from dependend on the board
	# if len(cand)=1, we only have one possible move
	# That is only useful, if we do not move pawns or the king, because they are often on the board
	# and somehow individual or as the king unique
	cand = []
	for i in range(0,8):
		for j in range(0,8):
			if(x[i,j,fig_num] == 1):
				cand.append([i,j])
	return cand
	
def which_figure(s,number):
	if(number ==0):
		number = 0
	else:
		number = 6
	if(s=='K'):
		return number+0
	if(s=='Q'):
		return number+1
	if(s=='R'):
		return number+2
	if(s=='B'):
		return number+3
	if(s=='N'):
		return number+4
	else:
		return number+5

def y_coordinate(s):
	# we need to define a function that returns the numbers of the coordinate
	return int(s)-1

def x_coordinate(s):
	# the x-component of the coordinate (a,b,c,d,e,f,g,h)
	if(s=='a'):
		return 0
	if(s=='b'):
		return 1
	if(s=='c'):
		return 2
	if(s=='d'):
		return 3
	if(s=='e'):
		return 4
	if(s=='f'):
		return 5
	if(s=='g'):
		return 6
	if(s=='h'):
		return 7
# We test initialisation of the checkerboard
x = initialise_chess_board()
visualise_checkerboard(x)
print("\n")

# As mentioned at return of remove_old_position, there is still at least one error in implementation.
# For that we will test a necessary condition. If that necesaary condition is not fulfilled,
# the game will not be saved for the deep neural network.
error_count = 0

# Testing the move
def import_game(filename):
	global error_count
	move_list = read_moves_from_match(filename)
	x = initialise_chess_board()
	# We implement a test: The number of figures should not increase
	game_move_number_list = np.zeros((8,8,12,min(19,len(move_list))))
	game_move_number_list[:,:,:,0] = x
	num_fig_old = np.sum(x)
	# We just want to have the first 20 moves for our classificaiton program
	for k in range(0,min(19,len(move_list))):
		x = move(x,move_list[k],k)
		game_move_number_list[:,:,:,k] = x
		num_fig = np.sum(x)
		if(num_fig_old<num_fig or num_fig+1<num_fig_old):
			error_count = error_count + 1
			print('error')
		num_fig_old = num_fig
	return game_move_number_list


# we use number of games with n
n = 5000
# Initialise the game moves in the specified notation.
game_move_number_list = np.zeros((8,8,12,19,n))
# We also need the used results, as we do not take all games, for example if there are errors.
results = np.zeros((n,1))
f = open('results.txt')
results_from_file = f.read()
# Testing the results
#print('test')
#print(results_from_file[1:200])
#print(results_from_file[2:5],results_from_file[9:12],results_from_file[16:19],results_from_file[23:26])
count = 0
for k in range(1,n):
	# Games that are analysed can not be used, as the program crashes with it.
	if(k==200 or k==766 or k==776 or k==811 or k==821 or k==830 or k==999 or k==1000
	or k==1135 or k==1152 or k==1370 or k==1397 or k==1415 or k==1442 or k==1532
	or k==1604 or k==2098 or k==2404 or k==2432 or k==2489 or k==2807 or k==2837
	or k==3107 or k==3682 or k==3745 or k==3772 or k==4150 or k==4182 or k==4253
	or k==4329 or k==4491 or k==4511 or k==4562 or k==4643 or k==4647 or k==4711
	or k==4723 or k==4968):
		continue
	print('gamee',k)
	temp = error_count
	game_move_number_list_temp = import_game('games/games'+str(k)+'.txt')
	# we only take games with 20 moves.
	if(len(game_move_number_list_temp[0,0,0,:])==19):
		if(temp==error_count):
			game_move_number_list[:,:,:,:,count] = game_move_number_list_temp
			count = count + 1
			if(k==1):
				results[count,0] = results_from_file[2:5]
			else:
				print('count',count)
				results[count,0] = results_from_file[(k-1)*7+2:k*7-2]
				print(float(results_from_file[(k-1)*7+2:k*7-2]))

# Before we save the data to file we want to compress them into (8,8,number_of_moves,number_of,games) format
# That is helpful, if we want to upload it to google Colaboratory as it reduces the size of the file by factor 1/12.
def chess_matrix_compress(A):
	shapiness = np.shape(A)
	print('shapiness')
	print(shapiness[0],shapiness[1],shapiness[3],shapiness[4])
	results = np.zeros((shapiness[0],shapiness[1],shapiness[3],shapiness[4]))
	# We just look at the tensors of form [:,:,k,:,:] and sum them up,
	# using that the tensor has only 1 or 0 as values.
	for k in range(0,12):
		results = results + k * A[:,:,k,:,:]
	return results

# The uncompress is for control and will be used in the jupyter notebook
def chess_matrix_decompress(A):
	shapiness = np.shape(A)
	results = np.zeros((shapiness[0],shapiness[1],12,shapiness[2],shapiness[3]))
	for k in range(0,12):
		positions = np.argwhere(A==k)
		for pos in positions:
			results[pos[0],pos[1],k,pos[2],pos[3]] = 1.0

	return results


compressed = chess_matrix_compress(game_move_number_list)

np.save('game_in_numbers_compressed.txt',compressed)
f = open('game_in_numbers_compressed.txt',"w")
np.save('results_in_numbers.txt',results)



# Testing the compressed and uncompressed. Is only as comment, as it was only for testing,
# but could be helpful for trying with it.
#compressed = chess_matrix_compress(game_move_number_list)
#print('new shape')
#print(np.shape(compressed))
#uncompressed = chess_matrix_decompress(compressed)
#print('compare compressed and not compressed')
#print(np.amax(game_move_number_list-uncompressed))

