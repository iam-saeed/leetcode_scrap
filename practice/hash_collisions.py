class HashTableEntry:
    # Linked list hash table key/value pair
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    # A hash table with `capacity` buckets that accepts string keys 
    def __init__(self, capacity):
        self.capacity = capacity  # number of buckets inside a hash table
        self.storage = [None] * capacity
        self.item_count = 0 # will count the number of items in the hash table
    
    def get_num_slots(self):
        # Return the length of the list to hold the hash table data. Not the numer of items stored in the hash table, but the number of slots in the main list. One of the tests relies on this.
        return len(self.storage)
    
    def djb2(self, key):
        # cast the key to a string and get bytes
        str_key = str(key).encode()

        # start from a arbitrary large prime number
        hash_value = 5381

        # bit shift and sum the value for each character
        for bit in str_key:
            hash_value = ((hash_value << 5) + hash_value) + bit
            hash_value &= 0xffffffff
        return hash_value

    def hash_index(self, key):
        # takes an arbitrary key and returns a valid integer index between within the storage capacity of the hash table 
        return self.djb2(key) % self.capacity
    
    def put(self, key, value):
        # stores the value with a given key
        index = self.hash_index(key)
        # look to the first value of the index
        current_entry = self.storage[index]
        # searches for the correct key inputted
        while current_entry is not None and current_entry.key != key:
            current_entry = current_entry.next
        # if current entry does exist reassign value to entry, if it does not exist make a new entry and enter it at the head
        if current_entry is not None:
            current_entry.value = value
        else:
            new_entry = HashTableEntry(key, value)
            new_entry.next = self.storage[index]
            self.storage[index] = new_entry
        return 

    def delete(self, key):
        # remove the value stored with the given key. Print a warning if the key is not found
        index = self.index(key)
        current_entry = self.storage[index]

        while current_entry is not None and current_entry.key != key:
            current_entry = current_entry.next
        if current_entry is not None:
            self.storage[index] = None
        else:
            print("The key inputted is not found")
    
    def get(self, key):
        # retrieves a value stored with a given key. Will return None if no key is found
        index = self.hash_index(key)
        current_entry = self.storage[index]
        while current_entry is not None and current_entry.key != key:
            current_entry = current_entry.next
        if current_entry is not None:
            return self.storage[index]
