class DynamicArray:
    
    def __init__(self, capacity: int):
        self._arr = dict()
        self._capacity = capacity
        self._size = 0
        self._back = -1


    def get(self, i: int) -> int:
        return self._arr[i]


    def set(self, i: int, n: int) -> None:
        self._arr[i] = n

    def getSize(self) -> int:
        return self._size
    
    def getCapacity(self) -> int:
        return self._capacity

    def resize(self) -> None:
        self._capacity *= 2

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            print("Resizing: ",self._size,self._capacity)
            self.resize()
            print("New size: ",self._size,self._capacity)
        
        self._back += 1
        self._arr[self._back] = n
        self._size += 1

        

    def popback(self) -> int:
        print("back = ",self._back)
        self._back -= 1
        self._size -= 1
        print("new back = ",self._back)
        return self._arr[self._back + 1]