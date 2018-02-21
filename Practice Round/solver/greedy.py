from .basesolver import BaseSolver


class Solver(BaseSolver):
    # Greedy solver as presented during
    # 'Get Ready for Hash Code 2018' (https://youtu.be/rosx_Xa-R5Y)

    def __init__(self, input_str):
        self.input_str = input_str
        self.row_count, self.column_count, self.min_ingredient, self.max_area = 0, 0, 0, 0
        self.grid = []
        self.results = []

        # read all the input
        self.read_input()

    def write(self, output_str):
        with open(output_str, 'w') as f:
            f.write(str(len(self.results)))
            f.write('\n')
            for s in self.results:
                f.write(" ".join([str(iii) for iii in list(s)]))
                f.write('\n')

    def solve(self):
        self.results = []

        # For each row, reset the counters
        for r in range(self.row_count):
            beg = 0
            end = 0
            mushroom_count = 0
            tomato_count = 0

            # while not at the end of the row
            # count if tomato or mushroom
            while end < self.column_count:
                if self.grid[r][end] == 'M':
                    mushroom_count += 1
                elif self.grid[r][end] == 'T':
                    tomato_count += 1
                end += 1

                # if slice is too big, remoge ingredient
                if end - beg > self.max_area:
                    if self.grid[r][beg] == 'M':
                        mushroom_count -= 1
                    elif self.grid[r][beg] == 'T':
                        tomato_count -= 1
                    beg += 1

                # if it is a valid slice,
                # log it in the results and reset the variables
                # in order to continue searching for
                # a new valid slice on the same line
                if (end - beg < self.max_area
                        and mushroom_count >= self.min_ingredient
                        and tomato_count >= self.min_ingredient):
                    self.results.append((r, beg, r, end - 1))
                    beg = end
                    tomato_count = 0
                    mushroom_count = 0

    def read_input(self):
        with open(self.input_str, 'r') as f:
            first_line = f.readline()

            self.row_count, self.column_count, self.min_ingredient, self.max_area = tuple(
                map(int, first_line.split(' '))
            )

            self.grid = []
            for i in range(self.row_count):
                self.grid.append(f.readline().rstrip())

        print("Problem statement:")
        print(self.row_count, self.column_count, self.min_ingredient, self.max_area)
        print(self.grid)
