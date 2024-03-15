import random

def print_board(heap):
    print(f"Current heap: {'|' * heap}")

def get_user_move(heap):
    while True:
        try:
            sticks_to_remove = int(input(f"Enter the number of sticks to remove (1 to {min(heap, heap // 2)}): "))
            if 1 <= sticks_to_remove <= min(heap, heap // 2):
                return sticks_to_remove
        except ValueError:
            pass
        print(f"Invalid input. Please enter a number between 1 and {min(heap, heap // 2)}.")

def get_computer_move(heap):
    xor_sum = heap ^ sum(range(heap))
    max_sticks = min(heap // 2, heap)
    return max(1, min(max_sticks, heap - xor_sum))

def nim_game():
    heap, player_turn = 16, 1
    while heap > 1:
        print_board(heap)
        player_name = "Player 1" if player_turn == 1 else "Computer"
        sticks_to_remove = get_user_move(heap) if player_turn == 1 else get_computer_move(heap)
        heap -= sticks_to_remove
        print(f"{player_name} removes {sticks_to_remove} sticks.")
        player_turn = 3 - player_turn
    
    print_board(heap)
    winner = "Player 1" if player_turn == 2 else "Computer"
    print(f"{winner} picks the last stick.\n{winner} is the winner!")

if __name__ == "__main__":
    nim_game()
