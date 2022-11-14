class Matrix:
    def __init__(self, data):
        self.data = data
        self.row = len(self.data)
        self.col = len(self.data[0])
        self.array = [[0] * self.col for i in range(self.row)]
        
    def __repr__(self):
        return f"Matrix({self.data})"
    
    def __add__(self, other):
        assert (self.row == other.row) and (self.col == other.col), "Assertion Error !!"
    
        for i in range(self.row):
            for j in range(self.col):
                self.array[i][j]=self.data[i][j] + other.data[i][j]  
        return Matrix(self.array)
    
    def __sub__(self, other):
        assert (self.row == other.row) and (self.col == other.col), "Assertion Error !!"
        
        for i in range(self.row):
            for j in range(self.col):
                self.array[i][j]=self.data[i][j] - other.data[i][j]  
        return Matrix(self.array)  
    
    def __mul__(self, other):
        if type(other) == Matrix:
            assert self.col == other.row, "Assertion Error!!"
        
            matmul_array = [[0] * self.row for i in range(other.col)]
        
            for i in range(len(matmul_array)):
                for j in range(len(matmul_array[0])):
                    for k in range(self.col):
                        matmul_array[i][j] += self.data[j][k] * other.data[k][i]
            return Matrix(matmul_array)
        else:
            for i in range(self.row):
                for j in range(self.col):
                    self.array[i][j] = other * self.data[i][j]
            return Matrix(self.array)
    
    def __rmul__(self, other):
        for i in range(self.row):
            for j in range(self.col):
                self.array[i][j] = other * self.data[i][j]        
        return Matrix(self.array)