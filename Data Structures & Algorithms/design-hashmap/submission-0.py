class MyHashMap:

    def __init__(self):
        self.storage = [[] for _ in range(100)]
        

    def put(self, key: int, value: int) -> None:
        bucket_index = key % len(self.storage)
        bucket = self.storage[bucket_index]

        # if the bucket exists update it 
        for i ,(storedKey, val) in enumerate(bucket):
            if storedKey == key: 
                bucket[i] = (key, value)
                return
        # otherwise add the next bucket
        bucket.append((key,value))


    def get(self, key: int) -> int:
          # 1. hash the key 
        bucket_index = key % len(self.storage)
        #   2. search the bucket
        for Storedkey, val in self.storage[bucket_index]:
            # if the key is in the bucket return true
            if key == Storedkey: return val
        
        return -1
        

    def remove(self, key: int) -> None:
        # look up the index 
        bucket_index = key % len(self.storage)
        bucket = self.storage[bucket_index]

        # if the bucket exists update it 
        for i, (storedKey, val) in enumerate(bucket):
            if storedKey == key: 
                bucket.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)