# Создаем пустое игровое поле 3х3
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


# Печатаем текущее состояние игрового поля
def print_board(board):
    print()
    print("      1     2     3")
    for i in range(3):
        print(f'{str(i + 1)} {" | "} {board[i][0]} {" | "} {board[i][1]} {" | "} {board[i][2]} {" | "}')
        if i != 2:
            print("   -------------------")
    print()


# Определяем функцию, которая проверяет, выиграл ли кто-то
def check_win(board):
    # Проверяем по горизонтали
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return True
    # Проверяем по вертикали
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return True
    # Проверяем по диагонали
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return False


# Определяем функцию, которая проверяет, есть ли свободные клетки на поле
def check_tie(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


# Импортируем модуль времени
import time


# Запускаем основной цикл игры
def play_game():
    print()
    print("Добро пожаловать в игру Крестики-нолики!")
    print()
    time.sleep(2)  # добавляем задержку в две секунды
    player_1 = input("Первый игрок, представьтесь пожалуйста (Вы будете Х)\n>>> ")
    player_2 = input("Второй игрок, как обращаться к Вам? (Вы будете 0)\n>>> ")
    print()
    print(f'{player_1}, {player_2} очень приятно.\nДавайте начнем игру.')
    current_player = player_1
    time.sleep(2)  # добавляем задержку в две секунды
    while True:
        print_board(board)
        print(f'{current_player}, Ваш ход: ')
        while True:
            row = input("Выберите строку (1-3): ")
            if len(row) == 1 and row.isdigit():
                row = int(row)
                if row in [1, 2, 3]:
                    break
                else:
                    print()
                    print("Некорректный выбор номера строки.")
            else:
                print()
                print("Пожалуйста, введите только одну цифру.")
        while True:
            col = input("Выберите столбец (1-3): ")
            if len(col) == 1 and col.isdigit():
                col = int(col)
                if col in [1, 2, 3]:
                    break
                else:
                    print()
                    print("Некорректный выбор номера столбца.")
            else:
                print()
                print("Пожалуйста, введите только одну цифру.")
        if board[row - 1][col - 1] != " ":
            print()
            print(f'{current_player}, эта клетка уже занята.\nПопробуйте еще раз.')
            continue
        if current_player == player_1:
            board[row - 1][col - 1] = "X"
        else:
            board[row - 1][col - 1] = "O"
        if check_win(board):
            print_board(board)
            print("Поздравляю!", current_player, "Вы выйграли!")
            break
        if check_tie(board):
            print_board(board)
            print("Ничья!")
            break
        if current_player == player_1:
            current_player = player_2
        else:
            current_player = player_1


# Запускаем игру
play_game()

# Выводим сообщение о завершении игры
print("Спасибо за игру!")
print()
print("Версия игры 1.3")
