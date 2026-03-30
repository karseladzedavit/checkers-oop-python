from board import Board

board = Board()
board.create_pieces()


current_turn = "Red"
while True:
    board.display()
    red_count = 0
    black_count = 0
    for i in board.grid:
        for j in i:
            if j != " ":
                if j.color=="Red":
                    red_count+=1
                else:
                    black_count+=1
    print(f"Red has {red_count} pieces left")
    print(f"Black has {black_count} pieces left")
    
            
    try:
        move_str = input("Enter move (r1 c1 r2 c2): ")
        r1,c1,r2,c2 = map(int,move_str.replace(",", " ").split())
        selected_piece = board.grid[r1][c1]
        if(selected_piece == " "):
            print("There is no piece there!"); continue
        if(selected_piece.color != current_turn):
            print(f"It is {current_turn}'s turn"); continue
        if board.move_piece((r1, c1), (r2, c2)):
            print("Move successful!")
            if(current_turn=="Red"):
                current_turn="Black"
            else:
                current_turn="Red"
        else:
            print("Please try again.")
            
        if board.check_winner() == "Red":
            print("Game Over, Winner is Red"); break
        if board.check_winner() == "Black":
            print("Game Over, Winner is Black"); break
        
    except (ValueError, IndexError):
        print("Invalid input! Please enter 4 numbers (0-7) separated by spaces.")
   


