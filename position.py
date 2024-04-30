class Position:
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column

    @property
    def row(self) -> int:
        return self.__row
    
    @row.setter
    def row(self, value: int) -> None:
        self.__row = value

    @property
    def column(self) -> int:
        return self.__column
    
    @column.setter
    def column(self, value: int) -> None:
        self.__column = value