# Checkers V2
import os
os.system("")

RESET = "\033[0m"
RED = "\033[0;31m"
BLUE = "\033[0;34m"
YELLOW = "\033[0;33m"
GREEN = "\033[32m"

class Checkers_Piece:
    def __init__(self, color):
        self.color = color
        self.king = False
    def __str__(self):
            if self.king == True and self.color == 'red':
                return RED + '♛' + RESET
            elif self.king == True and self.color == 'blue':
                return BLUE + '♛' + RESET
            elif self.king == False and self.color == 'red':
                return RED + '0' + RESET
            elif self.king == False and self.color == 'blue':
                return BLUE + '0' + RESET
            
class Checkers_Board:
    def __init__(self):
        self.board = []
        self.current_player = { 'color': 'blue' }
        self.blue_score = 0
        self.red_score = 0
        self.game_over = False

    def make_board(self):
        self.board = [[None] * 9 for _ in range(9)]
        # iterate over the board
        for row in range(1, 4):
            for col in range(1, 9):
                if (row + col) % 2 != 0:
                    self.board[row][col] = Checkers_Piece('red')
        for row in range(6, 9):
            for col in range(1, 9):
                if (row + col) % 2 != 0:
                    self.board[row][col] = Checkers_Piece('blue')

    def print_board(self):
        for row in range(9):
            for col in range(9):
                if row == 0:
                    print(col, end=' ')
                    continue
                if row != 0 and col == 0:
                    print(row, end= ' ')
                    continue
                if self.board[row][col] is not None:
                    print(self.board[row][col], end=' ')
                else:
                    print('.', end=' ')
            print('')

    def change_player(self):
        if self.current_player['color'] == 'red':
            self.current_player['color']  = 'blue'
        else:
            self.current_player['color']  = 'red'

    def create_king(self):
        for i, piece in enumerate(self.board[1]):
             if piece is not None:
                if piece.color == 'blue' and piece.king == False:
                    self.board[1][i].king = True

        for i, piece in enumerate(self.board[8]):
             if piece is not None:
                if piece.color == 'red' and piece.king == False:
                    self.board[8][i].king = True

