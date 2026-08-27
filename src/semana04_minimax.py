WIN_LINES = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

def winner(board):
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def minimax_alpha_beta(board, maximizing, alpha, beta):
    w = winner(board)
    if w == "X": return 1
    if w == "O": return -1
    if " " not in board: return 0
    
    if maximizing:
        max_eval = -float('inf')
        for i, cell in enumerate(board):
            if cell == " ":
                nxt = board.copy()
                nxt[i] = "X"
                eval_score = minimax_alpha_beta(nxt, False, alpha, beta)
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break  # Poda Beta
        return max_eval
    else:
        min_eval = float('inf')
        for i, cell in enumerate(board):
            if cell == " ":
                nxt = board.copy()
                nxt[i] = "O"
                eval_score = minimax_alpha_beta(nxt, True, alpha, beta)
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break  # Poda Alfa
        return min_eval

def best_move_alpha_beta(board):
    best_score = -float('inf')
    best_idx = -1
    alpha = -float('inf')
    beta = float('inf')
    
    for i, cell in enumerate(board):
        if cell == " ":
            nxt = board.copy()
            nxt[i] = "X"
            score = minimax_alpha_beta(nxt, False, alpha, beta)
            if score > best_score:
                best_score = score
                best_idx = i
            alpha = max(alpha, score)
            
    return best_idx

board = ["X", "O", "X", "O", "X", " ", " ", " ", "O"]
print("Tablero actual:", board)
print("Mejor posición calculada para X (con Poda Alfa-Beta):", best_move_alpha_beta(board))