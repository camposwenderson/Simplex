class simplex:

    def _init_(self):
        self.table = []

    def set_objective_function(self, fo: list):
        self.table.append(fo)

    def add_rescritions(self, sa: list):
        self.table.append(sa)
    
    def get_entry_column(self) -> int:
        colum_pivot = min(self.table[0])
        index = self.table.index(colum_pivot)

        return index
    def get_exit_line(self, entry_colum: int) -> int:
        results = {}
        for line in range(len(self.table)):
            if line > 0:
                if self.table[line] [entry_colum] > 0:
                    division = self.table[line][-1]/self.table[line][entry_colum]
                    results[line] = division
        index = min(results, key=results.get)

        return index
    
    def calculate_new_line(self, line: list, entry_colum: int, pivot_line: list) -> list:
        pivot = line[entry_colum] * -1

        result_line = [value * pivot for value in pivot_line]

        new_line = []

        for i in range(len(result_line)):
            sum_value = result_line[i] + line [i]
            new_line.append(sum_value)

        return new_line

    def is_negative(self) -> bool:
        negative = list(filter(lambda x: x < 0, self.table[0]))

        return True if len(negative)>0 else False

        def show_table(self):
            for i in range(len(self.table)):
                for j in range(len(self.table[0])):
                    print(f"{self.table[i][j]}\t", end="")
                print()
    
    def calculate(self):

        entry_colum = self.get_entry_colum()

        first_exit_line = self.get_exit_line(entry_colum)

        pivot_line = self.table[first_exit_line]
        
        self.table[first_exit_line] = pivot_line

        table_copy = self.table.copy()

        index = 0

        while index < len(self.table):
            if index != first_exit_line:
                line = table_copy[index]
                new_line = self.calculate_new_line(line, entry_colum, pivot_line)
                self.table[index] = new_line
                index += 1

    def solve(self):
        self.calculate()

        while self.is_negative():
            self.calculate()

        self.show_table()

if __name__ == '__main__':
    """
        MAX fo: 5x + 2y
        sa:
            2x + y <= 6
            10x + 12y <= 60
            x, y >= 0

        forma simplex:

        z - 5x + 2y = 0
            2x + y + f1 = 6
            10x + 12y + f2 = 60
    """
    simplex = simplex()
    simplex.set_objective_function([1, -5, -2, 0, 0, 0])

    simplex.add_rescritions([0, 2, 1, 1, 0, 6])
    simplex.add_rescritions([0, 10, 12, 0, 1, 60])

    simplex.solve()