class Move:
    def __init__(self, board, current_player):
        self.board = board
        self.current_player = current_player

    def is_jump_valid(self, starting_space, ending_space, player_color):
        
        enemy_piece_is_king = False
        if player_color == 'red':
            opponent_color = 'blue'
        if player_color == 'blue':
            opponent_color = 'red'

        # X's and A's are plugged into LEFT movement
        # Y's and B's are plugged into RIGHT movement
        if player_color == 'red':
            a1 = 1
            a2 = -1
            b1 = 1
            b2 = 1
            x1 = -2 
            x2 = 2  
            y1 = -2 
            y2 = -2 

        else: # BLUE
            a1 = -1
            a2 = -1
            b1 = -1
            b2 = 1
            x1 = 2 
            x2 = 2
            y1 = 2
            y2 = -2
            
        # DOWN / LEFT or UP / LEFT
        if starting_space[0] - ending_space[0] == x1 and starting_space[1] - ending_space[1] == x2:
            if self.board[starting_space[0] + a1][starting_space[1] + a2] is not None:
                if self.board[starting_space[0] + a1][starting_space[1] + a2].color == opponent_color:
                    # Jump is valid
                    self.board[starting_space[0]][starting_space[1]] = None
                    if self.board[starting_space[0] + a1][starting_space[1] + a2].king == True:
                        enemy_piece_is_king = True  
                    self.board[starting_space[0] + a1][starting_space[1] + a2] = None
                    self.board[ending_space[0]][ending_space[1]] = Checkers_Piece(player_color)                 
                    if enemy_piece_is_king == True:
                        self.board[ending_space[0]][ending_space[1]].king = True
                        starting_space = ending_space
                        self.king_double_jump_check(starting_space, player_color)
                        return True                   
                    starting_space = ending_space
                    self.double_jump_check(starting_space, player_color)
                    return True
                else:
                    # Jump is invalid. Return False
                    return False
        # DOWN / RIGHT or UP / RIGHT     
        elif starting_space[0] - ending_space[0] == y1 and starting_space[1] - ending_space[1] == y2: 
            if self.board[starting_space[0] + b1][starting_space[1] + b2] is not None:
                if self.board[starting_space[0] + b1][starting_space[1] + b2].color == opponent_color:
                    # Jump is valid
                    self.board[starting_space[0]][starting_space[1]] = None
                    if self.board[starting_space[0] + b1][starting_space[1] + b2].king == True: 
                        enemy_piece_is_king = True
                    self.board[starting_space[0] + b1][starting_space[1] + b2] = None
                    self.board[ending_space[0]][ending_space[1]] = Checkers_Piece(player_color)
                    if enemy_piece_is_king == True:
                        self.board[ending_space[0]][ending_space[1]].king = True
                        starting_space = ending_space
                        self.king_double_jump_check(starting_space, player_color)
                        return True
                    starting_space = ending_space
                    self.double_jump_check(starting_space, player_color)
                    return True
                else:
                    # Jump is invalid. Return False
                    return False  
        else:
            return False
            
    def king_is_jump_valid(self, starting_space, ending_space, player_color):
        if player_color == 'red':
            opponent_color = 'blue'
        if player_color == 'blue':
            opponent_color = 'red'

        # DOWN / LEFT
        if starting_space[0] - ending_space[0] == -2 and starting_space[1] - ending_space[1] == 2 and self.board[starting_space[0] + 1][starting_space[1] - 1] is not None:
            if self.board[starting_space[0] + 1][starting_space[1] - 1].color == opponent_color:
                # Jump is valid
                self.board[starting_space[0]][starting_space[1]] = None
                self.board[starting_space[0] + 1][starting_space[1] - 1] = None
                self.board[starting_space[0] + 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                self.board[starting_space[0] + 2][starting_space[1] - 2].king = True
                starting_space = ending_space
                board.print_board()
                self.king_double_jump_check(starting_space, player_color)
                return True
            else:
                # Jump is invalid. Return False
                return False
            
        # DOWN / RIGHT
        elif starting_space[0] - ending_space[0] == -2 and starting_space[1] - ending_space[1] == -2 and self.board[starting_space[0] + 1][starting_space[1] + 1] is not None:
            if self.board[starting_space[0] + 1][starting_space[1] + 1].color == opponent_color:
                # Jump is valid
                self.board[starting_space[0]][starting_space[1]] = None
                self.board[starting_space[0] + 1][starting_space[1] + 1] = None
                self.board[starting_space[0] + 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                self.board[starting_space[0] + 2][starting_space[1] + 2].king = True
                starting_space = ending_space
                # new instance of 'Checkers_Board()' so that way we can call a method from another class
                
                board.print_board()
                self.king_double_jump_check(starting_space, player_color)
                return True
            else:
                return False
            
        # UP / LEFT
        elif starting_space[0] - ending_space[0] == 2 and starting_space[1] - ending_space[1] == 2 and self.board[starting_space[0] - 1][starting_space[1] - 1] is not None:
            if self.board[starting_space[0] - 1][starting_space[1] - 1].color == opponent_color:
                # Jump is valid
                self.board[starting_space[0]][starting_space[1]] = None
                self.board[starting_space[0] - 1][starting_space[1] - 1] = None
                self.board[starting_space[0] - 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                self.board[starting_space[0] - 2][starting_space[1] - 2].king = True
                starting_space = ending_space
                board.print_board()
                self.king_double_jump_check(starting_space, player_color)
                return True
            else:
                # Jump is invalid. Return False
                return False
            
        # UP / RIGHT
        elif starting_space[0] - ending_space[0] == 2 and starting_space[1] - ending_space[1] == -2 and self.board[starting_space[0] - 1][starting_space[1] + 1] is not None:
            
            if self.board[starting_space[0] - 1][starting_space[1] + 1].color == opponent_color:
                # Jump is valid
                self.board[starting_space[0]][starting_space[1]] = None
                self.board[starting_space[0] - 1][starting_space[1] + 1] = None
                self.board[starting_space[0] - 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                self.board[starting_space[0] - 2][starting_space[1] + 2].king = True
                starting_space = ending_space
                board.print_board()
                self.king_double_jump_check(starting_space, player_color)
                return True
            else:
                # Jump is invalid. Return False
                return False
        else:
            # No jump found, return False
            return False
           
    def double_jump_check(self, starting_space, player_color):
        
        opponent_color = ''
        if player_color == 'red':
            opponent_color = 'blue'
        if player_color == 'blue':
            opponent_color = 'red'

        valid_jumps = []

        # Helper function to process the 'valid_jumps' elements:
        def process_valid_jumps(valid_jumps, starting_space, player_color):
            
            enemy_piece_is_king = False
            if len(valid_jumps) == 1:
                if player_color == 'red':
                    if valid_jumps[0] == 'down left':
                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] + 1][starting_space[1] - 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] + 1][starting_space[1] - 1] = None
                        self.board[starting_space[0] + 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] + 2][starting_space[1] - 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] + 2, starting_space[1] - 2]
                        self.double_jump_check(starting_space, player_color)
                        return
                    elif valid_jumps[0] == 'down right':
                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] + 1][starting_space[1] + 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] + 1][starting_space[1] + 1] = None
                        self.board[starting_space[0] + 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] + 2][starting_space[1] + 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] + 2, starting_space[1] + 2]
                        self.double_jump_check(starting_space, player_color)
                        return
                    
                elif player_color == 'blue':
                    if valid_jumps[0] == 'up left':
                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] - 1][starting_space[1] - 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] - 1][starting_space[1] - 1] = None
                        self.board[starting_space[0] - 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] - 2][starting_space[1] - 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] - 2, starting_space[1] - 2]                   
                        self.double_jump_check(starting_space, player_color)
                        return
                    elif valid_jumps[0] == 'up right':
                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] - 1][starting_space[1] + 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] - 1][starting_space[1] + 1] = None
                        self.board[starting_space[0] - 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] - 2][starting_space[1] + 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] - 2, starting_space[1] + 2]                   
                        self.double_jump_check(starting_space, player_color)
                        return
                   
            elif len(valid_jumps) > 1:
                valid_input = False
                while valid_input == False:
                    board.print_board()
                    ending_space = input('Enter the direction in which you would like to jump to: ' + str(valid_jumps))
                    # These 2 conditions might be redundant, given the third:
                    if player_color == 'red':
                        if ending_space == 'up left' or ending_space == 'up right':
                            print('ERROR: invalid input!1')
                            continue

                    if player_color == 'blue':
                        if ending_space == 'down left' or ending_space == 'down right':
                            print('ERROR: invalid input!2')
                            continue

                    if ending_space not in valid_jumps:
                        print('ERROR: invalid input!3')
                        continue

                    elif ending_space == 'up left':
                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] - 1][starting_space[1] - 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] - 1][starting_space[1] - 1] = None
                        self.board[starting_space[0] - 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] - 2][starting_space[1] - 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] - 2, starting_space[1] - 2]
                        # if starting space is top or bottom of board, convert piece to king and call 'king_double_jump_check()'
                        if starting_space[0] == 1 or starting_space[0] == 8:
                            board.create_king()
                            board.print_board()  
                            self.king_double_jump_check(starting_space, player_color)
                            return
                        else:          
                            self.double_jump_check(starting_space, player_color)
                            return
                    
                    elif ending_space == 'up right':
                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] - 1][starting_space[1] + 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] - 1][starting_space[1] + 1] = None
                        self.board[starting_space[0] - 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] - 2][starting_space[1] + 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] - 2, starting_space[1] + 2]
                        if starting_space[0] == 1 or starting_space[0] == 8:
                            board.create_king()
                            board.print_board()  
                            self.king_double_jump_check(starting_space, player_color)
                            return
                        else:                   
                            self.double_jump_check(starting_space, player_color)
                            return
                    
                    elif ending_space == 'down left':
                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] + 1][starting_space[1] - 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] + 1][starting_space[1] - 1] = None
                        self.board[starting_space[0] + 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] + 2][starting_space[1] - 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] + 2, starting_space[1] - 2]
                        if starting_space[0] == 1 or starting_space[0] == 8:
                            board.create_king()
                            board.print_board()  
                            self.king_double_jump_check(starting_space, player_color)
                            return
                        else:
                            self.double_jump_check(starting_space, player_color)
                            return
                    
                    elif ending_space == 'down right':
                        print(player_color)
                        print(starting_space)

                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] + 1][starting_space[1] + 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] + 1][starting_space[1] + 1] = None
                        self.board[starting_space[0] + 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] + 2][starting_space[1] + 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] + 2, starting_space[1] + 2]
                        if starting_space[0] == 1 or starting_space[0] == 8:
                            board.create_king()
                            board.print_board()  
                            self.king_double_jump_check(starting_space, player_color)
                            return
                        else:
                            self.double_jump_check(starting_space, player_color)
                            return
            else: # No double jumps found
                return
            
        if player_color == 'red': 
            if starting_space[0] < 7 and starting_space[1] > 2:
                if self.board[starting_space[0] + 1][starting_space[1] - 1] is not None and self.board[starting_space[0] + 1] != 1 and self.board[starting_space[1] - 1] != 8:
                    if self.board[starting_space[0] + 1][starting_space[1] - 1].color == opponent_color and self.board[starting_space[0] + 2][starting_space[1] + 2] == None:
                        valid_jumps.append('down left')
                        print('down left appended')
            
        if starting_space[0] < 7 and starting_space[1] < 7:
            if self.board[starting_space[0] + 1][starting_space[1] + 1] is not None and self.board[starting_space[0] + 1] != 1 and self.board[starting_space[1] + 1] != 8:
                if self.board[starting_space[0] + 1][starting_space[1] + 1].color == opponent_color and self.board[starting_space[0] + 2][starting_space[1] + 2] == None:
                    valid_jumps.append('down right')
                    print('down right appended')
                              
        if player_color == 'blue':
            if starting_space[0] > 2 and starting_space[1] > 2:
                if self.board[starting_space[0] - 1][starting_space[1] - 1] is not None and self.board[starting_space[0] - 1] != 1 and self.board[starting_space[1] - 1] != 8:
                    if self.board[starting_space[0] - 1][starting_space[1] - 1].color == opponent_color and self.board[starting_space[0] - 2][starting_space[1] - 2] == None:
                        valid_jumps.append('up left')
                        print('blue up left debug append test')
                            
        if starting_space[0] > 2 and starting_space[1] < 7:
            if self.board[starting_space[0] - 1][starting_space[1] + 1] is not None and self.board[starting_space[0] - 1] != 1 and self.board[starting_space[1] + 1] != 8:
                if self.board[starting_space[0] - 1][starting_space[1] + 1].color == opponent_color and self.board[starting_space[0] - 2][starting_space[1] + 2] == None:
                    valid_jumps.append('up right')
                    print('blue up right debug append test')
                            
        process_valid_jumps(valid_jumps, starting_space, player_color)             

    def king_double_jump_check(self, starting_space, player_color):
            
            opponent_color = ''
            if player_color == 'red':
                opponent_color = 'blue'
            if player_color == 'blue':
                opponent_color = 'red'
            
            print(starting_space)
            valid_jumps = []
        # Code cycles through all 4 diagonals, and appends the possible jumps to list 'valid_jumps':
            # UP / LEFT check:
            if starting_space[0] > 2 and starting_space[1] > 2:
                if self.board[starting_space[0] - 1][starting_space[1] - 1] is not None and self.board[starting_space[0] - 1][starting_space[1] - 1].color == opponent_color:
                    # Check for opposite color and empty space
                        if self.board[starting_space[0] - 1][starting_space[1] - 1].color == opponent_color and self.board[starting_space[0] - 2][starting_space[1] - 2] == None:
                            valid_jumps.append('up left')
                            print('king up left appended')
                            print(valid_jumps)
            
            # UP / RIGHT check:
            if starting_space[0] > 2 and starting_space[1] < 7:
                if self.board[starting_space[0] - 1][starting_space[1] + 1] is not None and self.board[starting_space[0] - 1][starting_space[1] + 1].color == opponent_color:
                        if self.board[starting_space[0] - 1][starting_space[1] + 1].color == opponent_color and self.board[starting_space[0] - 2][starting_space[1] + 2] == None:
                            valid_jumps.append('up right')
                            print('king up right appended')
                            print(valid_jumps)
            
            # DOWN / RIGHT check:
            if starting_space[0] < 7 and starting_space[1] < 7:
                if self.board[starting_space[0] + 1][starting_space[1] + 1] is not None and self.board[starting_space[0] + 1][starting_space[1] + 1].color == opponent_color:
                    if self.board[starting_space[0] + 1][starting_space[1] + 1].color == opponent_color and self.board[starting_space[0] + 2][starting_space[1] + 2] == None:
                        valid_jumps.append('down right')
                        print('king down right appended')
                        print(valid_jumps)
            
            # DOWN / LEFT check:
            if starting_space[0] < 7 and starting_space[1] > 2:
                if self.board[starting_space[0] + 1][starting_space[1] - 1] is not None and self.board[starting_space[0] + 1][starting_space[1] - 1].color == opponent_color:
                    if self.board[starting_space[0] + 1][starting_space[1] - 1].color == opponent_color and self.board[starting_space[0] + 2][starting_space[1] - 2] == None:
                        valid_jumps.append('down left')
                        print('king down left appended')
                        print(valid_jumps)
            
            # Only one possible jump route. Force it:
            print(valid_jumps)
            if len(valid_jumps) == 1:
                if valid_jumps[0] == 'up left':
                    self.board[starting_space[0]][starting_space[1]] = None
                    self.board[starting_space[0] - 1][starting_space[1] - 1] = None
                    self.board[starting_space[0] - 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                    self.board[starting_space[0] - 2][starting_space[1] - 2].king = True
                    starting_space = [starting_space[0] - 2, starting_space[1] - 2]
                    board.print_board()                
                    return self.king_double_jump_check(starting_space, player_color)
                    
                elif valid_jumps[0] == 'up right':
                    self.board[starting_space[0]][starting_space[1]] = None
                    self.board[starting_space[0] - 1][starting_space[1] + 1] = None
                    self.board[starting_space[0] - 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                    self.board[starting_space[0] - 2][starting_space[1] + 2].king = True
                    starting_space = [starting_space[0] - 2, starting_space[1] + 2]
                    board.print_board() 
                    return self.king_double_jump_check(starting_space, player_color)
                    
                elif valid_jumps[0] == 'down right':
                    self.board[starting_space[0]][starting_space[1]] = None
                    self.board[starting_space[0] + 1][starting_space[1] + 1] = None
                    self.board[starting_space[0] + 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                    self.board[starting_space[0] + 2][starting_space[1] + 2].king = True
                    starting_space = [starting_space[0] + 2, starting_space[1] + 2]
                    board.print_board()                   
                    return self.king_double_jump_check(starting_space, player_color)
                    
                elif valid_jumps[0] == 'down left':
                    self.board[starting_space[0]][starting_space[1]] = None
                    self.board[starting_space[0] + 1][starting_space[1] - 1] = None
                    self.board[starting_space[0] + 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                    self.board[starting_space[0] + 2][starting_space[1] - 2].king = True
                    starting_space = [starting_space[0] + 2, starting_space[1] - 2]
                    board.print_board()                   
                    return self.king_double_jump_check(starting_space, player_color)
            # More than one possible choice:       
            elif len(valid_jumps) > 1:
                valid_input = False
                while valid_input == False:
                    ending_space = input('Type the direction in which you would like to jump to (ex: up left, up right): ')
                    if ending_space not in valid_jumps:
                        print('ERROR: invalid input!')
                        continue
                    elif ending_space == 'up left':
                        self.board[starting_space[0]][starting_space[1]] = None
                        self.board[starting_space[0] - 1][starting_space[1] - 1] = None
                        self.board[starting_space[0] - 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                        self.board[starting_space[0] - 2][starting_space[1] - 2].king = True
                        # if player_color == 'red':
                        #     self.red_score += 1
                        # else:
                        #     self.blue_score += 1
                        starting_space = [starting_space[0] - 2, starting_space[1] - 2]
                        board.print_board()                        
                        return self.king_double_jump_check(starting_space, player_color)
                        
                    elif ending_space == 'up right':
                        self.board[starting_space[0]][starting_space[1]] = None
                        self.board[starting_space[0] - 1][starting_space[1] + 1] = None
                        self.board[starting_space[0] - 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                        self.board[starting_space[0] - 2][starting_space[1] + 2].king = True
                        # if player_color == 'red':
                        #     self.red_score += 1
                        # else:
                        #     self.blue_score += 1
                        starting_space = [starting_space[0] - 2, starting_space[1] + 2]
                        board.print_board()                        
                        return self.king_double_jump_check(starting_space, player_color)
                        
                    elif ending_space == 'down right':
                        self.board[starting_space[0]][starting_space[1]] = None
                        self.board[starting_space[0] + 1][starting_space[1] + 1] = None
                        self.board[starting_space[0] + 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                        self.board[starting_space[0] + 2][starting_space[1] + 2].king = True
                        # if player_color == 'red':
                        #     self.red_score += 1
                        # else:
                        #     self.blue_score += 1
                        starting_space = [starting_space[0] + 2, starting_space[1] + 2]
                        board.print_board()                         
                        return self.king_double_jump_check(starting_space, player_color)
                        
                    elif ending_space == 'down left':
                        self.board[starting_space[0]][starting_space[1]] = None
                        self.board[starting_space[0] + 1][starting_space[1] - 1] = None
                        self.board[starting_space[0] + 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                        self.board[starting_space[0] + 2][starting_space[1] - 2].king = True
                        # if player_color == 'red':
                        #     self.red_score += 1
                        # else:
                        #     self.blue_score += 1
                        starting_space = [starting_space[0] + 2, starting_space[1] - 2]
                        board.print_board() 
                        return self.king_double_jump_check(starting_space, player_color)
                        
            else: # No double jumps found
                return
            
    def get_users_move(self, current_player):
        
        if current_player == 'blue':
            print(YELLOW + 'PLAYER: ' + RESET + BLUE + 'Blue' + RESET)
        else:
            print(YELLOW + 'PLAYER: ' + RESET + RED + 'Red' + RESET)

        is_valid_piece = False
        is_valid_input = False
        is_valid_move = False
        
        while is_valid_piece == False:
            while is_valid_input == False:
                try:
                    starting_input = input('Select a piece to move (ex: i, j): ')
                    starting_space = list(map(int, starting_input.split(',')))
                    if len(starting_space) != 2 or starting_space[0] <= 0 or starting_space[1] <= 0 or starting_space[0] >= 9 or starting_space[1] >= 9:
                        print(RED + 'ERROR: ' + RESET + 'Out of bounds. 1')
                        continue
                    if self.board[starting_space[0]][starting_space[1]] is None or self.board[starting_space[0]][starting_space[1]].color != current_player:
                        print(RED + 'ERROR: ' + RESET + 'That space does not contain a valid piece!1')
                        continue
                    else:
                        is_valid_input = True
                     
                except ValueError:
                    print(RED + 'ERROR: ' + RESET + 'Invalid input format. Please enter two integers separated by a comma (ex: 1, 2)1')
            else:
                is_valid_piece = True
            
            # Select space to move to (REGULAR piece):
            is_valid_input = False
            if self.board[starting_space[0]][starting_space[1]].king == False:
                while is_valid_move == False:
                    while is_valid_input == False:
                        try:
                            ending_input = input('Select space to move to (ex: i, j): ')
                            ending_space = list(map(int, ending_input.split(',')))
                            if len(ending_space) != 2 or ending_space[0] <= 0 or ending_space[1] <= 0 or ending_space[0] >= 9 or ending_space[1] >= 9:
                                print(RED + 'ERROR: ' + RESET + 'Out of bounds.')
                                continue
                            if abs(starting_space[0] - ending_space[0]) == 1 and abs(starting_space[1] - ending_space[1]) != 1:
                                print(RED + 'ERROR: ' + RESET + 'Invalid move1.')
                                continue
                            if abs(starting_space[0] - ending_space[0]) == -1 and abs(starting_space[1] - ending_space[1]) == 1:
                                print(RED + 'ERROR: ' + RESET + 'Invalid move2.')
                                continue
                            if abs(starting_space[0] - ending_space[0]) == 2 and abs(starting_space[1] - ending_space[1]) != 2:
                                print(RED + 'ERROR: ' + RESET + 'Invalid move3.')
                                continue
                            if abs(starting_space[0] - ending_space[0]) == -2 and abs(starting_space[1] - ending_space[1]) == 2:
                                print(RED + 'ERROR: ' + RESET + 'Invalid move4.')
                                continue
                            else:
                                is_valid_input = True
                                
                        except ValueError:
                            print(RED + 'ERROR: ' + RESET + 'Invalid input format. Please enter two integers separated by a comma (ex: 1, 2)1')
                        
                        # Jump attempts:
                    if abs(starting_space[0] - ending_space[0]) == 2:
                        if current_player == 'red': 
                            if starting_space[0] - ending_space[0] == -2 and self.board[ending_space[0]][ending_space[1]] is None:
                                # Could set the return value to this method to boolean, save as var, and exit state or display message based on bool
                                is_jump_valid_boolean = self.is_jump_valid(starting_space, ending_space, current_player)
                                if is_jump_valid_boolean == True:
                                    # Break the loop
                                    is_valid_move = True
                                    return
                                else:
                                    # Jump is invalid
                                    print('Invalid move! (jump attempt, red player)')
                                    is_valid_input = False
                                    continue
                        elif current_player == 'blue':
                            if starting_space[0] - ending_space[0] == 2 and self.board[ending_space[0]][ending_space[1]] is None:
                                is_jump_valid_boolean = self.is_jump_valid(starting_space, ending_space, current_player)
                                if is_jump_valid_boolean == True:
                                    # Break the loop
                                    is_valid_move = True
                                    return
                                else:
                                    # Jump is invalid
                                    print('Invalid move! (jump attempt, blue player)')
                                    is_valid_input = False
                                    continue

                    # Regular movements:
                    elif abs(starting_space[0] - ending_space[0]) == 1:
                        
                        if current_player == 'red':
                            if starting_space[0] - ending_space[0] == -1 and self.board[ending_space[0]][ending_space[1]] is None:
                                # move is valid AS FAR AS I KNOW
                                self.board[starting_space[0]][starting_space[1]] = None
                                self.board[ending_space[0]][ending_space[1]] = Checkers_Piece('red')
                                is_valid_move = True
                                return
                            else:
                                print('ERROR: Invalid movement. (blue movement block)')
                                # probably bad design?
                                board.print_board()
                                return self.get_users_move(current_player)
                        elif current_player == 'blue':                           
                            if starting_space[0] - ending_space[0] == 1 and self.board[ending_space[0]][ending_space[1]] is None:
                                self.board[starting_space[0]][starting_space[1]] = None
                                self.board[ending_space[0]][ending_space[1]] = Checkers_Piece('blue')
                                is_valid_move = True
                                return
                            else:
                                print('ERROR: Invalid movement. (blue movement block)')
                                # probably bad design?
                                board.print_board()
                                return self.get_users_move(current_player)
                    else:
                        print('ERROR: Invalid move.')
                        is_valid_input = False
                        break
            # Select space to move to (KING piece)
            elif self.board[starting_space[0]][starting_space[1]].king == True:
                while is_valid_move  == False:
                    while is_valid_input == False:
                        try:
                            ending_input = input('Select space to move to (ex: i, j)')
                            ending_space = list(map(int, ending_input.split(',')))
                            if len(ending_space) != 2 or ending_space[0] <= 0 or ending_space[1] <= 0 or ending_space[0] >= 9 or ending_space[1] >= 9:
                                print(RED + 'ERROR: ' + RESET + 'Out of bounds. king')
                                continue
                            if abs(starting_space[0] - ending_space[0]) == 1 and abs(starting_space[1] - ending_space[1]) != 1:
                                print(RED + 'ERROR: ' + RESET + 'Invalid move1. king')
                                continue
                            if abs(starting_space[0] - ending_space[0]) == -1 and abs(starting_space[1] - ending_space[1]) == 1:
                                print(RED + 'ERROR: ' + RESET + 'Invalid move2. king')
                                continue
                            if abs(starting_space[0] - ending_space[0]) == 2 and abs(starting_space[1] - ending_space[1]) != 2:
                                print(RED + 'ERROR: ' + RESET + 'Invalid move3. king')
                                continue
                            if abs(starting_space[0] - ending_space[0]) == -2 and abs(starting_space[1] - ending_space[1]) == 2:
                                print(RED + 'ERROR: ' + RESET + 'Invalid move4. king')
                                continue
                            else:
                                is_valid_input = True
                            
                        except ValueError:
                            (RED + 'ERROR: ' + RESET + 'Invalid input!  kingpiece 1')
                    
                    if abs(starting_space[0] - ending_space[0]) == 2 and self.board[ending_space[0]][ending_space[1]] == None:
                        # Check for jump. Do color checking inside the 'king_double_jump()' func:
                        is_jump_valid_boolean = self.king_is_jump_valid(starting_space, ending_space,current_player)
                        if is_jump_valid_boolean == True:
                            is_valid_move = True
                            return
                     
                    if abs(starting_space[0] - ending_space[0]) == 1 and self.board[ending_space[0]][ending_space[1]] == None: # [3, 6] -> [4, 5]
                        # move is valid
                        self.board[starting_space[0]][starting_space[1]] = None
                        self.board[ending_space[0]][ending_space[1]] = Checkers_Piece(current_player)
                        self.board[ending_space[0]][ending_space[1]].king = True
                        return
                    else:
                        print(RED + 'ERROR: ' + RESET + 'Invalid move (end of king movement block)')
                        is_valid_move = False
                        is_valid_input = False
    
# MAIN script:
board = Checkers_Board()
board.make_board()
move = Move(board.board, 'blue')

# testing board state:
# board.board[1][2] = Checkers_Piece('blue')
# board.board[1][8] = None
# board.board[4][5] = Checkers_Piece('red')
# board.board[1][4] = Checkers_Piece('red')

# board.board[3][4] = None
# board.board[4][3] = Checkers_Piece('red')
# board.board[1][6] = None
# board.board[8][1] = None
# board.board[5][4] = Checkers_Piece('blue')
# board.board[6][3] = None
# board.board[8][5] = None
# board.board[6][7] = None
# board.board[4][7] = Checkers_Piece('blue')
# board.board[3][6] = None
# board.board[3][2] = None
# board.board[5][6] = Checkers_Piece('blue')
# board.board[5][6].king = True
# board.board[6][7] = None
# board.board[8][5] = Checkers_Piece('blue')
# board.board[8][1] = Checkers_Piece('blue')

while board.game_over == False:
    board.create_king()
    board.print_board()
    move.get_users_move(board.current_player['color'])
    board.change_player()
                        
                            
                    

                            
