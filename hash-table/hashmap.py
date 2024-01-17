class HashMap:
    def __init__(self, size):
        self.hash_table = [[],] * size
        self.size = size

    
    def checkPrime(self,n):
        if n == 1 or n == 0:
            return 0

        for i in range(2, n//2):
            if n % i == 0:
                return 0

        return 1
    
    def getPrime(self,n):
        if n % 2 == 0:
            n = n + 1

        while not self.checkPrime(n):
            n += 2

        return n
    
    def hashFunction(self, key):
        """
        hash is independent of the size of the hash table. 
        hash is reduced to an index – a number between 0, the start of the array, and array_size - 1, 
        the end of the array – using the modulo (%) operator
        """

        hash = self.getPrime(key)
        return hash % self.size


    def insertData(self, key, data):
        index = self.hashFunction(key)
        self.hash_table[index] = [key, data]

    def removeData(self, key):
        index = self.hashFunction(key)
        self.hash_table[index] = 0

    def search(self,key):
        index = self.hashFunction(key)
        return self.hash_table[index]

if __name__ == "__main__":
    hashmap = HashMap(10)
    hashmap.insertData(123, "apple")
    hashmap.insertData(532, "mango")
    hashmap.insertData(213, "banana")
    hashmap.insertData(654, "guava")

    print(hashmap.hash_table)

    print(hashmap.search(213))
    