import pygame
import sys
import copy

pygame.init()

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 5, 5
SQUARE_SIZE = WIDTH // COLS

WHITE = (240, 217, 181)
BLACK = (181, 136, 99)
HIGHLIGHT = (186, 202, 68)

PLAYER = 1
AI = 2
EMPTY = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("5x5 Hexapawn")

FONT = pygame.font.SysFont("Arial", 32)

margin = 2
pawn_white = pygame.transform.scale(pygame.image.load("pawn_white.png"), (SQUARE_SIZE - margin + 25, SQUARE_SIZE - margin))
pawn_black = pygame.transform.scale(pygame.image.load("pawn_black.png"), (SQUARE_SIZE - margin, SQUARE_SIZE - margin + 25))


def init_board():
    board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
    board[0] = [AI] * COLS
    board[ROWS - 1] = [PLAYER] * COLS
    return board

def draw_board(board, selected=None):
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect)
            if selected == (row, col):
                pygame.draw.rect(screen, HIGHLIGHT, rect, 5)
            piece = board[row][col]
            if piece == PLAYER:
                screen.blit(pawn_white, (rect.centerx - pawn_white.get_width() // 2, rect.centery - pawn_white.get_height() // 2))
            elif piece == AI:
                screen.blit(pawn_black, (rect.centerx - pawn_black.get_width() // 2, rect.centery - pawn_black.get_height() // 2))

def animate_move(board, start, end):
    piece = board[start[0]][start[1]]
    x1, y1 = start[1] * SQUARE_SIZE, start[0] * SQUARE_SIZE
    x2, y2 = end[1] * SQUARE_SIZE, end[0] * SQUARE_SIZE
    sprite = pawn_white if piece == PLAYER else pawn_black
    frames = 10
    for i in range(frames + 1):
        screen.fill((0, 0, 0))
        draw_board(board)
        t = i / frames
        x = int(x1 + (x2 - x1) * t)
        y = int(y1 + (y2 - y1) * t)
        screen.blit(sprite, (x, y))
        pygame.display.flip()
        pygame.time.delay(30)

def get_valid_moves(board, player):
    direction = -1 if player == PLAYER else 1
    moves = []
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == player:
                nr = r + direction
                if 0 <= nr < ROWS:
                    if board[nr][c] == EMPTY:
                        moves.append(((r, c), (nr, c)))
                    for dc in [-1, 1]:
                        nc = c + dc
                        if 0 <= nc < COLS and board[nr][nc] != EMPTY and board[nr][nc] != player:
                            moves.append(((r, c), (nr, nc)))
    return moves

def move_piece(board, move):
    (r1, c1), (r2, c2) = move
    board[r2][c2] = board[r1][c1]
    board[r1][c1] = EMPTY

def is_winner(board, player):
    if player == PLAYER and any(board[0][c] == PLAYER for c in range(COLS)):
        return True
    if player == AI and any(board[ROWS - 1][c] == AI for c in range(COLS)):
        return True
    return False

def evaluate(board):
    return sum(cell == AI for row in board for cell in row) - sum(cell == PLAYER for row in board for cell in row)

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_winner(board, PLAYER) or is_winner(board, AI):
        return evaluate(board), None
    player = AI if maximizing_player else PLAYER
    moves = get_valid_moves(board, player)
    if not moves:
        return evaluate(board), None
    best_move = None
    if maximizing_player:
        max_eval = float('-inf')
        for move in moves:
            new_board = copy.deepcopy(board)
            move_piece(new_board, move)
            eval, _ = minimax(new_board, depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in moves:
            new_board = copy.deepcopy(board)
            move_piece(new_board, move)
            eval, _ = minimax(new_board, depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def get_mouse_square():
    x, y = pygame.mouse.get_pos()
    return y // SQUARE_SIZE, x // SQUARE_SIZE

def show_end_screen(message):
    while True:
        screen.fill((0, 0, 0))
        label = FONT.render(message, True, (255, 255, 255))
        button = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 + 40, 150, 50)
        pygame.draw.rect(screen, (100, 200, 100), button)
        btn_text = FONT.render("Restart", True, (0, 0, 0))
        screen.blit(label, (WIDTH // 2 - label.get_width() // 2, HEIGHT // 2 - 80))
        screen.blit(btn_text, (button.centerx - btn_text.get_width() // 2, button.centery - btn_text.get_height() // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(pygame.mouse.get_pos()):
                    return  # Restart the game

def main():
    board = init_board()
    running = True
    selected = None
    player_turn = True
    while running:
        screen.fill((0, 0, 0))
        draw_board(board, selected)
        pygame.display.flip()

        player_moves = get_valid_moves(board, PLAYER)
        ai_moves = get_valid_moves(board, AI)

        if is_winner(board, AI):
            show_end_screen("AI Wins!")
            return main()
        elif is_winner(board, PLAYER):
            show_end_screen("Player Wins!")
            return main()
        elif not player_moves and not ai_moves:
            show_end_screen("It's a Draw!")
            return main()
        elif player_turn and not player_moves:
            show_end_screen("AI Wins!")
            return main()
        elif not player_turn and not ai_moves:
            show_end_screen("Player Wins!")
            return main()

        if not player_turn:
            _, move = minimax(board, 3, float('-inf'), float('inf'), True)
            if move:
                animate_move(board, *move)
                move_piece(board, move)
            player_turn = True
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                row, col = get_mouse_square()
                if selected:
                    if ((selected, (row, col))) in player_moves:
                        animate_move(board, selected, (row, col))
                        move_piece(board, (selected, (row, col)))
                        selected = None
                        player_turn = False
                    else:
                        selected = None
                elif board[row][col] == PLAYER:
                    selected = (row, col)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
