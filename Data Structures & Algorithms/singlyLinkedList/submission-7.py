class LinkedList:
    
    def __init__(self):
        self._LL = list()
        self._tail = -1

    
    def get(self, index: int) -> int:
        try:
            return self._LL[index]
        except IndexError:
            return -1
        

    def insertHead(self, val: int) -> None:
        self._LL = [val] + self._LL
        self._tail += 1
        print(self._LL)
        print("Tail = ", self._tail)

    def insertTail(self, val: int) -> None:
        self._LL.append(val)
        self._tail += 1

    def remove(self, index: int) -> bool:
        if index not in range(len(self._LL)):
            return False
        
        self._LL = self._LL[:index] + self._LL[index+1:]
        return True

    def getValues(self) -> List[int]:
        return self._LL
        
