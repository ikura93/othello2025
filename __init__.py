
EMPTY = 0
BLACK = 1
WHITE = -1 # コードの count_pieces に合わせて -1 に統一
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
BOARD_SIZE = 6 # コードの範囲指定 (range(6)) に基づく


def myai(board, color):
    """
    AIが選択する手 (現時点では最初の有効な手を返す)
    """
    # get_valid_moves 関数を呼び出し、全ての有効な手をリストアップ
    valid_moves = get_valid_moves(board, color)
    
    if not valid_moves:
        return None 
    
    row, col = valid_moves[0]
    return (col, row) 


def get_valid_moves(board, color):
    """
    指定された色の有効な手をすべて取得する (myaiから分離)
    """
    valid_moves = []
    
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY: # 0 は EMPTY
                if is_valid_move(board, i, j, color, DIRECTIONS):
                    valid_moves.append((i, j)) # (row, col) の順序で追加

    return valid_moves


def is_valid_move(board, row, col, color, directions):
    """
    指定された位置が有効な手かどうかを判定する
    """
    for dr, dc in directions:
        if has_flippable_pieces(board, row, col, color, dr, dc):
            return True
    return False


def has_flippable_pieces(board, row, col, color, dr, dc):
    """
    指定された方向に反転可能なピースがあるかを確認する
    """
    r, c = row + dr, col + dc
    count = 0

    while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
        if board[r][c] == EMPTY:
            return False
        if board[r][c] == color:
            return count > 0 
        
        count += 1
        r += dr
        c += dc

    return False


def play_move(board, row, col, color):
    """
    手を受け、ボードを更新して反転させたピース数を返す
    """
    board[row][col] = color
    total_flipped = 0

    for dr, dc in DIRECTIONS:
        flipped = flip_pieces(board, row, col, color, dr, dc)
        total_flipped += flipped

    return total_flipped


def flip_pieces(board, row, col, color, dr, dc):
    """
    指定された方向のピースを反転させる
    """
    r, c = row + dr, col + dc
    flipped_pieces = []

    while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
        if board[r][c] == EMPTY:
            return 0
        if board[r][c] == color:
            for fr, fc in flipped_pieces:
                board[fr][fc] = color
            return len(flipped_pieces)
        
        flipped_pieces.append((r, c))
        r += dr
        c += dc

    return 0


def count_pieces(board):
    """
    ボード上のピースの数をカウントする
    """
    black_count = sum(row.count(BLACK) for row in board)
    white_count = sum(row.count(WHITE) for row in board)
    return black_count, white_count


def is_game_over(board):
    """
    ゲームが終了したかを判定する
    """
    return len(get_valid_moves(board, BLACK)) == 0 and len(get_valid_moves(board, WHITE)) == 0
