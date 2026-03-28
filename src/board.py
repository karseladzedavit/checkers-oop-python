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
                    