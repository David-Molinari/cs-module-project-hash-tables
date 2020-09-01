class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class LinkedList:
    def __init__(self):
        self.head = None
#     def __str__(self):
#         """Print entire linked list."""
# ​
#         if self.head is None:
#             return "[Empty List]"
# ​
#         cur = self.head
#         s = ""
# ​
#         while cur != None:
#             s += f'({cur.value})'
# ​
#             if cur.next is not None:
#                 s += '-->'
# ​
#             cur = cur.next
# ​
#         return s

    def find(self, key):
        cur = self.head

        while cur is not None:
            if cur.key == key:
                return cur

            cur = cur.next

        return None

    def delete(self, key):
        cur = self.head

        # Special case of deleting head

        if cur.key == key:
            self.head = cur.next
            return cur

        # General case of deleting internal node

        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.key == key:  # Found it!
                prev.next = cur.next   # Cut it out
                return cur  # Return deleted node
            else:
                prev = cur
                cur = cur.next

        return None  # If we got here, nothing found

    def insert_at_head(self, node):
            node.next = self.head
            self.head = node

    def insert_or_overwrite_value(self, node):
        this_node = self.find(node.key)

        if this_node is None:
            # Make a new node
            self.insert_at_head(node)

        else:
            # Overwrite old value
            this_node.value = node.value

    def return_list(self):
        if self.head == None:
            return None
        else:
            this_list = []
            cur = self.head
            while cur != None:
                this_list.append(cur)
                next_node = cur.next
                cur = next_node
            for i in this_list:
                print(i.key, i.value)
            return this_list




class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.load = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        load_factor = self.load / self.capacity
        return load_factor




    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # Your code here
        hval = 0x811c9dc5
        fnv_32_prime = 0x01000193
        uint32_max = 2 ** 32
        for s in key:
            hval = hval ^ ord(s)
            hval = (hval * fnv_32_prime) % uint32_max
        return hval


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        new_node = HashTableEntry(key, value)
        index = self.hash_index(key)
        if self.table[index] == None:
            self.table[index] = LinkedList()
            self.table[index].insert_at_head(new_node)
            self.load += 1
            if self.get_load_factor() > .7:
                self.resize(self.capacity * 2)
        else:
            self.table[index].insert_or_overwrite_value(new_node)
        

         

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.table[index] == None:
            print("Nothing here")
        elif self.table[index].find(key) == None:
            print("Nothing here")
        else:
            self.table[index].delete(key)
            self.load -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.table[index] == None:
            return None
        elif self.table[index].find(key) != None:
            return self.table[index].find(key).value
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_table = HashTable(new_capacity)
        
        for i in self.table:
            if i != None:
                this_list = i.return_list()
                if len(this_list) > 0:
                    for e in this_list:
                        new_table.put(e.key, e.value)
        self.table = new_table



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
