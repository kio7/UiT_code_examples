class EQ:
    def __init__(self, lis = None):
        self.queens = 8 * [-1]
        if lis != None:
            for x in range(0,len(lis)):
                self.set(x, lis[x])
    
    def get(self, i):
        return self.queens[i]

    def set(self, i, j):
        self.queens[i] = j

    """ 
    This next part is a little tricky so i thought i would try to explain myself.

    It's a standard search algorythm that looks through all diagonals but I found an issue in my own throughts.
    It's normal to think about it in 2d and have the search looking in 1d.

    At comment nr. 1 (#1): I check to see if I'm on the same line that I'm actually asking about. so it will skip itself.

    At comment nr. 2 (#2): The counter variable is used to limit the search to the correct paramaters. When i go through the for loop on the
    2nd time i ran into an issue where it would looks through the other elements of the list and ask if they were the wrong value...
    E. g. 2nd run of the loop, first if statement asks if board1[0] == new search value - 0. Which makes no sense.
    What it should ask is if that value == new search value - 1.

    So for every loop of "for i in self.queens:" i needed to fix the search paramater in increments by 1.
    """

    def is_solved(self):
        #2
        counter = 0

        for i in self.queens:
            for j in range(len(self.queens)):
                #1
                if self.queens[j] != self.queens[self.queens.index(i)]:

                    if self.queens[j] == i + j - counter:
                        return False                    
                    if self.queens[j] == i - j + counter:
                        return False
            counter += 1
        return True


    def print_board(self):
        for x in self.queens:
            for _ in range(x):
                print("| ", end ='')

            print("|X", end='')

            for _ in range(7 - x):
                print("| ", end ='')
            
            print('|')


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

    print(f"Is board1 a correct eight queen placement? {board1.is_solved()}")

    board2 = EQ([0, 4, 7, 5, 2, 6, 1, 3])

    if board2.is_solved():
        print("Eight queens are placed correctly in board2")

        board2.print_board()

    else:
        print("Eight queens are placed incorrectly in board2")

if __name__ == "__main__":
    main()
