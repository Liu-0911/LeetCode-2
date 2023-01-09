class Test:
    def __init__(self,len):
        self.LenOfHashTable = len

    def hashkey(self,key):
        return key % self.LenOfHashTable

    def printkey(self,key):
        key1 = hashkey(key)
        key2 = self.hashkey(key)
        print(key1)
        print(key2)

t = Test(500)
t.printkey(20000000000000)