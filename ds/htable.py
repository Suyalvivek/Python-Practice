class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self,key):
        h=0
        for  ch in key:
            h+=ord(ch)
        return h % self.MAX
    def add(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
    def remove(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]

ht = HashTable()
print(ht.arr)
ht.add('vivek','handsome')
print(ht.arr)
print(ht.get('vivek'))