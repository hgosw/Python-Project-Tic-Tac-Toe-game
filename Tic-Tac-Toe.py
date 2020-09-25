from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print("-|-|-")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("-|-|-")
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1 choose (X or O): ').upper()
    player1= marker 
    if player1 =='X':
        player2='O'
    else:
        player2 = 'X'
    return (player1,player2)



def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    
    if board[7]== mark and board[8]== mark and board[9] == mark:
        return 'win!'
    if board[1]== mark and board[5]== mark and board[9] == mark:
        return 'win!'
    if board[4]== mark and board[5]== mark and board[6] == mark:
        return 'win!'
    if board[1]== mark and board[2]== mark and board[3] == mark:
        return 'win!'
    if board[1]== mark and board[4]== mark and board[7] == mark:
        return 'win!'
    if board[2]== mark and board[5]== mark and board[8] == mark:
        return 'win!'
    if board[3]== mark and board[6]== mark and board[9] == mark:
        return 'win!'
    if board[3]== mark and board[5]== mark and board[7] == mark:
        return 'win!'
    else:
        return False 

import random

def choose_first():
    ran= random.randint(1,2)
    if ran ==1:
        a = 'player1 '
    elif ran == 2 :
        a='player2 '
    return a+'will go first'


def space_check(board, position):
        return board[position]==' '

def full_board_check(board):
    a= True
    for n in range(1,10):
        if board[n] ==' ' :
            a= False
    return a
            
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
            try:
                position = int(input('Choose your next position: (1-9) '))
            except ValueError :
                    print('please Enter a Number! ')
                    position = int(input('Choose your next position: (1-9) '))
        
    
    return position

    
def replay():
    q='yes'
    while q != 'yes' or q != 'no':
        q = input('Do you want to play again? Enter Yes or No: ')
        q= q.lower()
        if q=='yes':
            return True 
        if q == 'no':
            return False 
        else:
            print('Please enter Yes or No')

print('Welcome to Tic Tac Toe!')
k=True 

while k!= False:
   

    
    m=[' ']*10
    g=''
    q = False
    player_1 , player_2 =player_input()
    display_board(m)
    first_choise = choose_first()
    print (first_choise)
   
    while q!= True:
        
        if first_choise == 'player1 will go first':
            choise= player_choice(m)
            place_marker(m,player_1,choise)
            display_board(m)
            g = win_check(m,player_1)
            if g== 'win!':
                print ('congratulations! player 1 "'+ player_1+'" you have won the game!')
                k=replay()
                break
            if full_board_check(m) == True:
                print('Tie Game!')
                k=replay()
                break

            first_choise = 'player2 will go first'
       
        if first_choise == 'player2 will go first':
            choise= player_choice(m)
            place_marker(m,player_2,choise)
            display_board(m)
            g = win_check(m,player_2)
            if g== 'win!':
                print ('congratulations! player 2 "'+player_2+'" you have won the game!')
                k=replay()
                break
            if full_board_check(m) == True:
                print('Tie Game!')
                k=replay()
                break
          
            first_choise= 'player1 will go first'
