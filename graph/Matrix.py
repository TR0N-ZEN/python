class Matrix:
    def __init__(self, amount_rows, amount_columns):
        self.row = list()
        for i in range(amount_rows):
            dummy_row = list()
            for i in range(amount_columns):
                dummy_row.append(0)
            self.row.append(dummy_row)
        self.print()

    def rows(self, string):
        return len(self.row) if string == "amount" else self.row

    def columns(self, string):
        if string == "amount":
            return len(self.row[0])
        elif string == "":
            columns = list()
            for column_index in range(len(self.columns("amount"))):
                column = list()
                for row in self.row:
                    column.append(row[column_index])
                columns.append(column)

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

    def add(m1, m2):
        if len(m1.row) == len(m2.row):
            for row in range(len(m1.row)):
                if len(m1.row[row]) != m2.row[row]:
                    return "ERROR"
        else:
            return "ERROR"
        matrix = Matrix(len(m1.row), len(m1.row[0]))
        for row in range(len(m1.row)):
            for column in range(len(row)):
                matrix.enter(
                        m1.row[row][column]+m2.row[row][column],
                        row,
                        column)
        return matrix

    def multiply(m1, m2):
        if m1.columns("amount") != m2.rows("amount"):
            return "ERROR"
        matrix = Matrix(m1.rows("amount"), m2.columns("amount"))
        for i in m2.columns("amount"):  # i is a column variable for m2
            for k in m1.rows("amount"):  # k is a row variable for m1
                sum = 0
                # j is a row variabel for m2 and a column variable for m1
                for j in range(m2.rows("amount")):
                    sum += m1.entry(k, j)*m2.entry(j, i)
                matrix.enter(sum, k, i)  # for every column in m2 there will be

