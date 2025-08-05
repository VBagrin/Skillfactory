def print_board(board):
    print("  0 1 2")
    for i, row in enumerate(board):
        print(i, " ".join(row))


def check_winner(board):
    # Проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "-":
            return True
    # Диагонали
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return True
    return False


def is_full(board):
    return all(cell != "-" for row in board for cell in row)


# Основной игровой цикл
board = [["-" for _ in range(3)] for _ in range(3)]
current_player = "X"

while True:
    print_board(board)
    try:
        row, col = map(int, input(f"Игрок {current_player}, введите координаты (строка и столбец): ").split())
        if board[row][col] != "-":
            print("Ячейка уже занята. Попробуйте снова.")
            continue
        board[row][col] = current_player
        if check_winner(board):
            print_board(board)
            print(f"Игрок {current_player} победил!")
            break
        if is_full(board):
            print_board(board)
            print("Ничья!")
            break
        current_player = "O" if current_player == "X" else "X"
    except (ValueError, IndexError):
        print("Неверный ввод. Введите две цифры от 0 до 2, разделённые пробелом.")
