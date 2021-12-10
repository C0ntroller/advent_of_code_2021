class Board:
    def __init__(self, numbers):
        self.numbers = []
        self.lut = {}
        for i in range(5):
            self.numbers.append([[x, False] for x in numbers[i]])
            for j in range(5):
                self.lut[numbers[i][j]] = (i, j)
    
    def draw(self, no):
        idx = self.lut.get(no, None)
        if idx is None:
            return False, None
        self.numbers[idx[0]][idx[1]][1] = True
        return self.check_for_win(no)
    
    def check_for_win(self, no):
        # horizontal
        for r in self.numbers:
            if sum([1 for x in r if x[1]]) == 5:
                return True, self.calculate_score(no)
        # vertical
        for i in range(5):
            if sum([1 for j in range(5) if self.numbers[j][i][1]]) == 5:
                return True, self.calculate_score(no)
        # diagonals don't count..............
        """diag = [self.numbers[0][0],self.numbers[1][1],self.numbers[2][2],self.numbers[3][3],self.numbers[4][4]]
        if sum([1 for e in diag if e[1]]) == 5:
            return True, self.calculate_score(no)
        diag = [self.numbers[0][4],self.numbers[1][3],self.numbers[2][2],self.numbers[3][1],self.numbers[4][0]]
        if sum([1 for e in diag if e[1]]) == 5:
            return True, self.calculate_score(no)"""
        
        return False, None

    def calculate_score(self, no):
        score = 0
        for i in range(5):
            for j in range(5):
                score += self.numbers[i][j][0] if not self.numbers[i][j][1] else 0
        return score * no
    
    def __str__(self):
        string = ""
        for i in range(5):
            row = "["
            for j in range(5):
                nmb = f"\033[92m{self.numbers[i][j][0]}\033[0m" if self.numbers[i][j][1] else str(self.numbers[i][j][0])
                row += nmb + "\t"
            row += "]"
            string += row + "\n"
        return string


with open("day04_data.txt") as data:
    d = [x.strip() for x in data.readlines()]
    numbers = [int(x) for x in d[0].split(",")]
    d = d[1:]
boards = []
for i in range(len(d) // 6):
    b = []
    for j in range(1,6):
        r = [int(x) for x in d[6*i+j].split()]
        b.append(r)
    boards.append(Board(b))

for no in numbers:
    pop_list  = []
    for i in range(len(boards)):
        result = boards[i].draw(no)
        if result[0]:
            print(f"Board {i} wins! Score: {result[1]}")
            # Part 1
            # exit()
            # Part 2
            pop_list.append(i)
    for i in range(len(pop_list)):
        boards.pop(pop_list[-(i+1)])
