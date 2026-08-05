'''
1.	Create an array of a fixed size (say 8 or 16 slots).
2. Initialize every slot as empty.
3. When inserting, hash the key to determine the array index.
4. Store the key and value together at that index.

'''


class MyHashSet:

    def __init__(self):
        # will initlize the object with 100 empty elements 
        self.storage = [[] for _ in range(100)]
        

    def add(self, key: int) -> None:

        # get the index 
        bucket_index = key % len(self.storage)
        # first check if we already contain it
        if self.contains(key): return 
        # otherwise store it      # store it in the bucket 
        else: self.storage[bucket_index].append(key)


        

    def remove(self, key: int) -> None:
        # look up the index 
        bucket_index = key % len(self.storage)
        # check if we have the element 
        if self.contains(key):
            self.storage[bucket_index].remove(key)
        

    def contains(self, key: int) -> bool:
        # 1. hash the key 
        bucket_index = key % len(self.storage)
        #   2. search the bucket
        for num in self.storage[bucket_index]:
            # if the key is in the bucket return true
            if key == num: return True
        
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)