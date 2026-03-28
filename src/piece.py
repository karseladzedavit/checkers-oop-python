class Piece:
    def __init__(self,color):
        self.color = color
        self.is_king = False


    def __str__(self):
       char = "R" if self.color == "Red" else "B"
       if self.is_king:
        return char + "K"
    
       return char