class HashTable:
    def __init__(self):
        self.size = 10
        self.map = [None]*self.size
    
    def _get_hash(self, key):
        return key % self.size
    
    def _linear_probing(self, key, index):
        return (self._get_hash(key)+ index) % self.size
    
    def _probing(self, key):
        for index in range(self.size):
            probe_hash = self._linear_probing(key, index)
            if (self.map[probe_hash] is None) or (self.map[probe_hash] == 'deleted'):
                return probe_hash
        return None
    
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        if self.map[key_hash] is None:
            self.map[key_hash] = key_value
        else:
            key_hash = self._probing(key)
            if key_hash is None:
                return False
            self.map[key_hash] = key_value
        return True

    def print_all(self):
        print("==== ISI DARI HASH TABLE ====")
        for item in self.map:
            if item is not None:
                print(f"NIM: {item[0]} NAMA: {item[1]}")

    def get_data(self, key):
        key_hash = self._get_hash(key)
        for i in range(self.size):
            probe_hash = self._linear_probing(key, i)
            if self.map[probe_hash] is not None:
                if self.map[probe_hash][0] == key:
                    return self.map[probe_hash][1]
            else:
                break
        return None
    
    def resize(self, size):
        map_lama = self.map
        self.size = size
        self.map = [None] * self.size
        
        for item in map_lama:
            if item is not None and item != 'deleted':
                self.add(item[0], item[1])

def main():
    ht : HashTable = HashTable()
    # isi hash table
    ht.add(71210689, "Gian")
    ht.add(71210683, "Yandi")
    ht.add(71210699, "Andreas")

    print("==== HASH TABLE SEBELUM DIRESIZE ====")
    print()
    ht.print_all()
    print(f"mahasiswa dengan NIM 71210683 adalah {ht.get_data(71210683)}")
    print()
    # resize hash table
    ht.resize(3)

    print("==== HASH TABLE SETELAH DIRESIZE ====")
    print()
    ht.print_all()
    print(f"mahasiswa dengan NIM 71210683 adalah {ht.get_data(71210683)}")
    

if __name__ == "__main__":
    main()