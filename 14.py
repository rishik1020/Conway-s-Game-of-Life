import time
import os

def game_of_life(board, generations):
    rows, cols = len(board), len(board[0])

    def print_board(b):
        os.system('cls' if os.name == 'nt' else 'clear')
        for r in range(rows):
            print(" ".join(["■" if b[r][c] else "□" for c in range(cols)]))
        print("-" * (2 * cols))

    for gen in range(generations):
        print(f"Generation: {gen + 1}")
        print_board(board)
        time.sleep(0.5)

        # Create a new board for the next state
        next_board = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0
                # Check all 8 neighbors
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        nr, nc = r + i, c + j
                        if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 1:
                            live_neighbors += 1
                
                # Apply rules
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    next_board[r][c] = 0
                elif board[r][c] == 0 and live_neighbors == 3:
                    next_board[r][c] = 1
                else:
                    next_board[r][c] = board[r][c]
        board = next_board

# Example: A "Glider" pattern
initial_board = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

game_of_life(initial_board, 20)