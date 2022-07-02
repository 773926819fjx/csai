class MyList:
    def __init__(self, myList):
        self.myList = myList

    def __getitem__(self, index):
        return self.myList[index]

    def __setitem__(self, index, key):
        self.myList[index] = key

    def __delitem__(self, index):
        del self.myList[index]


myList1 = MyList([2, 4, 6, 8, 10])
print(myList1[1:5])
