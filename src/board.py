from piece import Piece

class Board:
    
    def __init__(self):
        self.grid = [[" " for _ in range(8)] for _ in range(8)]
        
        

    def display(self):
        print(" ", end=" ")
        for i in range(8):
            print(i, end=" ")
        print()
        for i in range(len(self.grid)):
            print(i, end=" ")
            for j in range(len(self.grid[i])):
                if(self.grid[i][j] == " "):
                    print(".", end=" ")
                else:
                    print(self.grid[i][j], end=" ")
            print()
            
    def create_pieces(self):
        for row in range(len(self.grid)):
            if row == 3 or row == 4:
                continue
            for col in range(len(self.grid[row])):
                if row < 3  and (row + col) % 2 != 0:
                    p = Piece("Black")
                    self.grid[row][col] = p
                elif row > 4  and (row + col) % 2 != 0:   
                    p = Piece("Red")
                    self.grid[row][col] = p
                    
                    
    def move_piece(self,start_pos, end_pos):
        start_row , start_col = start_pos
        end_row, end_col = end_pos
        
        #check bounds
        if not (0 <= start_row < 8 and 0 <= end_row < 8 and 0 <= start_col < 8 and 0 <= end_col < 8): 
            print("Outside board!"); return False
            
        #Check occupancy  
        if(self.grid[start_row][start_col]==" "):
            print("No piece there!"); return False
        if(self.grid[end_row][end_col] != " "):
            print("Target occupied!"); return False
            
        piece = self.grid[start_row][start_col]
        #check direction
        if piece.color == "Black" and end_row < start_row and not piece.is_king: 
            print("Can't move piece backword"); return False
        if piece.color == "Red" and end_row > start_row and not piece.is_king: 
            print("Can't move piece backword"); return False
        
        #check diagonal
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        if row_diff not in [1,2] or row_diff!= col_diff:
            print("Not a diagonal move!"); return False
        
        if(row_diff==2 and col_diff==2):
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            if self.grid[mid_row][mid_col] == " ":
                print("Not a valid  move!"); return False
            if self.grid[mid_row][mid_col].color == piece.color:
                print("Not a valid  move! Cant kill your piece"); return False
            self.grid[mid_row][mid_col]= " "
                        
        
        self.grid[start_row][start_col] = " "
        self.grid[end_row][end_col] = piece
        
        if piece.color =="Black" and end_row==7:
            piece.make_king()
        if piece.color =="Red" and end_row==0:
            piece.make_king()
        return True
        