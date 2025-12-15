# Generation ID: Hutch_1763363382366_pvtgnx94j (前半)

def myai(board, color):
    """
    指定された色の有効な手をすべて取得する
    """
    valid_moves = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i in range(6):
        for j in range(6):
            if board[i][j] == 0:
                if is_valid_move(board, i, j, color, directions):
                    valid_moves.app# Generation ID: Hutch_1763363382366_pvtgnx94j (前半)

def myai(board, color):
    """
    指定された色の有効な手をすべて取得する
    """
    valid_moves = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i in range(6):
        for j in range(6):
            if board[i][j] == 0:
                if is_valid_move(board, i, j, color, directions):
                    valid_moves.append((i, j))

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

    while 0 <= r < 6 and 0 <= c < 6:
        if board[r][c] == 0:
            return False
        if board[r][c] == color:
            return count > 0
        count += 1
        r += dr
        c += dc

    return False

def play_move(board, row, col, color):
    """
    手を打つ。ボードを更新して反転させたピース数を返す
    """
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    board[row][col] = color
    total_flipped = 0

    for dr, dc in directions:
        flipped = flip_pieces(board, row, col, color, dr, dc)
        total_flipped += flipped

    return total_flipped

def flip_pieces(board, row, col, color, dr, dc):
    """
    指定された方向のピースを反転させる
    """
    r, c = row + dr, col + dc
    flipped_pieces = []

    while 0 <= r < 6 and 0 <= c < 6:
        if board[r][c] == 0:
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
    black_count = sum(row.count(1) for row in board)
    white_count = sum(row.count(-1) for row in board)
    return black_count, white_count

def is_game_over(board):
    """
    ゲームが終了したかを判定する
    """
    return len(get_valid_moves(board, 1)) == 0 and len(get_valid_moves(board, -1)) == 0

# Generation ID: Hutch_1763363382366_pvtgnx94j (後半)
end((i, j))

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

    while 0 <= r < 6 and 0 <= c < 6:
        if board[r][c] == 0:
            return False
        if board[r][c] == color:
            return count > 0
        count += 1
        r += dr
        c += dc

    return False

def play_move(board, row, col, color):
    """
    手を打つ。ボードを更新して反転させたピース数を返す
    """
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    board[row][col] = color
    total_flipped = 0

    for dr, dc in directions:
        flipped = flip_pieces(board, row, col, color, dr, dc)
        total_flipped += flipped

    return total_flipped

def flip_pieces(board, row, col, color, dr, dc):
    """
    指定された方向のピースを反転させる
    """
    r, c = row + dr, col + dc
    flipped_pieces = []

    while 0 <= r < 6 and 0 <= c < 6:
        if board[r][c] == 0:
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
    black_count = sum(row.count(1) for row in board)
    white_count = sum(row.count(-1) for row in board)
    return black_count, white_count

def is_game_over(board):
    """
    ゲームが終了したかを判定する
    """
    return len(get_valid_moves(board, 1)) == 0 and len(get_valid_moves(board, -1)) == 0

# Generation ID: Hutch_1763363382366_pvtgnx94j (後半)
