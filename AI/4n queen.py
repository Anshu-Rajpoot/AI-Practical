class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0]*n for _ in range(n)]
        self.row = [False]*n
        self.col = [False]*n
        self.diag1 = [False]*(2*n - 1)
        self.diag2 = [False]*(2*n - 1)
        self.solutions = []

    def solve(self):
        self.solve_helper(0)
        return self.solutions

    def solve_helper(self, col):
        if col == self.n:
            self.solutions.append([row[:] for row in self.board])
            return True
        for row in range(self.n):
            if self.is_valid(row, col):
                self.board[row][col] = 1
                self.row[row] = True
                self.col[col] = True
                self.diag1[row+col] = True
                self.diag2[row-col+self.n-1] = True
                self.solve_helper(col+1)
                self.board[row][col] = 0
                self.row[row] = False
                self.col[col] = False
                self.diag1[row+col] = False
                self.diag2[row-col+self.n-1] = False

    def is_valid(self, row, col):
        return not self.row[row] and not self.col[col] and not self.diag1[row+col] and not self.diag2[row-col+self.n-1]

n = 4
solver = NQueens(n)
solutions = solver.solve()
print(f"Found {len(solutions)} solutions for {n}-queens problem:")
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        print(row)
    print()
