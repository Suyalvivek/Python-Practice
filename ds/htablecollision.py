# COLLISION PREVENTION USING CHAINING

class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr = [[] for i in range(self.MAX)]
    def get_hash(self,key):
        h = 0
        for char in key:
            h+=ord(char)
        return h%self.MAX

    def add(self,key,value):
        h = self.get_hash(key)
        found = False
        for idx,elem in enumerate(self.arr[h]):
            if len(elem)==2 and elem[0]==key:
                self.arr[h][idx] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))

    def get(self,key):
        h = self.get_hash(key)
        for elem in self.arr[h]:
            if elem[0] == key:
                return elem[1]

    def remove(self,key):
        h = self.get_hash(key)
        for idx,elem in enumerate(self.arr[h]):
            if elem[0] == key:
                self.arr[h].remove(elem)

htc = HashTable()
htc.add('vivek','smart man')
print(htc.arr)
print(htc.get('vivek'))
