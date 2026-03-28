from board import Board

board = Board()
board.create_pieces()



while True:
    board.display()
    move_str = input("Enter move (r1 c1 r2 c2): ")
    r1,c1,r2,c2 = map(int,move_str.split())
    if board.move_piece((r1, c1), (r2, c2)):
        print("Move successful!")
    
    else:
        print("Please try again.")