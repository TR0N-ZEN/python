class Matrix:
    def __init__(self, rows, columns):
        self.row = list()
        for i in range(rows):
            dummy_row = list()
            for i in range(columns):
                dummy_row.append(0)
            self.row.append(dummy_row)
        self.print()
    def row(self, i):
        return self.row[i]
    def column(self, i):
        column = []
        for j in range(len(self.row)):
            column.append(self.row[j][i])
        return column
    def enter(self, value, row, column):
        self.row[row][column] = value
    def entry(self, row, column):
        return self.row[row][column]
    def print(self):
        for row in self.row:
            print(row)
        # for row in range(len(self.row)):
        #     for column in range(len(self.row[row])):
        #         print(self.entry(row, column))