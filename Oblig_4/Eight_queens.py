class EQ:
    def __init__(self):
        pass

    



def main():

    board1 = EQ()
    board1.set(0, 2)
    board1.set(1, 4)
    board1.set(2, 7)
    board1.set(3, 1)
    board1.set(4, 0)
    board1.set(5, 3)
    board1.set(6, 6)
    board1.set(7, 5)

    print(f"Is board1 a correct eight queen placement? {board1.isSolved()}")

    board2 = EQ([0, 4, 7, 5, 2, 6, 1, 3])

    if board2.isSolved():
        print("Eight queens are placed correctly in board2")

        board2.printBoard()

    else:
        print("Eight queens are placed incorrectly in board2")

if __name__ == "__main__":
    main()
