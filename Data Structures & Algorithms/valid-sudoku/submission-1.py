class Solution:
    def getRow(self, board: List[List[str]], index: int, start:int=0, end:int=9) -> set:
            return board[index][start:end]

    def getCol(self, board: List[List[str]], index: int, start:int=0, end:int=9) -> set:
            return [row[index] for row in board][start:end]

    def getSubBox(self, board: List[List[str]], index: int) -> set:
        SUB_INDICES = {
            0: ([0,3], [0,3]),
            1: ([0,3], [3,6]),
            2: ([0,3], [6,9]),

            3: ([3,6], [0,3]),
            4: ([3,6], [3,6]),
            5: ([3,6], [6,9]),

            6: ([6,9], [0,3]),
            7: ([6,9], [3,6]),
            8: ([6,9], [6,9])
        }
        
        row_set, col_set = SUB_INDICES[index]
        subBox = []
        for row in range(row_set[0],row_set[1]):
            subBox += (self.getRow(
                board = board,
                index = row,
                start = col_set[0],
                end = col_set[1]
            ))
        return subBox

    def isValid(self, sudokuPart: List) -> bool:
        VALID = {"1","2","3","4","5","6","7","8","9","."}        
        # print(f"\t{sudokuPart}")
        length_nine = len(sudokuPart) == 9

        sudokuPart = [elem for elem in sudokuPart if elem!="."]
        part_length = len(sudokuPart)

        deduplicated_part = set(sudokuPart)
        deduplicated_length = len(deduplicated_part)
        no_duplicates = part_length == deduplicated_length
        
        valid_alphabets = deduplicated_part <= VALID

        # print(f"\tLength 9 = {length_nine}")
        # print(f"\tValid alphabets = {valid_alphabets}")
        # print(f"\tNo duplicates = {no_duplicates}")

        return (
            length_nine and no_duplicates and valid_alphabets
        )

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValid(self.getRow(board=board,index=i)):
                return False
            # print(f"Row {i} valid? = {self.isValid(self.getRow(board=board,index=i))}")
            
            if not self.isValid(self.getCol(board=board,index=i)):
                return False
            # print(f"Col {i} valid? = {self.isValid(self.getCol(board=board,index=i))}")
            
            if not self.isValid(self.getSubBox(board=board,index=i)):
                return False
            # print(f"Sub-box {i} valid? = {self.isValid(self.getSubBox(board=board,index=i))}")

        return True
                
        # sub box:
        # 1 -> rows [0,3), cols [0,3)
        # 2 -> rows [0,3), cols [3,6)
        # 3 -> rows [0,3), cols [6,9)

        # 4 -> rows [3,6), cols [0,3)
        # 5 -> rows [3,6), cols [3,6)
        # 6 -> rows [3,6), cols [6,9)

        # 7 -> rows [6,9), cols [0,3)
        # 8 -> rows [6,9), cols [3,6)
        # 9 -> rows [6,9), cols [6,9)