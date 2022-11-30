def main():
    print("*******************")
    print("        ИГРА       ")
    print("  КРЕСТИКИ-КОЛИКИ  ")
    print("*******************")
    print()
    print("___________________")
    print("Чтобы сделать ход, ")
    print("введите номер строки")
    print("и номер столбца ")
    print("через пробел\n")


def field():
    print()
    print(f"     | 0 | 1 | 2 | ")
    print("   --------------- ")
    for i, j in enumerate(cells):
        unite = f"   {i} | {' | '.join(j)} | "
        print(unite)
        print("   --------------- ")
    print()


def ask():
    while True:
        cords = input("\t\tВаш ход: ").split()

        if len(cords) != 2:
            print(" Введите две координаты через пробел!")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Можно только числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if cells[x][y] != " ":
            print(" Клетка занята! ")
            continue
        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (1, 2)),
                ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)),
                ((0, 0), (1, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)),
                ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []

        for c in cord:
            symbols.append(cells[c[0]][c[1]])

        if symbols == ["X", "X", "X"]:
            print(" Выиграли крестики!!! ")
            return True
        if symbols == ["0", "0", "0"]:
            print(" Выиграли нолики!!! ")
            return True
    return False


main()
cells = [[' '] * 3 for i in range(3)]
count = 0
while True:
    count += 1

    field()

    if count % 2 == 1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик ")

    x, y = ask()

    if count % 2 == 1:
        cells[x][y] = 'X'
    else:
        cells[x][y] = '0'

    if check_win():
        break

    if count == 9:
        print(" Ничья! ")
        break
